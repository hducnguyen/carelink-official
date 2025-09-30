"""
Forms for the auth app.
"""
from django import forms
from django.utils.translation import gettext_lazy as _

class LoginForm(forms.Form):
    """Form for user login."""
    username = forms.CharField(
        label=_('Username'),
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Username')})
    )
    password = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': _('Password')})
    )