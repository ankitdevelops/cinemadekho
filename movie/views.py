from django.shortcuts import get_object_or_404, render
from genre . models import Genre
from movie . models import Movie
# Create your views here.

def movie(request, genre = None):
    if genre != None:
        genre = get_object_or_404(Genre, genre = genre)
        movies = Movie.objects.all().filter(genre = genre)
    else:
        movies = Movie.objects.all()
    
    context = {
        'movies':movies
    }

    return render(request, 'movie/movie.html', context)

def watch(request, genre, movie_name_slug):
    try:
        watch_movie = Movie.objects.get(genre__genre = genre, movie_name_slug = movie_name_slug)
        single_movie = Movie.objects.filter()
    except Exception as e:
        raise e
    context = {
        'watch_movie':watch_movie,
    }
    
    return render(request, 'movie/watch.html', context)