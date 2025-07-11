"""
ASGI config for taskmanager project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# Set the default settings module for the 'taskmanager' project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taskmanager.settings')

# This is the ASGI application used by Django's runserver and any ASGI server
application = get_asgi_application()
