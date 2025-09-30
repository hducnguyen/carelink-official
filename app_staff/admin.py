"""
Admin configuration for the staff app.
"""
from django.contrib import admin
from .models import Staff

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    """Admin configuration for the Staff model."""
    list_display = ('name', 'role', 'specialization', 'phone')
    list_filter = ('role',)
    search_fields = ('name', 'specialization', 'bio')