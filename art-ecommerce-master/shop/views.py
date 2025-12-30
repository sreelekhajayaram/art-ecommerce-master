from decimal import Decimal
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.http import JsonResponse
import json

from .forms import CheckoutForm
from .models import CartItem, Category, Order, OrderItem, Product
from booking.forms import STATE_CITY_MAP


def home(request):
    categories = Category.objects.all()

    # Handle search and category filtering
    category_slug = request.GET.get('category')
    search_query = request.GET.get('search')

    # Start with base queryset
    products = Product.objects.order_by('-created_at')

    if category_slug:
        try:
            category = Category.objects.get(slug=category_slug)
            products = products.filter(category=category)
        except Category.DoesNotExist:
            products = Product.objects.none()

    if search_query:
        products = products.filter(title__icontains=search_query) | products.filter(description__icontains=search_query)

    # Apply slice after filtering
    products = products[:6]

    return render(request, 'home.html', {'products': products, 'categories': categories})


def category_view(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()
    return render(request, 'category.html', {'category': category, 'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product_detail.html', {'product': product})


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    qty = int(request.POST.get('quantity', 1))
    qty = max(1, qty)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += qty
    else:
        cart_item.quantity = qty
    cart_item.save()
    messages.success(request, f"Added {product.title} to cart.")
    return redirect('cart')


@login_required
def cart_view(request):
    items = CartItem.objects.filter(user_id=request.user.id).select_related('product')
    subtotal = sum(item.line_total for item in items)
    return render(request, 'cart.html', {'items': items, 'subtotal': subtotal})


@login_required
def update_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    qty = int(request.POST.get('quantity', 1))
    cart_item.quantity = max(1, qty)
    cart_item.save()
    messages.success(request, "Cart updated.")
    return redirect('cart')


@login_required
def remove_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    cart_item.delete()
    messages.success(request, "Item removed from cart.")
    return redirect('cart')


@login_required
def checkout(request):
    items = CartItem.objects.filter(user_id=request.user.id).select_related('product')
    if not items.exists():
        messages.warning(request, "Your cart is empty.")
        return redirect('home')
    subtotal = sum(item.line_total for item in items)

    initial = {
        'name': request.user.get_full_name() or request.user.username,
        'email': request.user.email,
    }
    if request.method == 'POST':
        form = CheckoutForm(request.POST, user=request.user)
        if form.is_valid():
            request.session['checkout_data'] = form.cleaned_data
            request.session['checkout_total'] = str(subtotal)
            return redirect('payment_portal')
    else:
        form = CheckoutForm(initial=initial, user=request.user)

    context = {
        'form': form,
        'items': items,
        'subtotal': subtotal,
        'state_city_map': json.dumps(STATE_CITY_MAP)
    }
    return render(request, 'checkout.html', context)


@login_required
def payment_portal(request):
    booking_id = request.session.get('booking_pending')
    if booking_id:
        from booking.models import PortraitBooking
        booking = PortraitBooking.objects.filter(id=booking_id, user_id=request.user.id).first()
        if not booking:
            messages.error(request, "Booking not found.")
            return redirect('booking')
        subtotal = booking.price
        return render(request, 'payment_portal.html', {'items': [], 'subtotal': subtotal, 'booking': booking})

    items = CartItem.objects.filter(user_id=request.user.id).select_related('product')
    if not items.exists():
        messages.warning(request, "Your cart is empty.")
        return redirect('home')
    subtotal = sum(item.line_total for item in items)
    checkout_data = request.session.get('checkout_data')
    if not checkout_data:
        return redirect('checkout')
    return render(request, 'payment_portal.html', {'items': items, 'subtotal': subtotal})


@login_required
def order_success(request, order_id):
    user = request.user
    order = get_object_or_404(Order, id=order_id, user_id=user.id)
    return render(request, 'order_success.html', {'order': order})


def order_failed(request):
    messages.error(request, "Payment failed. Please try again.")
    return render(request, 'order_failed.html')


def _create_order_from_cart(user, checkout_data):
    items = CartItem.objects.filter(user_id=user.id).select_related('product')
    order = Order.objects.create(
        user_id=user.id,
        shipping_name=checkout_data.get('name'),
        shipping_email=checkout_data.get('email'),
        shipping_phone=checkout_data.get('phone'),
        shipping_address=checkout_data.get('address'),
        shipping_city=checkout_data.get('city'),
        shipping_state=checkout_data.get('state'),
        shipping_pincode=checkout_data.get('pincode'),
        payment_status='paid',
        order_status='pending',
    )
    for item in items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price,
        )
        # reduce stock safely
        if item.product.stock >= item.quantity:
            item.product.stock -= item.quantity
            item.product.save(update_fields=['stock'])
    order.update_totals()
    items.delete()
    return order


@login_required
def simulate_success(request):
    checkout_data = request.session.get('checkout_data')
    booking_id = request.session.get('booking_pending')
    user = request.user
    # Force evaluation of lazy proxy by accessing .id early
    user_id = user.id
    if booking_id:
        from booking.models import PortraitBooking
        booking = PortraitBooking.objects.filter(id=booking_id, user_id=user_id).first()
        if booking:
            booking.booking_status = 'paid'
            booking.save(update_fields=['booking_status'])
            request.session.pop('booking_pending', None)
            return redirect('booking_success', booking_id=booking.id)
    if not checkout_data:
        return redirect('checkout')
    order = _create_order_from_cart(request.user, checkout_data)
    request.session.pop('checkout_data', None)
    request.session.pop('checkout_total', None)
    return redirect('order_success', order_id=order.id)


@login_required
def simulate_failure(request):
    request.session.pop('checkout_data', None)
    request.session.pop('checkout_total', None)
    request.session.pop('booking_pending', None)
    messages.error(request, "Payment failed.")
    return redirect('order_failed')


@login_required
def place_order_cod(request):
    """Place an order for Cash On Delivery without processing card payment.
    Expects a POST request. Returns JSON with redirect URL to dashboard.
    """
    if request.method != 'POST':
        return redirect('payment_portal')

    checkout_data = request.session.get('checkout_data')
    booking_id = request.session.get('booking_pending')
    user = request.user
    # Force evaluation of lazy proxy by accessing .id early
    user_id = user.id

    if booking_id:
        from booking.models import PortraitBooking
        booking = PortraitBooking.objects.filter(id=booking_id, user_id=user_id).first()
        if booking:
            # mark booking as pending payment (COD)
            booking.booking_status = 'pending'
            booking.save(update_fields=['booking_status'])
            request.session.pop('booking_pending', None)
            return JsonResponse({'redirect_url': reverse('booking_success', args=[booking.id])})

    if not checkout_data:
        return JsonResponse({'redirect_url': reverse('checkout')})

    # Create order (uses helper which defaults to paid) then change status to pending for COD
    order = _create_order_from_cart(user, checkout_data)
    order.payment_status = 'pending'
    order.save(update_fields=['payment_status'])
    request.session.pop('checkout_data', None)
    request.session.pop('checkout_total', None)
    messages.success(request, "Order placed. Please pay on delivery.")
    return JsonResponse({'redirect_url': reverse('user_dashboard')})
