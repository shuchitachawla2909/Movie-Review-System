from django.shortcuts import render
from .models import Movie

def home(request):
    return render(request, 'blog/home.html')

def movie(request):
    context = {
        'movies' : Movie.objects.all()
    }
    return render(request, 'blog/darkknight.html', context)