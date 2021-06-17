from django.db import models
from django.db.models.base import Model
from django.db.models.fields import DateField
from genre . models import Genre
from django.urls import reverse
# Create your models here.

class Movie(models.Model):
    movie_name = models.CharField(max_length=300, unique=True)
    movie_name_slug = models.SlugField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    movie_poster_link = models.URLField(max_length=500)
    movie_on_platform = models.CharField(max_length=100)
    movie_on_platform_link = models.URLField(max_length=2000)
    trailer_youtube_id = models.CharField(max_length=100)
    on_homepage = models.BooleanField(default=False)
    # movie_released_date = models.DateField(auto_now_add=False, blank=True)
    movie_added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.movie_name

    def get_url(self):
        return reverse('watch', args=[self.genre.genre, self.movie_name_slug])
