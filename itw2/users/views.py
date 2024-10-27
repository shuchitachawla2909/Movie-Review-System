from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

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
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')



def watchlist(request):
    return render(request, 'users/watchlist.html')


def addWatchlist(request):
    return render(request, 'users/watchlist.html')


def updateWatchlist(request):
    return render(request, 'users/watchlist.html')


def deleteWatchlist(request):
    return render(request, 'users/watchlist.html')