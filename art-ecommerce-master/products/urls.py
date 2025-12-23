from django.urls import re_path
from .views import get_products, get_single_product
from .views import category_view


urlpatterns = [
    re_path(r'^$', get_products, name='get_products'),
    re_path(r'^(?P<pk>\d+)/$', get_single_product, name='get_single_product'),
    re_path(r'^category/(?P<slug>[-\w]+)/$', category_view, name='category_view'),
]
