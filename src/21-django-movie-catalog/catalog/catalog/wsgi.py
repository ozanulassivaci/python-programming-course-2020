"""
WSGI config for catalog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/

LEARNER NOTE: WSGI (Web Server Gateway Interface) is the standard
Python spec for how a web server talks to a Python web application --
it defines a simple "application(environ, start_response)" calling
convention. You will normally never call anything in this file
yourself: a production web server (e.g. gunicorn, uWSGI, mod_wsgi)
imports the `application` object defined below and calls it once per
incoming HTTP request, and Django takes it from there (running
middleware, matching urlpatterns, calling your view, etc.). During
local development, `python manage.py runserver` plays that same "web
server" role for you.
"""

import os

from django.core.wsgi import get_wsgi_application

# Tell Django which settings module to use (catalog/settings.py) before
# anything else happens -- Django can't do anything (including building
# the `application` callable below) without knowing its configuration
# first. setdefault() only sets this if it isn't already set, so an
# environment variable configured outside this file would take priority.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'catalog.settings')

# Build the actual WSGI-compatible callable that a web server will invoke
# for every request. Everything about how a request becomes a response
# (middleware, URL routing, views, templates) happens inside this object.
application = get_wsgi_application()
