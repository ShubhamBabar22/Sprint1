"""
Application configuration for the tasks app.

This module contains the configuration class for the tasks application.
"""

from django.apps import AppConfig


class TasksConfig(AppConfig):
    """
    Configuration class for the tasks application.
    Defines the application name and any initialization code.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasks'
