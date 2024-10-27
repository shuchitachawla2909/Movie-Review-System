from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Movie, Review
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



def home(request):
    context = {
        'movies' : Movie.objects.all()[:5]
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



# def review(request, pk):
#     movie = Movie.objects.get(id=pk)
#     context = {
#         'reviews' : Review.objects.filter(movie=movie.title).order_by('-date_posted')
#     }
#     return render(request, 'blog/reviews.html', context)




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
