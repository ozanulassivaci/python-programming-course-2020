"""catalog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

# This is the PROJECT-level URLconf (as opposed to each app's own
# urls.py). Django starts here for every single request: it walks
# urlpatterns from top to bottom and uses the first path() that matches
# the request's URL. This file's job isn't to know about every URL in the
# site -- it's just to decide which app should handle which URL prefix,
# then hand off ("include") the rest of the URL to that app's own
# urls.py. That's what keeps each app's routes self-contained.

# http://127.0.0.1:8000/admin

urlpatterns = [
    # include('pages.urls') means: for any URL, first strip off this
    # path's prefix (here the prefix is '' -- nothing) and then let
    # pages/urls.py decide what to do with what's left. Since the prefix
    # is empty, this is effectively "everything pages/urls.py defines
    # lives at the site root", e.g. '' -> home page, 'about' -> about page.
    path('', include('pages.urls')),
    # Any URL starting with 'movies/' (e.g. /movies/, /movies/2,
    # /movies/search) is handed off to movies/urls.py, which matches
    # against the remainder of the URL after 'movies/' has been removed.
    path('movies/', include('movies.urls')),
    # Same idea for authentication-related URLs: /user/login/,
    # /user/register/, /user/logout/ are routed into user/urls.py.
    path('user/', include('user.urls')),
    # admin.site.urls is a URLconf that Django's admin app builds for you
    # automatically, covering every model registered with
    # admin.site.register(...) across the whole project (see the
    # admin.py file in each app). This is what makes /admin/ into a full
    # working "content management system" for free.
    path('admin/', admin.site.urls),
]
