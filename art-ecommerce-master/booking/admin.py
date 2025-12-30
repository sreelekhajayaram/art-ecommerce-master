from django.contrib import admin
from django.utils.html import format_html
from .models import PortraitBooking


@admin.register(PortraitBooking)
class PortraitBookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'size', 'booking_status', 'price', 'created_at']
    list_filter = ['booking_status', 'created_at']
    search_fields = ['name', 'email', 'phone']
    readonly_fields = ['created_at', 'user', 'price']
    fieldsets = (
        ('User Info', {'fields': ('user', 'name', 'email', 'phone')}),
        ('Address', {'fields': ('address', 'city', 'state', 'pincode')}),
        ('Booking Details', {'fields': ('size', 'preferred_date', 'price', 'reference_image', 'description')}),
        ('Status', {'fields': ('booking_status', 'created_at')}),
    )

    def reference_image_tag(self, obj):
        if obj.reference_image:
            return format_html('<a href="{}" target="_blank">Download / View</a>', obj.reference_image.url)
        return '-'
    reference_image_tag.short_description = 'Reference Image'


# Size model is not defined in this app; remove registration

























