from django.db import models
from django.urls import reverse
# Create your models here.

class Genre(models.Model):
    genre = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.genre

    def get_url(self):
        return reverse('movie_by_genre', args=[self.genre])