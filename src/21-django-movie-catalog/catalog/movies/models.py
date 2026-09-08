from django.db import models

# Create your models here.

# LEARNER NOTE: what is a "model"?
# A Django model is a Python class that describes one database table.
# Each class attribute that's set to a models.<Something>Field becomes
# one column in that table, and its type (CharField, TextField, ...)
# tells Django what kind of column to create (VARCHAR, TEXT, ...) and
# what validation to apply in forms/the admin. Every subclass of
# models.Model automatically gets an auto-incrementing integer primary
# key column called "id" for free -- you never have to declare it
# yourself, and it's what lets movies/urls.py match a movie by
# <int:movie_id> and views.py look it up with pk=movie_id.
#
# Note that defining this class does NOT create the database table by
# itself. Whenever you add/change a model like this, you run
# `python manage.py makemigrations` to generate a "migration" -- a small
# Python file (see movies/migrations/) that records the exact schema
# change -- and then `python manage.py migrate` to actually apply it to
# the database file (db.sqlite3, per DATABASES in settings.py).
class Movie(models.Model):
    # CharField is for short, fixed-maximum-length text stored in a
    # single line -- max_length=100 is required by Django (it's used to
    # size the database column and to validate input) and means "at most
    # 100 characters", not "always exactly 100". verbose_name overrides
    # the human-readable label Django would otherwise derive from the
    # field name (it would default to "name") -- this is what makes the
    # admin site and auto-generated forms show "Movie Title" instead.
    name = models.CharField(max_length=100, verbose_name='Movie Title')
    # TextField is for long-form text with no practical length limit --
    # unlike CharField it doesn't require (or generally use) max_length,
    # and most databases store it differently (e.g. as a TEXT column
    # rather than VARCHAR), which is why it's the right choice for a
    # movie's full description instead of a CharField.
    description = models.TextField(verbose_name='Movie Description')
    # This field just stores an image's *filename* (e.g. "1.jpg") as
    # plain text -- notice it's a CharField, not Django's dedicated
    # models.ImageField. A real ImageField would handle file uploads,
    # store the file under MEDIA_ROOT and validate that it's actually an
    # image; here, images are simply pre-placed in catalog/static/img/
    # and this field just remembers which one belongs to which movie (see
    # get_image_path() below, which turns "1.jpg" into "/img/1.jpg" for
    # use with the {% static %} template tag).
    image = models.CharField(max_length=50, verbose_name='Movie Image')
    # DateTimeField stores a full date+time value. auto_now_add=True
    # means Django automatically sets this field to "now" the *first*
    # time the row is created, and then never touches it again on later
    # saves -- perfect for a "when was this added" timestamp, and it's
    # also why this field never appears in a form for editing a movie:
    # auto_now_add fields are read-only by design. (The similar-sounding
    # auto_now=True, not used here, would instead update the timestamp on
    # *every* save -- useful for "last modified" fields instead.)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Date Added')
    # BooleanField stores True/False and maps to a checkbox in forms and
    # the admin. default=True means a Movie is published by default when
    # created unless explicitly set otherwise. This flag is what lets
    # movies/admin.py toggle a movie's visibility directly from the admin
    # list view via list_editable (see movies/admin.py) -- although note
    # that the views in this project (movies/views.py) currently show
    # every movie regardless of isPublished; the flag itself doesn't
    # filter the public listing.
    isPublished = models.BooleanField(default= True)

    # __str__ controls how a Movie instance is displayed as text -- most
    # importantly, in the Django admin's object lists and dropdowns
    # (e.g. "Movie object (1)" would show there instead if this method
    # weren't defined), and anywhere else Python converts the object to a
    # string, such as an f-string or print().
    def __str__(self):
        return self.name

    # Storing just the filename and building the path here instead of using
    # an ImageField was the simple approach I went with at this stage.
    # This is a normal Python instance method (not a model field) that
    # every Movie object gets. Templates can call it like a plain
    # attribute -- {% static movie.get_image_path %} in list.html/
    # detail.html -- because Django's template language automatically
    # calls any no-argument callable it finds when you do
    # "object.something" in a template.
    def get_image_path(self):
        return '/img/'+ self.image