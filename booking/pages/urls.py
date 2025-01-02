from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Index page
    path('order/', views.order_view, name='order'),  # Order form page
    path('success/', views.success_view, name='success'),  # Success page after placing an order
    path('view_order/', views.view_order, name='view_order'),  # View a specific order page
    path('terms/', views.terms_view, name='terms'),
    path('privacy/', views.privacy_view, name='privacy'),
]
