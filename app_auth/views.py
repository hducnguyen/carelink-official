"""
Views for the auth app.
"""
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from .forms import LoginForm

def login_view(request):
    """View for user login."""
    if request.user.is_authenticated:
        return redirect('app_staff:dashboard')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, _('Login successful.'))
                
                # Redirect to the next page if provided, otherwise to dashboard
                next_page = request.GET.get('next', 'app_staff:dashboard')
                return redirect(next_page)
            else:
                messages.error(request, _('Invalid username or password.'))
    else:
        form = LoginForm()
    
    context = {
        'title': _('Login'),
        'form': form,
    }
    return render(request, 'app_auth/login.html', context)

@login_required
def logout_view(request):
    """View for user logout."""
    logout(request)
    messages.success(request, _('Logout successful.'))
    return redirect('app_home:home')