from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .forms import SignUpForm, AddGameForm, AddListForm
from .models import Game, Profile, List, Platform


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
#here will be code for main page view, but for now, let it be
    return render(request, 'loggedin.html')

def profile(request, profile_name):
    site_user = User.objects.get(username=profile_name)
    profile = site_user.profile
    wanna_play = List.objects.filter(user_profile=profile, added_to='WANNA_PLAY')
    playing = List.objects.filter(user_profile=profile, added_to='PLAYING')
    return render(request, 'profile.html', {'wanna_play': wanna_play, 'playing': playing})
#might be rewrited with class-based view

def game_add(request):
    add_game_form = AddGameForm()
    list_form = AddListForm()
    return render(request, 'loggedin.html', {'add_game_form': add_game_form, 'list_form': list_form})







