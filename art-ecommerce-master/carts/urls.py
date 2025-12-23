from django.urls import re_path
from .views import view_cart, add_to_cart, remove_from_cart, clear_cart


urlpatterns = [
    re_path(r'^$', view_cart, name='view_cart'),
    re_path(r'^add/(?P<pk>\d+)/$', add_to_cart, name='add_to_cart'),
    re_path(r'^remove/(?P<pk>\d+)/$', remove_from_cart, name='remove_from_cart'),
    re_path(r'^clear/$', clear_cart, name="clear_cart")
]
