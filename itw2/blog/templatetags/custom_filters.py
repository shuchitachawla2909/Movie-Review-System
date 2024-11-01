from django import template

register = template.Library()


@register.filter
def is_in_watchlist(user, movie):
    return user.watchlist.filter(movie=movie).exists()

@register.filter
def is_in_favourites(user, movie):
    return user.favourites.filter(movie=movie).exists()




