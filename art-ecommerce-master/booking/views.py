from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods
import json

from .forms import PortraitBookingForm, STATE_CITY_MAP, SIZE_DESCRIPTIONS
from .models import PortraitBooking, Size
from django.utils.crypto import get_random_string


@login_required
def booking_form(request):
    # No initial values - username must be entered manually
    if request.method == 'POST':
        form = PortraitBookingForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user

            # Calculate total price based on size and category
            size = form.cleaned_data.get('size')
            category = form.cleaned_data.get('category')

            # Size prices
            size_prices = {
                '8x10': 240,
                '11x14': 270,
                'A2': 250,
                'A3': 350,
                'A4': 300,
                '16x20': 400
            }

            # Category prices
            category_prices = {
                'pen_art': 200,
                'pencil': 500,
                'stencil': 500,
                'paintings': 500,
                'ghibli_art': 350,
                'caricature': 450
            }

            size_price = size_prices.get(size, 0)
            category_price = category_prices.get(category, 0)
            total_price = size_price + category_price

            booking.price = total_price
            booking.total_price = total_price
            booking.booking_status = 'pending'
            booking.save()
            messages.success(request, "Booking submitted. Complete payment to confirm.")
            request.session['booking_pending'] = booking.id
            return redirect('portrait_payment')
    else:
        form = PortraitBookingForm(user=request.user)

    context = {
        'form': form,
        'state_city_map': json.dumps(STATE_CITY_MAP),
        'size_descriptions': json.dumps(SIZE_DESCRIPTIONS)
    }
    return render(request, 'booking.html', context)


@login_required
def booking_success(request, booking_id):
    booking = get_object_or_404(PortraitBooking, id=booking_id, user=request.user)
    return render(request, 'booking_success.html', {'booking': booking})


@login_required
def portrait_booking(request):
    if request.method == 'POST':
        form = PortraitBookingForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user

            # Calculate total price based on size and category
            size = form.cleaned_data.get('size')
            category = form.cleaned_data.get('category')

            # Size prices
            size_prices = {
                '8x10': 240,
                '11x14': 270,
                'A2': 250,
                'A3': 350,
                'A4': 300,
                '16x20': 400
            }

            # Category prices
            category_prices = {
                'pen_art': 200,
                'pencil': 500,
                'stencil': 500,
                'paintings': 500,
                'ghibli_art': 350,
                'caricature': 450
            }

            size_price = size_prices.get(size, 0)
            category_price = category_prices.get(category, 0)
            total_price = size_price + category_price

            booking.price = total_price
            booking.total_price = total_price
            booking.booking_status = 'pending'
            booking.save()

            messages.success(request, "Booking submitted. Complete payment to confirm.")
            request.session['booking_pending'] = booking.id
            return redirect('portrait_payment')
        else:
            # Debug: Print form errors to console
            print("Form is not valid. Errors:", form.errors)
            print("Non-field errors:", form.non_field_errors())
            messages.error(request, "Please correct the errors in the form.")
    else:
        form = PortraitBookingForm(user=request.user)

    context = {
        'form': form,
        'state_city_map': json.dumps(STATE_CITY_MAP),
        'size_descriptions': json.dumps(SIZE_DESCRIPTIONS)
    }
    return render(request, 'booking.html', context)


@require_http_methods(["GET"])
def get_size_price(request):
    size_id = request.GET.get('size_id')
    try:
        size = Size.objects.get(id=size_id)
        return JsonResponse({
            'price': float(size.price),
            'image_url': size.reference_image.url if size.reference_image else ''
        })
    except Size.DoesNotExist:
        return JsonResponse({'price': 0, 'image_url': ''})


@require_http_methods(["GET"])
def size_reference_images(request):
    sizes = Size.objects.all()
    data = [{
        'id': size.id,
        'name': size.name,
        'dimensions': size.dimensions,
        'image_url': size.reference_image.url if size.reference_image else ''
    } for size in sizes]
    return JsonResponse({'sizes': data})


@require_http_methods(["GET"])
def get_cities_by_state(request):
    """API endpoint to get cities for a selected state"""
    state = request.GET.get('state', '')
    cities = STATE_CITY_MAP.get(state, [])
    return JsonResponse({'cities': cities})


@login_required
def portrait_payment(request):
    """Payment page for portrait bookings"""
    booking_id = request.session.get('booking_pending')
    if not booking_id:
        messages.error(request, "No pending booking found.")
        return redirect('booking')

    try:
        booking = PortraitBooking.objects.get(id=booking_id, user=request.user)
    except PortraitBooking.DoesNotExist:
        messages.error(request, "Booking not found.")
        return redirect('booking')

    if request.method == 'POST':
        # Process payment (dummy implementation)
        booking.booking_status = 'paid'
        booking.order_id = get_random_string(length=10, allowed_chars='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
        booking.save()

        # Clear session
        del request.session['booking_pending']

        messages.success(request, f"Payment successful! Order ID: {booking.order_id}")
        return redirect('booking_success', booking_id=booking.id)

    context = {
        'booking': booking,
        'subtotal': booking.total_price
    }
    return render(request, 'portrait_payment.html', context)
