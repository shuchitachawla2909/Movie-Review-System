from django.db import models
from django.contrib.auth.models import User
from blog.models import Movie
from PIL import Image

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    def save(self):
        super().save()

        img=Image.open(self.image.path)

        if img.height>300 or img.width >300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)



class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watchlist")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'movie')  
    def __str__(self):
        return f"{self.user.username}'s watchlist - {self.movie.title}"

class Favourites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favourites")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'movie')  
    def __str__(self):
        return f"{self.user.username}'s  - {self.movie.title}"
    

    