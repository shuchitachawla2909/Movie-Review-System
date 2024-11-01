from django import template

register = template.Library()

print("Custom filters loaded")

@register.filter
def is_in_watchlist(user, movie):
    return user.watchlist.filter(movie=movie).exists()
