from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=100, verbose_name='Movie Title')
    description = models.TextField(verbose_name='Movie Description')
    image = models.CharField(max_length=50, verbose_name='Movie Image')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Date Added')
    isPublished = models.BooleanField(default= True)

    def __str__(self):
        return self.name

    # Storing just the filename and building the path here instead of using
    # an ImageField was the simple approach I went with at this stage.
    def get_image_path(self):
        return '/img/'+ self.image