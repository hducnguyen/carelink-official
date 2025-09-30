"""
Admin configuration for the home app.
"""
from django.contrib import admin
from .models import AboutContent

@admin.register(AboutContent)
class AboutContentAdmin(admin.ModelAdmin):
    """Admin configuration for the AboutContent model."""
    list_display = ('title', 'order')
    list_editable = ('order',)
    search_fields = ('title', 'content')