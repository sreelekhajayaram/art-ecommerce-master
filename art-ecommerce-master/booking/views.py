from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods

from .forms import PortraitBookingForm
from .models import PortraitBooking, Size


@login_required
def booking_form(request):
    initial = {
        'name': request.user.get_full_name() or request.user.username,
        'email': request.user.email,
    }
    if request.method == 'POST':
        form = PortraitBookingForm(request.POST, request.FILES)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.booking_status = 'pending'
            booking.save()
            messages.success(request, "Booking submitted. Complete payment to confirm.")
            request.session['booking_pending'] = booking.id
            return redirect('payment_portal')
    else:
        form = PortraitBookingForm(initial=initial)
    return render(request, 'booking.html', {'form': form})


@login_required
def booking_success(request, booking_id):
    booking = get_object_or_404(PortraitBooking, id=booking_id, user=request.user)
    return render(request, 'booking_success.html', {'booking': booking})


@login_required
def portrait_booking(request):
    if request.method == 'POST':
        form = PortraitBookingForm(request.POST, request.FILES)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            size = form.cleaned_data.get('size')
            if size:
                booking.price = size.price
            booking.save()
            return redirect('booking_success')
    else:
        form = PortraitBookingForm()

    context = {'form': form}
    return render(request, 'booking_form.html', context)


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

