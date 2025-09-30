"""
Models for the patient app.
"""
from django.db import models
from django.utils.translation import gettext_lazy as _

class Patient(models.Model):
    """Model representing a patient."""
    name = models.CharField(_('Full Name'), max_length=100)
    phone = models.CharField(_('Phone Number'), max_length=15, unique=True)
    dob = models.DateField(_('Date of Birth'), null=True, blank=True)
    gender = models.CharField(_('Gender'), max_length=10, choices=[
        ('male', _('Male')),
        ('female', _('Female')),
        ('other', _('Other')),
    ], blank=True)
    address = models.TextField(_('Address'), blank=True, null=True)
    medical_history = models.TextField(_('Medical History'), blank=True, null=True)
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)

    class Meta:
        verbose_name = _('Patient')
        verbose_name_plural = _('Patients')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.phone}"