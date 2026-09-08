from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from .models import Movie

# Create your views here.
# LEARNER NOTE: a "view" in Django is just a Python function (or class)
# that takes a request and returns a response -- this is the core of
# the request/response cycle. When a browser asks for a URL, Django's
# URLconf (movies/urls.py) matches it to one of the functions below and
# calls it with an HttpRequest object; whatever that function returns
# (almost always built with render() or redirect(), see below) becomes
# the HttpResponse sent back to the browser. Every view in this project
# takes `request` as its first parameter -- Django always passes it in,
# and it carries everything about the incoming request: request.method
# ('GET'/'POST'), request.GET / request.POST (submitted form/query
# data), request.user (the logged-in user, thanks to
# AuthenticationMiddleware), request.path (the URL path), etc.

def index(request):
    # Movie.objects.all() asks the ORM (the layer that translates Python
    # into SQL) for every row in the movies_movie database table, as a
    # QuerySet of Movie instances -- roughly "SELECT * FROM
    # movies_movie". QuerySets are lazy: the actual SQL only runs once
    # you iterate over them, which happens here inside the template's
    # {% for movie in movies %} loop, not on this line.
    movies = Movie.objects.all()

    # `context` is just a plain dict mapping template-variable names to
    # Python values. Whatever key you use here (e.g. 'movies') is
    # exactly the name you reference inside the template with
    # {{ movies }} or {% for movie in movies %} -- see
    # templates/movies/list.html.
    context = {
        'movies': movies
    }
    # render() is the standard way a view produces an HTML response: it
    # (1) finds the named template (searching each app's templates/
    # folder and the project-level templates/ dir configured in
    # settings.py), (2) renders it using `context` plus anything added
    # automatically by the context processors (request, user, messages),
    # and (3) wraps the resulting HTML in an HttpResponse for you.
    return render(request, 'movies/list.html', context)

# get_object_or_404 was new to me here - much cleaner than a manual
# try/except around a 404 response.
def detail(request, movie_id):
    # movie_id arrives here as a plain Python int, already converted by
    # the <int:movie_id> path converter in movies/urls.py.
    # get_object_or_404(Movie, pk=movie_id) tries Movie.objects.get(pk=
    # movie_id) (pk = "primary key", i.e. the auto-generated id column)
    # and, if no row with that id exists, automatically raises Http404
    # -- which Django turns into a proper "404 Not Found" page -- instead
    # of letting an unhandled Movie.DoesNotExist exception crash the
    # request with a 500 error.
    movie = get_object_or_404(Movie, pk = movie_id)
    context = {
        'movie': movie
    }
    return render(request, 'movies/detail.html', context)

def search(request):
    # This view doesn't pass any context at all -- it just renders a
    # static search page/template. (There's no search *logic* here yet;
    # the template itself, movies/search.html, is likewise just a
    # placeholder heading for now.)
    return render(request, 'movies/search.html')

