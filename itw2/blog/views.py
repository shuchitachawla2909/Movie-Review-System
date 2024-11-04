from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from .models import Movie, Review, Actor
from users.models import Watchlist, Favourites
from .forms import GenreForm, LanguageForm, RatingForm
from .forms import ReviewForm
import django_filters
from .filters import MovieFilter


def home(request):
    engmovies = Movie.objects.filter(language="English")
    hindimovies = Movie.objects.filter(language="Hindi")
    actors = Actor.objects.all()
    context = {
        'engmovies': engmovies,
        'hindimovies': hindimovies,
        'topeng': engmovies[:5],
        'tophindi': hindimovies[:5],
        'actors': actors[:6],
        'title': 'Home'  # Set the title for the Home view
    }
    return render(request, 'blog/home.html', context)


class MovieDetailView(DetailView):
    model = Movie

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        movie = self.object
        context['reviews'] = Review.objects.filter(movie=movie).order_by('-date_posted')
        context['title'] = movie.title  # Set the title to the movie's title
        return context


def review(request, pk):
    movie = Movie.objects.get(id=pk)
    context = {
        'reviews': Review.objects.filter(movie=movie.title).order_by('-date_posted'),
        'title': f'Reviews for {movie.title}'  # Set the title for the review page
    }
    return render(request, 'blog/movie_detail.html', context)


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

    def get_initial(self):
        initial = super().get_initial()
        movie_id = self.kwargs.get('pk')
        movie = get_object_or_404(Movie, id=movie_id)
        initial['movie'] = movie  # Set the initial value for the movie field
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Review'
        context['movie'] = get_object_or_404(Movie, id=self.kwargs.get('pk'))
        return context


class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    fields = ['movie', 'content', 'userRating']

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

    def test_func(self):
        review = self.get_object()
        return self.request.user == review.username

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Review'  # Set the title for the review edit page
        return context


class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    success_url = 'blog/reviews.html'

    def test_func(self):
        review = self.get_object()
        return self.request.user == review.username

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete Review'  # Set the title for the review deletion page
        return context


class UserReviewsView(ListView):
    model=Review
    template_name='users/user_reviews.html'
    context_object_name='reviews'

    def get_queryset(self):
        user_id=self.kwargs['user_id']
        return Review.objects.filter(username_id=user_id).order_by('-date_posted')


def search(request):
    query = request.GET['query']
    context = {
        'movies': Movie.objects.filter(title__icontains=query),
        'title': 'Search Results'  # Set the title for the search results page
    }
    return render(request, 'blog/search.html', context)


@login_required
def toggle_watchlist(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    watchlist_item, created = Watchlist.objects.get_or_create(user=request.user, movie=movie)

    if not created:
        watchlist_item.delete()
        message = "Removed from your watchlist"
    else:
        message = "Added to your watchlist"
    
    return redirect('movie-detail', pk=movie_id)


@login_required
def toggle_favourites(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    favourites_item, created = Favourites.objects.get_or_create(user=request.user, movie=movie)

    if not created:
        favourites_item.delete()
        message = "Removed from your favourites"
    else:
        message = "Added to your favourites"
    
    return redirect('movie-detail', pk=movie_id)


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

            if selected_genre != 'all':
                movies = movies.filter(genre__icontains=selected_genre)
            if selected_language != 'all':
                movies = movies.filter(language__icontains=selected_language)
            if selected_rating != 'all':
                movies = movies.filter(rating__gte=float(selected_rating))

    else:
        genre_form = GenreForm()
        language_form = LanguageForm()
        rating_form = RatingForm()

    context = {
        'genre_form': genre_form,
        'language_form': language_form,
        'rating_form': rating_form,
        'movies': movies,
        'title': 'Filter Movies'  # Set the title for the filter page
    }
    return render(request, 'blog/filter.html', context)


def actor_detail(request, pk):
    actor = get_object_or_404(Actor, pk=pk)
    context = {
        'actor': actor,
        'title': actor.name  # Set the title to the actor's name
    }
    return render(request, 'blog/actor_detail.html', context)


class ActorsListView(ListView):
    model = Actor
    template_name = 'actors_list.html'
    context_object_name = 'actors'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actors List'  # Set the title for the actors list page
        return context


