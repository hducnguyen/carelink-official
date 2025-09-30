"""
Models for the home app.
"""
from django.db import models
from django.utils.translation import gettext_lazy as _

class AboutContent(models.Model):
    """Model for storing content for the About page."""
    title = models.CharField(_('Title'), max_length=200)
    content = models.TextField(_('Content'))
    order = models.IntegerField(_('Order'), default=0)
    
    class Meta:
        verbose_name = _('About Content')
        verbose_name_plural = _('About Contents')
        ordering = ['order']
    
    def __str__(self):
        return self.title