from django.db import models

# Create your models here.
# The "user" app doesn't define its own model here -- it relies entirely
# on django.contrib.auth's built-in User model (imported directly in
# user/views.py as `from django.contrib.auth.models import User`) for
# storing accounts, passwords, etc. That's a common pattern: this app
# just supplies the login/register/logout *views* and templates around
# an account system Django already provides.
