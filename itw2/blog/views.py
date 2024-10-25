from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Movie, Review
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home(request):
    context = {
        'movies' : Movie.objects.all()
    }
    return render(request, 'blog/home.html', context)


class MovieDetailView(DetailView):
    model = Movie


def review(request):
    context = {
        'reviews' : Review.objects.all()
    }
    ordering = ['-date_posted']
    return render(request, 'blog/reviews.html', context)


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
