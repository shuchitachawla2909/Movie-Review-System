from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('watchlist/', views.Watchlist, name='watchlist')
]