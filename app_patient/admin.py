"""
Admin configuration for the patient app.
"""
from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    """Admin configuration for the Patient model."""
    list_display = ('name', 'phone', 'dob', 'gender', 'created_at')
    list_filter = ('gender', 'created_at')
    search_fields = ('name', 'phone', 'medical_history')
    date_hierarchy = 'created_at'