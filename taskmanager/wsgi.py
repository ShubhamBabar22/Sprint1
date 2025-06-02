"""
WSGI config for taskmanager project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Set the default settings module for the 'taskmanager' project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taskmanager.settings')

# This is the WSGI application used by Django's runserver and any WSGI server
application = get_wsgi_application()
