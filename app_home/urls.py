"""
URL patterns for the home app.
"""
from django.urls import path
from . import views

app_name = 'app_home'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
]