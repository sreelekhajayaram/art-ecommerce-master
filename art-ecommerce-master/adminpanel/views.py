from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
import csv
from reportlab.pdfgen import canvas
from io import BytesIO

from shop.models import Category, Product, Order, OrderItem
from shop.models import ProductImage
from booking.models import PortraitBooking
from accounts.models import UserProfile
from .forms import CategoryForm, ProductForm

User = get_user_model()


@staff_member_required
def dashboard(request):
    data = {
        'products': Product.objects.count(),
        'orders': Order.objects.count(),
        'bookings': PortraitBooking.objects.count(),
        'users': UserProfile.objects.count(),
    }
    latest_orders = Order.objects.select_related('user').order_by('-created_at')[:5]
    latest_bookings = PortraitBooking.objects.select_related('user').order_by('-created_at')[:5]
    return render(request, 'adminpanel/dashboard.html', {
        'stats': data,
        'latest_orders': latest_orders,
        'latest_bookings': latest_bookings,
    })


@staff_member_required
def export_orders_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="orders.csv"'
    writer = csv.writer(response)
    writer.writerow(['ID', 'User', 'Total', 'Payment Status', 'Order Status', 'Created'])
    for order in Order.objects.select_related('user'):
        writer.writerow([order.id, order.user.username, order.total_price, order.payment_status, order.order_status, order.created_at])
    return response


@staff_member_required
def export_bookings_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="bookings.csv"'
    writer = csv.writer(response)
    writer.writerow(['ID', 'User', 'Name', 'Email', 'Phone', 'Price', 'Status', 'Preferred Date'])
    for booking in PortraitBooking.objects.select_related('user'):
        writer.writerow([booking.id, booking.user.username, booking.name, booking.email, booking.phone, booking.price, booking.booking_status, booking.preferred_date])
    return response


@staff_member_required
def export_users_pdf(request):
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 800, "Users List")
    y = 760
    for profile in UserProfile.objects.select_related('user'):
        text = f"{profile.user.email} — role: {profile.role} — joined: {profile.user.date_joined.strftime('%Y-%m-%d')}"
        p.drawString(60, y, text)
        y -= 20
    p.showPage()
    p.save()
    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/pdf')


@staff_member_required
def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'
    writer = csv.writer(response)
    writer.writerow(['Email', 'Role', 'Date Joined', 'Last Login'])
    for user in User.objects.select_related('profile').all().order_by('-date_joined'):
        role = getattr(getattr(user, 'profile', None), 'role', '')
        writer.writerow([
            user.email,
            role,
            user.date_joined.strftime('%Y-%m-%d'),
            user.last_login.strftime('%Y-%m-%d') if user.last_login else '',
        ])
    return response


@staff_member_required
def user_list(request):
    query = request.GET.get('q', '').strip()
    users = User.objects.select_related('profile').all().order_by('-date_joined')
    if query:
        users = users.filter(email__icontains=query)
    return render(request, 'adminpanel/users.html', {
        'users': users,
        'query': query,
    })


@staff_member_required
def catalog(request):
    cat_form = CategoryForm(request.POST or None, request.FILES or None, prefix="cat")
    prod_form = ProductForm(request.POST or None, request.FILES or None, prefix="prod")

    if request.method == "POST":
        if "cat-submit" in request.POST and cat_form.is_valid():
            cat_form.save()
            messages.success(request, "Category saved.")
            return redirect('admin_catalog')
        if "prod-submit" in request.POST and prod_form.is_valid():
            product = prod_form.save()
            # handle multiple images
            images = request.FILES.getlist('images')
            for img in images:
                ProductImage.objects.create(product=product, image=img)
            messages.success(request, "Product saved.")
            return redirect('admin_catalog')

    categories = Category.objects.prefetch_related('products').all().order_by('name')
    products = Product.objects.select_related('category').order_by('-created_at')

    # Handle search filters
    category_search = request.GET.get('category_search', '').strip()
    product_search = request.GET.get('product_search', '').strip()

    if category_search:
        categories = categories.filter(name__icontains=category_search) | categories.filter(description__icontains=category_search)

    if product_search:
        products = products.filter(title__icontains=product_search) | products.filter(description__icontains=product_search)

    return render(request, 'adminpanel/catalog.html', {
        'categories': categories,
        'products': products,
        'cat_form': cat_form,
        'prod_form': prod_form,
    })


@staff_member_required
def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    form = CategoryForm(request.POST or None, request.FILES or None, instance=category)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Category updated.")
        return redirect('admin_catalog')
    return render(request, 'adminpanel/edit_category.html', {'form': form, 'category': category})


@staff_member_required
def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        category.delete()
        messages.success(request, "Category deleted.")
        return redirect('admin_catalog')
    return render(request, 'adminpanel/confirm_delete.html', {'object': category, 'type': 'Category'})


@staff_member_required
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if request.method == "POST":
        if form.is_valid():
            try:
                prod = form.save()
                # handle new uploaded images
                images = request.FILES.getlist('images')
                for img in images:
                    ProductImage.objects.create(product=prod, image=img)
                messages.success(request, "Product updated.")
                return redirect('admin_catalog')
            except Exception as e:
                messages.error(request, f"Error saving product: {str(e)}")
        else:
            messages.error(request, "Please correct the errors below.")
    return render(request, 'adminpanel/edit_product.html', {'form': form, 'product': product})


@staff_member_required
def delete_product_image(request, pk):
    img = get_object_or_404(ProductImage, pk=pk)
    product_id = img.product.id
    if request.method == 'POST':
        img.delete()
        messages.success(request, "Image removed.")
        return redirect('edit_product', pk=product_id)
    return render(request, 'adminpanel/confirm_delete.html', {'object': img, 'type': 'Product Image'})


@staff_member_required
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        messages.success(request, "Product deleted.")
        return redirect('admin_catalog')
    return render(request, 'adminpanel/confirm_delete.html', {'object': product, 'type': 'Product'})


@staff_member_required
def portrait_orders(request):
    """View for managing portrait booking orders"""
    query = request.GET.get('q', '').strip()
    status_filter = request.GET.get('status', '').strip()

    bookings = PortraitBooking.objects.select_related('user').order_by('-created_at')

    if query:
        bookings = bookings.filter(
            name__icontains=query
        ) | bookings.filter(
            email__icontains=query
        ) | bookings.filter(
            order_id__icontains=query
        )

    if status_filter:
        bookings = bookings.filter(booking_status=status_filter)

    return render(request, 'adminpanel/portrait_orders.html', {
        'bookings': bookings,
        'query': query,
        'status_filter': status_filter,
    })


@staff_member_required
def download_reference_image(request, booking_id):
    """Download reference image for a portrait booking"""
    booking = get_object_or_404(PortraitBooking, id=booking_id)
    if not booking.reference_image:
        messages.error(request, "No reference image found for this booking.")
        return redirect('portrait_orders')

    # Get the file
    file_path = booking.reference_image.path
    with open(file_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{booking.reference_image.name.split("/")[-1]}"'
        return response



