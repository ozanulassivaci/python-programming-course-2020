from django.apps import AppConfig


# Standard per-app configuration -- see movies/apps.py for the fuller
# explanation. `name` must match this app's entry ('user') in
# settings.py's INSTALLED_APPS.
class UserConfig(AppConfig):
    name = 'user'
