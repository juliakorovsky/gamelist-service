from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    games_added = models.ManyToManyField('Game', through='List', blank=True, related_name='user_games')

    def __str__(self):
        return self.user.username


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Game(models.Model):
    title = models.CharField(max_length=100, primary_key=True)
    platforms = models.ManyToManyField('Platform', blank=True)
    exclusive = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class List(models.Model):
    list_choices = (
        ('WANNA_PLAY', 'Want to play'),
        ('PLAYING', 'Playing'),
        ('COMPLETED', 'Completed'),
        ('DROPPED', 'Dropped')
    )
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    games_user_added = models.ForeignKey(Game, on_delete=models.CASCADE)
    added_to = models.CharField(max_length=20, choices=list_choices, blank=False, default='WANNA_PLAY')

    def __str__(self):
        return self.user_profile.user.username + ' added ' + self.games_user_added.title + ' to ' + self.added_to



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
