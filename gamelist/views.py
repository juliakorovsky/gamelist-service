from django.shortcuts import render

# Create your views here.
def homepage(request):
    template_name = 'start.html'
    if request.user.is_authenticated():
        template_name = 'loggedin.html'
    return render(request, template_name)
