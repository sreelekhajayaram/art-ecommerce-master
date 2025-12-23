from django.urls import re_path
from .views import view_orders, view_single_order, user_orders


urlpatterns = [
    re_path(r'^$', view_orders, name='view_orders'),
    re_path(r'^order/(?P<pk>\d+)/$', view_single_order, name='order'),
    re_path(r'^userorder/$', user_orders, name='user_orders'),
]
