"""
Views for the home app.
"""
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from .models import AboutContent

def home_view(request):
    """View for the home page."""
    context = {
        'title': _('Private Clinic Management System'),
        'welcome_message': _('Welcome to our Private Clinic Management System'),
    }
    return render(request, 'app_home/home.html', context)

def about_view(request):
    """View for the about page."""
    about_contents = AboutContent.objects.all()
    context = {
        'title': _('About Our Project'),
        'about_contents': about_contents,
    }
    return render(request, 'app_home/about.html', context)