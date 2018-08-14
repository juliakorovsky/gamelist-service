from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from gamelist.forms import UserForm


# Create your views here.
def homepage(request):
    template_name = 'start.html'
    if request.user.is_authenticated:
        template_name = 'loggedin.html'
    else:
        registered = False
        if request.method == 'POST':
            user_form = UserForm(request.POST)
            if user_form.is_valid():
                user = user_form.save()
                user.set_password(user.password)
                user.save()
                registered = True
                return redirect('')
            else:
                print(user_form.errors)
        else:
            user_form = UserForm()
            
    return render(request, template_name, {'user_form': user_form, 'registered' : homepage})


