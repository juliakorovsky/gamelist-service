from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from gamelist.forms import UserForm


# Create your views here.
def homepage(request):
    template_name = 'start.html'
    if request.user.is_authenticated:
        template_name = 'loggedin.html'
        dictionary = {}
    else:
        if request.method == 'POST':
            signup_form = UserForm(request.POST)
            if signup_form.is_valid():
                user = signup_form.save()
                user.set_password(user.password)
                user.save()
                return redirect('/')
            else:
                print(signup_form.errors)
        else:
            signup_form = UserForm()
            dictionary = {'signup_form': signup_form}
            
    return render(request, template_name, dictionary)


