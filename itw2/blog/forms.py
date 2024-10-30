from django import forms

class GenreForm(forms.Form):
    GENRES = [
        ('all', 'ALL'),
        ('action', 'Action'),
        ('drama', 'Drama'),
        ('comedy', 'Comedy'),
        ('horror', 'Horror'),
        ('sci-fi', 'Sci-Fi'),
        ('adventure', 'Adventure'),
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