from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('watchlist/', views.watchlist, name='watchlist'),
    path('watchlist/add/', views.addWatchlist, name='watchlist-add'),
    path('watchlist/update/', views.updateWatchlist, name='update-watchlist'),
    path('watchlist/delete/', views.deleteWatchlist, name='delete-watchlist'),
]