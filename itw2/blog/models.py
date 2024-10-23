from django.db import models

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
    image = models.ImageField(default='dkposter.jpg')
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=5.0)

    def __str__(self):
        return self.title

