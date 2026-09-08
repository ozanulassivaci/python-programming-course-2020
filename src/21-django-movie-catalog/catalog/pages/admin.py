from django.contrib import admin

# Register your models here.
# Nothing to register: pages/models.py defines no models, so there's
# nothing for the admin site to manage for this app. Compare with
# movies/admin.py, where admin.site.register(Movie, MovieAdmin) is what
# actually makes a model manageable at /admin/.
