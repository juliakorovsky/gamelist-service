from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    games_wanna_play = []
    games_playing = []
    games_completed = []
    games_dropped = []

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class Platform(models.Model):
    family_choices = (
    ('NOT_SPECIFIED', 'Not specified'),
    ('NIN', 'Nintendo'),
    ('PS', 'Playstation'),
    ('SEGA', 'Sega')
    )

    title = models.CharField(max_length=100, primary_key=True)
    games = models.ManyToManyField('Game', blank=True)
    platform_family = models.CharField(max_length=20, choices=family_choices, default='NOT_SPECIFIED')

    def __str__(self):
        return self.title


class Game(models.Model):
    title = models.CharField(max_length=100, primary_key=True)
    platforms = models.ManyToManyField('Platform', blank=False)
    exclusive = models.BooleanField(default=False)

    def __str__(self):
        return self.title
