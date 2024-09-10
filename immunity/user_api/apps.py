"""
Конфигурация приложения.
"""

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UserApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    verbose_name = _("Управление пользователями")
    name = 'user_api'
