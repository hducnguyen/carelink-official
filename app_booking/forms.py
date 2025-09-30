"""
Forms for the booking app.
"""
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Appointment
from app_patient.models import Patient
from app_staff.models import Staff

class PublicBookingForm(forms.Form):
    """Form for public appointment booking."""
    name = forms.CharField(
        label=_('Full Name'),
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Enter your full name')})
    )
    phone = forms.CharField(
        label=_('Phone Number'),
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Enter your phone number')})
    )
    doctor = forms.ModelChoiceField(
        label=_('Doctor'),
        queryset=Staff.objects.filter(role='doctor'),
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    appointment_date = forms.DateTimeField(
        label=_('Appointment Date and Time'),
        widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'})
    )
    note = forms.CharField(
        label=_('Notes (Optional)'),
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': _('Any special requests or information')})
    )

class AppointmentForm(forms.ModelForm):
    """Form for staff to create and update appointments."""
    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'appointment_date', 'status', 'note']
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-select'}),
            'doctor': forms.Select(attrs={'class': 'form-select'}),
            'appointment_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'note': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }