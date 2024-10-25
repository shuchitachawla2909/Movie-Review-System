from django.shortcuts import render
from django.views.generic import DetailView
from .models import Movie

def home(request):
    context = {
        'movies' : Movie.objects.all()
    }
    return render(request, 'blog/home.html', context)


class MovieDetailView(DetailView):
    model = Movie
