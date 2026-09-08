from django.urls import path
from . import views

# LEARNER NOTE: this is an app-level URLconf, included from the
# project's catalog/urls.py under the 'movies/' prefix. Each entry below
# matches what's LEFT of the URL after that prefix has already been
# stripped off, which is why the paths here look like '', '<int:...>'
# and 'search' rather than 'movies/', 'movies/<int:...>' etc.

# 127.0.0.1:8000/movies
# 127.0.0.1:8000/movies/2
# 127.0.0.1:8000/movies/search

# Mapping URLs to view functions like this made routing click for me.
urlpatterns = [
    # '' matches the prefix exactly, i.e. /movies/ with nothing after it
    # -> calls views.index. The `name='movies'` argument gives this
    # specific route a stable, code-independent name; instead of
    # hard-coding '/movies/' anywhere else, templates and views use
    # {% url 'movies' %} / reverse('movies') and Django looks the actual
    # path up for you -- so if this URL's path ever changed, nothing
    # referencing it by name would need to change.
    path('', views.index, name= 'movies'),
    # <int:movie_id> is a path converter: it matches one or more digits
    # in that segment of the URL, converts them to a Python int, and
    # passes the result to the view as the movie_id keyword argument --
    # so /movies/2 calls views.detail(request, movie_id=2). If that
    # segment weren't a valid integer (e.g. /movies/abc), this pattern
    # simply wouldn't match and Django would try the next one instead.
    path('<int:movie_id>', views.detail, name= 'detail'),
    # A fixed, literal path segment ('search') with no dynamic part --
    # matches /movies/search exactly.
    path('search', views.search, name= 'search'),
]