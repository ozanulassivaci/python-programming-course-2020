from django.contrib import admin

# Register your models here.
# No custom models here to register (see user/models.py). Django's User
# model is already registered in the admin automatically by
# django.contrib.auth itself, which is why /admin/ shows a "Users" section
# even though this file never calls admin.site.register(User, ...).
