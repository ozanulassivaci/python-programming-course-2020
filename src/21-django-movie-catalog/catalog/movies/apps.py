from django.apps import AppConfig


# LEARNER NOTE: every Django app has exactly one of these AppConfig
# subclasses (created automatically by `django-admin startapp`). It's
# app-level configuration -- Django uses it to identify the app
# internally and, in bigger apps, it's also where you'd hook in
# app-specific startup code (via a ready() method) such as registering
# signal handlers. This project doesn't need any of that, so the class
# below only sets the one required attribute: the app's importable
# Python name, which must match the app's entry in settings.py's
# INSTALLED_APPS list ('movies').
class MoviesConfig(AppConfig):
    name = 'movies'
