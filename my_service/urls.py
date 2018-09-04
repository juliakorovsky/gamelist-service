"""my_service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url
from django.contrib.auth.views import LoginView
from gamelist import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='front_page'),
    path('register/', views.registration, name='register'),
    path('login/', LoginView.as_view(template_name='login_user.html'), name='login'),
    path('home/', views.central_page, name='home'),
    path('add/', views.game_add, name='add_game'),
    re_path(r'^(?P<profile_name>\w+)/$', views.profile, name='profile')
]
