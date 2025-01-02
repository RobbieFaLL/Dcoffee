from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.custom_login_view, name='login'),
    path('accounts/login/', views.custom_login_view, name='login'),
    # Use the built-in LogoutView and specify a custom template for logout
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('booking/', views.booking, name='booking'),
    path('booking/success/', views.booking_success, name='booking_success'),
]
