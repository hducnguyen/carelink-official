"""
Forms for the patient app.
"""
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Patient

class PatientForm(forms.ModelForm):
    """Form for creating and updating patients."""
    class Meta:
        model = Patient
        fields = ['name', 'phone', 'dob', 'gender', 'address', 'medical_history']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'medical_history': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }

class PatientSearchForm(forms.Form):
    """Form for searching patients by phone number."""
    phone = forms.CharField(
        label=_('Phone Number'),
        max_length=15,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Enter phone number')})
    )