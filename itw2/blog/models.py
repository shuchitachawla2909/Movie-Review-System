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

class Actor(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(blank=True)
    birthdate = models.DateField(null=True, blank=True)
    movies = models.ManyToManyField(Movie, related_name='actors')
    profile_picture = models.ImageField(default='default.jpg', upload_to='actor_pics/')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('actor-detail', kwargs={'pk': self.pk})
    
    def save(self, *args, **kwargs):
        # Call the original save() method
        super().save(*args, **kwargs)

        # Update actors
        self.update_actors()

    def update_actors(self):
        # Access the cast string from the related Movie instance
        if self.movies.exists():  # Ensure there are associated movies
            for movie in self.movies.all():
                cast_names = movie.cast.split(', ')  # Accessing the cast from Movie

                for name in cast_names:
                    # Get or create the actor
                    actor, created = Actor.objects.get_or_create(name=name)

                    # Associate the actor with the movie
                    actor.movies.add(movie)  # Add this movie to the actor's movie set

    

