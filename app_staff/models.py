"""
Models for the staff app.
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class Staff(models.Model):
    """Model representing a staff member."""
    ROLE_CHOICES = [
        ('doctor', _('Doctor')),
        ('nurse', _('Nurse')),
        ('receptionist', _('Receptionist')),
        ('admin', _('Administrator')),
    ]
    
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='staff_profile',
        verbose_name=_('User Account')
    )
    name = models.CharField(_('Full Name'), max_length=100)
    role = models.CharField(_('Role'), max_length=20, choices=ROLE_CHOICES)
    specialization = models.CharField(_('Specialization'), max_length=100, blank=True, null=True)
    phone = models.CharField(_('Phone Number'), max_length=15, blank=True, null=True)
    bio = models.TextField(_('Biography'), blank=True, null=True)
    schedule = models.JSONField(_('Work Schedule'), default=dict, blank=True, null=True)
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)

    class Meta:
        verbose_name = _('Staff Member')
        verbose_name_plural = _('Staff Members')
        ordering = ['name']

    def __str__(self):
        return f"{self.name} - {self.get_role_display()}"