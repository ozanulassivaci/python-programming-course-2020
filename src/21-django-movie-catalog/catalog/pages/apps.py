from django.apps import AppConfig


# Standard per-app configuration, one per app -- see movies/apps.py for
# the fuller explanation. The `name` here must match this app's entry
# ('pages') in settings.py's INSTALLED_APPS.
class PagesConfig(AppConfig):
    name = 'pages'
