"""
WSGI config for blog_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
# """

import os

from django.core.wsgi import get_wsgi_application

settings_module = 'blog_project.deployment' if 'WEBSITE_HOSTNAME' in os.environ else 'blog_project.settings'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_wsgi_application()
