from django.contrib import admin
from . models import Movie
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {"movie_name_slug":('movie_name',)}
    list_display = ('movie_name','genre','on_homepage')
    list_editable = ('on_homepage',)
    list_display_links = ('movie_name','genre',)


admin.site.register(Movie,MovieAdmin)