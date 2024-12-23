from django import forms
from .models import Review


class GenreForm(forms.Form):
    GENRES = [
        ('all', 'ALL'),
        ('action', 'Action'),
        ('drama', 'Drama'),
        ('comedy', 'Comedy'),
        ('horror', 'Horror'),
        ('sci-fi', 'Sci-Fi'),
        ('adventure', 'Adventure'),
        ('biography', 'Biography'),
    ]
    genre = forms.ChoiceField(choices=GENRES, label="Select Genre")


class LanguageForm(forms.Form):
    LANGUAGES = [
        ('all', 'All'),
        ('english', 'English'),
        ('hindi', 'Hindi'),
        ('tamil', 'Tamil'),
        ('telugu', 'Telugu'),
    ]
    language = forms.ChoiceField(choices=LANGUAGES, label="Select Language")


class RatingForm(forms.Form):
    RATINGS = [
        ('all', 'All'),
        ('9', 'Rating above 9'),
        ('8', 'Rating above 8'),
        ('7', 'Rating above 7'),
    ]
    rating = forms.ChoiceField(choices=RATINGS, label="Select Rating")

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['movie', 'content', 'userRating']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['movie'].disabled = True 