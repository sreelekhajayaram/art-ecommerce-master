from django.urls import path
from .views import logout_view, login_view, register_user, user_dashboard

urlpatterns = [
    path('logout/', logout_view, name="logout"),
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path('dashboard/', user_dashboard, name="user_dashboard"),
]
