from django.urls import path
from . import views

app_name = 'feedback'

urlpatterns = [
    path('', views.feedback_list, name='feedback_list'),
    path('delete/<int:feedback_id>/', views.delete_feedback, name='delete_feedback'),
]
