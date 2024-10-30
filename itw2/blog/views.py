from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Movie, Review
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from users.models import Watchlist
from django.shortcuts import get_object_or_404, redirect
from .forms import GenreForm, LanguageForm, RatingForm


def home(request):
    engmovies = Movie.objects.filter(language="English")
    hindimovies = Movie.objects.filter(language="Hindi")
    context = {
        'engmovies': engmovies,
        'hindimovies': hindimovies,
        'topeng': engmovies[:5],
        'tophindi': hindimovies[:5]
    }
    return render(request, 'blog/home.html', context)



class MovieDetailView(DetailView):
    model = Movie
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        movie = self.object
        context['reviews'] = Review.objects.filter(movie=movie.title).order_by('-date_posted')
        return context



def review(request, pk):
    movie = Movie.objects.get(id=pk)
    context = {
        'reviews' : Review.objects.filter(movie=movie.title).order_by('-date_posted')
    }
    return render(request, 'blog/movie_detail.html', context)



class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['movie','content','userRating']

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)
    


class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    fields = ['movie','content','userRating']

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        review = self.get_object()
        if self.request.user == review.username:
            return True
        return False



class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    success_url = 'blog/reviews.html'

    def test_func(self):
        review = self.get_object()
        if self.request.user == review.username:
            return True
        return False



def search(request):
    query = request.GET['query']
    context = {
        'movies' : Movie.objects.filter(title__icontains=query)
    }
    return render(request, 'blog/search.html', context)



@login_required
def toggle_watchlist(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    watchlist_item, created = Watchlist.objects.get_or_create(user=request.user, movie=movie)
    
    if not created:  # If already in watchlist, remove it
        watchlist_item.delete()
        message = "Removed from your watchlist"
    else:
        message = "Added to your watchlist"
    
    return redirect('movie-detail', pk=movie_id)  # Redirect to movie detail page



def filters(request):
    selected_genre = None
    selected_language = None
    selected_rating = None

    movies = Movie.objects.all()  

    if request.method == 'POST':
        genre_form = GenreForm(request.POST)
        language_form = LanguageForm(request.POST)
        rating_form = RatingForm(request.POST)

        if genre_form.is_valid() and language_form.is_valid() and rating_form.is_valid():
            selected_genre = genre_form.cleaned_data['genre']
            selected_language = language_form.cleaned_data['language']
            selected_rating = rating_form.cleaned_data['rating']

            # Filter by genre if it's not "all"
            if selected_genre != 'all':
                movies = movies.filter(genre__icontains=selected_genre)

            # Filter by language if it's not "all"
            if selected_language != 'all':
                movies = movies.filter(language__icontains=selected_language)

            # Filter by rating
            if selected_rating != 'all':
                movies = movies.filter(rating__gte=float(selected_rating))

    else:
        genre_form = GenreForm()
        language_form = LanguageForm()
        rating_form = RatingForm()

    return render(request, 'blog/filter.html', {
        'genre_form': genre_form,
        'language_form': language_form,
        'rating_form': rating_form,
        'movies': movies,
    })

