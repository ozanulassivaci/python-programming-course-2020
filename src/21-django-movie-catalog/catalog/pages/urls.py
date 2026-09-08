from django.urls import path
from . import views

# http://127.0.0.1:8000/

# The home page and about page for this small "pages" app. This
# app-level URLconf is included from catalog/urls.py under the '' (root)
# prefix, so these paths are exactly the final site URLs: '' -> the
# homepage (/), and 'about' -> /about. Note that 'index' and 'about' are
# both the view function names AND the `name=` used for {% url %} /
# reverse() lookups -- that's a naming convenience, not a requirement;
# the name argument could be anything as long as it's used consistently.
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
]