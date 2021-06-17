from django.db import models

# Create your models here.

class slider(models.Model):
    banner_name = models.CharField(max_length=100,blank=True)
    banner_image_link = models.URLField()
    banner_link = models.URLField()

    def __str__(self):
        return self.banner_name
