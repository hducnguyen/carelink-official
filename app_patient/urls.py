"""
URL patterns for the patient app.
"""
from django.urls import path
from . import views

app_name = 'app_patient'

urlpatterns = [
    path('search/', views.patient_search, name='patient_search'),
    path('<int:pk>/', views.patient_detail, name='patient_detail'),
    path('list/', views.patient_list, name='patient_list'),
    path('create/', views.patient_create, name='patient_create'),
    path('<int:pk>/update/', views.patient_update, name='patient_update'),
    path('<int:pk>/delete/', views.patient_delete, name='patient_delete'),
]