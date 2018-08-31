from django.contrib import admin
from .models import Game, Platform, Profile, List

# Register your models here.

admin.site.register(Game)
admin.site.register(Platform)
admin.site.register(Profile)
admin.site.register(List)
