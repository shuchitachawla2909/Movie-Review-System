from django.urls import path
from .views import MovieDetailView
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie-detail')
]