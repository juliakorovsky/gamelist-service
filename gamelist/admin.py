from django.contrib import admin
from gamelist.models import Game, Platform, Profile

# Register your models here.

admin.site.register(Game)
admin.site.register(Platform)
admin.site.register(Profile)
