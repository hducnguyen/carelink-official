"""
URL patterns for the staff app.
"""
from django.urls import path
from . import views

app_name = 'app_staff'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('list/', views.staff_list, name='staff_list'),
    path('<int:pk>/', views.staff_detail, name='staff_detail'),
    path('create/', views.staff_create, name='staff_create'),
    path('<int:pk>/update/', views.staff_update, name='staff_update'),
    path('<int:pk>/delete/', views.staff_delete, name='staff_delete'),
]