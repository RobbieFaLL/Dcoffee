from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.booking_view, name='booking_view'),
    path('booking-success/', views.booking_success, name='booking_success'),
]
