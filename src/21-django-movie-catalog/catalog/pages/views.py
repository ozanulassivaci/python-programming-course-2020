from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# http://127.0.0.1:8000

# Both views below are about as simple as a Django view gets: they take
# no URL parameters, look nothing up from the database, and pass no
# context dict to render() -- they just render a static template
# (Django still fills in the parts that come from context processors,
# like {{ user }} and the messages block, automatically). Compare with
# movies/views.py, where index() and detail() build a context dict of
# database data before rendering.
def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')