"""
URL patterns for the booking app.
"""
from django.urls import path
from . import views

app_name = 'app_booking'

urlpatterns = [
    path('', views.public_booking, name='public_booking'),
    path('success/<int:pk>/', views.booking_success, name='booking_success'),
    path('list/', views.appointment_list, name='appointment_list'),
    path('<int:pk>/', views.appointment_detail, name='appointment_detail'),
    path('create/', views.appointment_create, name='appointment_create'),
    path('<int:pk>/update/', views.appointment_update, name='appointment_update'),
    path('<int:pk>/delete/', views.appointment_delete, name='appointment_delete'),
]