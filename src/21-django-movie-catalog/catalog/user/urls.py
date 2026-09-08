from django.urls import path
from . import views

# Included from catalog/urls.py under the 'user/' prefix, so these
# become /user/login/, /user/register/ and /user/logout/. Note that
# `views.login` here refers to the *local* login() function defined in
# user/views.py, not django.contrib.auth.views.LoginView -- this project
# rolls its own login/register/logout views by hand (see user/views.py)
# instead of using Django's built-in auth views, which is why the
# `from . import views` above matters: without it, `views.login` would
# be ambiguous.
urlpatterns = [
    path('login/', views.login, name= 'login'),
    path('register/', views.register, name= 'register'),
    path('logout/', views.logout, name= 'logout'),
]