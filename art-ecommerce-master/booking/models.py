from django.conf import settings
from django.db import models
import django.utils.timezone


from django.conf import settings
from django.db import models
import django.utils.timezone


class PortraitBooking(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    pincode = models.CharField(max_length=15)
    # Categories for portrait booking (keeps stored value simple)
    CATEGORY_CHOICES = [
        ('paintings', 'Paintings'),
        ('pencil', 'Pencil Drawings'),
        ('caricature', 'Caricatures'),
        ('stencil', 'Stencil Artworks'),
        ('mural', 'Kerala Murals'),
    ]
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='paintings')
    reference_image = models.ImageField(upload_to='bookings/')
    description = models.TextField(blank=True)
    size = models.CharField(max_length=50)
    preferred_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    BOOKING_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('paid', 'Paid'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    booking_status = models.CharField(max_length=20, choices=BOOKING_STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(default=django.utils.timezone.now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='portrait_bookings')

    def __str__(self):
        return f"PortraitBooking {self.id} - {self.name}"


class Size(models.Model):
    name = models.CharField(max_length=100)
    dimensions = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    reference_image = models.ImageField(upload_to='size_references/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.dimensions})"


