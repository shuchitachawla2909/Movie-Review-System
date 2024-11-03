from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Watchlist, Favourites

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been created. You can now Log In!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form, 'title': 'Register'})

from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    if request.method== 'POST':
        u_form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Profile has been Updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'title': 'Profile'
    }
    
    return render(request, 'users/profile.html', context)


@login_required
def Watchlist(request):
    watchlist_movies = request.user.watchlist.all()
    return render(request, 'users/watchlist.html', {'watchlist_movies': watchlist_movies})

@login_required
def Favourites(request):
    favourites_movies = request.user.favourites.all()
    return render(request, 'users/favourites.html', {'favourites_movies': favourites_movies})
