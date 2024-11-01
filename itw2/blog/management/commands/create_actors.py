from django.core.management.base import BaseCommand
from blog.models import Movie, Actor  # Replace 'your_app' with your actual app name

class Command(BaseCommand):
    help = 'Create actors from the movie cast and associate them with movies'

    def handle(self, *args, **kwargs):
        movies = Movie.objects.all()  # Get all movies

        for movie in movies:
            # Split the cast string into individual actor names
            cast_names = movie.cast.split(', ')
            
            for name in cast_names:
                # Get or create the actor, leaving biography and birthdate blank
                actor, created = Actor.objects.get_or_create(name=name)
                
                # Associate the actor with the movie
                actor.movies.add(movie)  # Add the movie to the actor's movie set
            
            # Optionally, save the movie instance to persist the associations
            movie.save()  

        self.stdout.write(self.style.SUCCESS('Successfully created actors and associated them with movies.'))
