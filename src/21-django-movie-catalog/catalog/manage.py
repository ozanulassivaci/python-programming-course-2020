#!/usr/bin/env python
"""Django's command-line utility for administrative tasks.

LEARNER NOTE: this is the file you actually run from a terminal --
things like `python manage.py runserver` (start the development
server), `python manage.py makemigrations` (look at your models.py
files and generate migration files describing the database changes
needed), `python manage.py migrate` (apply those migration files to the
actual database, creating/altering tables) and
`python manage.py createsuperuser` (create an admin account for the
/admin site) all go through this script. It's a thin wrapper: its only
real job is telling Django which settings module to use, then handing
control off to Django's own command-line machinery.
"""
import os
import sys


def main():
    # Every manage.py command needs to know which settings module to load
    # (database config, installed apps, etc.) before it can do anything --
    # this points it at catalog/settings.py, the same module wsgi.py uses.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'catalog.settings')
    try:
        # Imported lazily, inside the try, so that a missing/inactive
        # Django installation produces the friendly error message below
        # instead of a raw, confusing ImportError traceback.
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # sys.argv is the list of command-line arguments this script was
    # invoked with, e.g. ['manage.py', 'runserver'] -- Django parses that
    # list itself to figure out which subcommand ("runserver",
    # "migrate", ...) to run and with what options.
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
