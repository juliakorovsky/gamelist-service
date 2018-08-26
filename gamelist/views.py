from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from gamelist.forms import SignUpForm
from gamelist.models import Game, Profile, List


# Create your views here.

def homepage(request):
    template_name = 'start.html'
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request, template_name)

def registration(request):
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            return redirect('/')
        else:
            print(signup_form.errors)
    else:
        signup_form = SignUpForm()
    return render(request, 'registration.html', {'signup_form': signup_form})

def central_page(request):
    template_name='loggedin.html'
    profile = request.user.profile
    games = profile.games_added.all()
    wanna_play = List.objects.filter(user_profile=profile, added_to='WANNA_PLAY')
    return render(request, template_name, {'games': games, 'wanna_play': wanna_play})


