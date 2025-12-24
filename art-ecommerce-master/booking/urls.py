from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking_form, name='booking'),
    path('success/<int:booking_id>/', views.booking_success, name='booking_success'),
    path('api/get-size-price/', views.get_size_price, name='get_size_price'),
    path('api/size-references/', views.size_reference_images, name='size_references'),
    path('api/get-cities/', views.get_cities_by_state, name='get_cities'),
    path('portrait/', views.portrait_booking, name='portrait_booking'),
]



















