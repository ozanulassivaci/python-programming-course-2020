from django.contrib import admin
from .models import Movie

# LEARNER NOTE: django.contrib.admin is a full content-management
# website that Django can generate automatically from your models --
# it's what powers the /admin/ URL wired up in catalog/urls.py. Simply
# calling admin.site.register(Movie) at the bottom of this file would
# already be enough to manage Movie objects (list, add, edit, delete)
# at /admin/movies/movie/. The MovieAdmin class below is optional: it's
# a "ModelAdmin" subclass used purely to customize how that
# auto-generated interface looks and behaves for this particular model.

# Customizing ModelAdmin like this was a nice discovery - list_editable
# in particular lets me flip isPublished right from the list view.
class MovieAdmin(admin.ModelAdmin):
    # Which columns appear in the admin's list-of-movies table, and in
    # what order (left to right). Without this, the admin would only
    # show a single column with each movie's __str__().
    list_display = ('id','name','created_date','isPublished')
    # Of the columns listed above, which ones are clickable links that
    # take you to that movie's edit page. Here both "id" and "name" work
    # as links; the other columns are plain, non-clickable text.
    list_display_links = ('id','name')
    # Adds a filter sidebar on the right of the list page, letting staff
    # narrow the list down by created_date (e.g. "Today", "Past 7 days").
    list_filter = ('created_date',)
    # Makes the isPublished column directly editable as a checkbox right
    # there in the list table -- you can flip a movie's published state
    # without opening its full edit page. Any field listed here must
    # also appear in list_display (isPublished does, above).
    list_editable = ('isPublished',)
    # Adds a search box at the top of the list page that runs a
    # case-insensitive "contains" lookup across these two model fields.
    search_fields = ('name','description')
    # How many rows to show per page in the list view before Django
    # paginates to a second page.
    list_per_page = 20

# Register your models here.
# This is the line that actually plugs Movie into the admin site, using
# the customization defined above. Without a call like this, a model --
# no matter how it's defined in models.py -- simply will not show up
# anywhere under /admin/ at all.
admin.site.register(Movie, MovieAdmin)