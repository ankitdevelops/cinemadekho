from pages.models import slider
from django.shortcuts import render
from movie . models import Movie
from . models import slider
# Create your views here.

def home(request):
    movies_on_homepage = Movie.objects.all().filter(on_homepage = True)
    sliders = slider.objects.all()
    context = {
        'movies_on_homepage':movies_on_homepage,
        'sliders':sliders,
    }
    return render(request, 'pages/home.html', context)