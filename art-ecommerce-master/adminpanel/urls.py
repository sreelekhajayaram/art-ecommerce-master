from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='admin_dashboard'),
    path('export/orders/csv/', views.export_orders_csv, name='export_orders_csv'),
    path('export/bookings/csv/', views.export_bookings_csv, name='export_bookings_csv'),
    path('export/users/pdf/', views.export_users_pdf, name='export_users_pdf'),
    path('export/users/csv/', views.export_users_csv, name='export_users_csv'),
    path('users/', views.user_list, name='admin_users'),
    path('catalog/', views.catalog, name='admin_catalog'),
    path('catalog/category/<int:pk>/edit/', views.edit_category, name='edit_category'),
    path('catalog/category/<int:pk>/delete/', views.delete_category, name='delete_category'),
    path('catalog/product/<int:pk>/edit/', views.edit_product, name='edit_product'),
    path('catalog/product/<int:pk>/delete/', views.delete_product, name='delete_product'),
    path('catalog/product-image/<int:pk>/delete/', views.delete_product_image, name='delete_product_image'),
    path('portrait-orders/', views.portrait_orders, name='portrait_orders'),
    path('portrait-orders/<int:booking_id>/download-image/', views.download_reference_image, name='download_reference_image'),
]
