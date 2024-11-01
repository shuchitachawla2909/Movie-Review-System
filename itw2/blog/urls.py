from django.urls import path
from .views import MovieDetailView, ReviewCreateView, ReviewUpdateView, ReviewDeleteView, actor_detail
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('reviews/new/', ReviewCreateView.as_view(), name='create-review'),
    path('reviews/<int:pk>/update/', ReviewUpdateView.as_view(), name='update-review'),
    path('reviews/<int:pk>/delete/', ReviewDeleteView.as_view(), name='delete-review'),
    path('reviews/<int:pk>/', views.review, name='movie-review'),
    path('search', views.search, name='search'),
    path('movie/<int:movie_id>/toggle_watchlist/', views.toggle_watchlist, name='toggle_watchlist'),
    path('filters/', views.filters, name='filters'),
    path('actor/<int:pk>/', actor_detail, name='actor-detail'),
    # path('actors/', actor_list, name='actor-list'),
]