"""
App configuration for the staff app.
"""
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class AppStaffConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_staff'
    verbose_name = _('Staff Management')