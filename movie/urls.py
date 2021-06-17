from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie, name='movie'),
    path('<str:genre>/',views.movie,name='movie_by_genre'),
    path('<str:genre>/<slug:movie_name_slug>/',views.watch,name='watch'),
]
