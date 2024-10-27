from django.urls import path
from .views import MovieDetailView, ReviewCreateView, ReviewUpdateView, ReviewDeleteView
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('reviews/new/', ReviewCreateView.as_view(), name='create-review'),
    path('reviews/<int:pk>/update/', ReviewUpdateView.as_view(), name='update-review'),
    path('reviews/<int:pk>/delete/', ReviewDeleteView.as_view(), name='delete-review'),
    path('reviews/<int:pk>/', views.review, name='movie-review')
]