from . models import Movie

def movie_link(request):
    movie_link = Movie.objects.filter(on_homepage = True)
    return dict(movie_link = movie_link)