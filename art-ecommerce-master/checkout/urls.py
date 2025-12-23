from django.urls import re_path
from .views import checkout

urlpatterns = [
    re_path(r'^$', checkout, name='checkout'),
]


