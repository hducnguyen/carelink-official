"""
App configuration for the home app.
"""
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class AppHomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_home'
    verbose_name = _('Home Page')