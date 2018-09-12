from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, Select
from .models import Game, List


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1')

class AddGameForm(ModelForm):

    class Meta:
        model = Game
        fields = ['title', 'platforms']


class AddListForm(ModelForm):

    class Meta:
        model = List
        fields = ['added_to']




