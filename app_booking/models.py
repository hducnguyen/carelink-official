"""
Models for the booking app.
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from app_patient.models import Patient
from app_staff.models import Staff

class Appointment(models.Model):
    """Model representing a patient appointment."""
    STATUS_CHOICES = [
        ('scheduled', _('Scheduled')),
        ('confirmed', _('Confirmed')),
        ('completed', _('Completed')),
        ('cancelled', _('Cancelled')),
        ('no_show', _('No Show')),
    ]
    
    patient = models.ForeignKey(
        Patient, 
        on_delete=models.CASCADE,
        verbose_name=_('Patient')
    )
    doctor = models.ForeignKey(
        Staff,
        on_delete=models.CASCADE,
        verbose_name=_('Doctor'),
        limit_choices_to={'role': 'doctor'}
    )
    appointment_date = models.DateTimeField(_('Appointment Date and Time'))
    status = models.CharField(
        _('Status'),
        max_length=20,
        choices=STATUS_CHOICES,
        default='scheduled'
    )
    note = models.TextField(_('Notes'), blank=True, null=True)
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)

    class Meta:
        verbose_name = _('Appointment')
        verbose_name_plural = _('Appointments')
        ordering = ['-appointment_date']

    def __str__(self):
        return f"{self.patient.name} - {self.doctor.name} - {self.appointment_date}"