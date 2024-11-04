from django.urls import path
from .views import MovieDetailView, ReviewCreateView, ReviewUpdateView, ReviewDeleteView, actor_detail, ActorsListView, UserReviewsView
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('movie/<int:pk>/review/new/', views.ReviewCreateView.as_view(), name='create-review'),
    path('reviews/<int:pk>/update/', ReviewUpdateView.as_view(), name='update-review'),
    path('reviews/<int:pk>/delete/', ReviewDeleteView.as_view(), name='delete-review'),
    path('reviews/<int:pk>/', views.review, name='movie-review'),
    path('user/<int:user_id>/reviews/', UserReviewsView.as_view(), name='user_reviews'),
    path('search', views.search, name='search'),
    path('movie/<int:movie_id>/toggle_watchlist/', views.toggle_watchlist, name='toggle_watchlist'),
    path('movie/<int:movie_id>/toggle_favourites/', views.toggle_favourites, name='toggle_favourites'),
    path('filters/', views.filters, name='filters'),
    path('actor/<int:pk>/', actor_detail, name='actor-detail'),
    path('actors/', ActorsListView.as_view(), name='actors-list'),
    # path('actors/', actor_list, name='actor-list'),
]