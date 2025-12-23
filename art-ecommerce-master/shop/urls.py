from django.urls import path
from . import views
from home.views import about, contact_form, contact_view

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact_view, name='contact_view'),
    path('contact/form/', contact_form, name='contact_form'),
    path('category/<slug:slug>/', views.category_view, name='category_detail'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart_view, name='cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/update/<int:item_id>/', views.update_cart_item, name='update_cart_item'),
    path('cart/remove/<int:item_id>/', views.remove_cart_item, name='remove_cart_item'),
    path('checkout/', views.checkout, name='checkout'),
    path('payment/checkout/', views.payment_portal, name='payment_portal'),
    path('payment/success/', views.simulate_success, name='payment_success'),
    path('payment/failure/', views.simulate_failure, name='payment_failure'),
    path('payment/cod/', views.place_order_cod, name='payment_cod'),
    path('order/success/<int:order_id>/', views.order_success, name='order_success'),
    path('order/failed/', views.order_failed, name='order_failed'),
]

