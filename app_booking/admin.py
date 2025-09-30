"""
Admin configuration for the booking app.
"""
from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    """Admin configuration for the Appointment model."""
    list_display = ('patient', 'doctor', 'appointment_date', 'status', 'created_at')
    list_filter = ('status', 'doctor', 'appointment_date')
    search_fields = ('patient__name', 'doctor__name', 'note')
    date_hierarchy = 'appointment_date'