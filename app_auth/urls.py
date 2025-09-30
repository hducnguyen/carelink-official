"""
URL patterns for the auth app.
"""
from django.urls import path
from . import views

app_name = 'app_auth'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]