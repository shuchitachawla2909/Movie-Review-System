from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Movie(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    director = models.TextField()
    cast = models.TextField()
    genre = models.TextField()
    duration = models.IntegerField()
    year = models.IntegerField()
    language = models.CharField(max_length=100)
    awards = models.TextField()
    trailer = models.TextField()
    review = models.TextField()
    image = models.ImageField(default='dkposter.jpg', upload_to='movies')
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=5.0)

    def __str__(self):
        return self.title


class Review(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.CharField(max_length=250)
    content = models.TextField()
    userRating = models.DecimalField(max_digits=2, decimal_places=1, default=5.0)
    date_posted = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('user-reviews')