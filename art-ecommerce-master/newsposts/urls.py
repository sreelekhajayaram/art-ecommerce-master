from django.urls import re_path
from .views import get_newsposts, news_detail

urlpatterns = [
    re_path(r'^$', get_newsposts, name='get_newsposts'),
    re_path(r'^(?P<pk>\d+)/$', news_detail, name='news_detail'),
]