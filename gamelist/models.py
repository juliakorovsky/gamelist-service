from django.db import models

# Create your models here.

class Platform(models.Model):
    title = models.CharField(max_length=100, primary_key=True)
    games = models.ManyToManyField('Game', blank=True)

    def __str__(self):
        return self.title


class Game(models.Model):
    title = models.CharField(max_length=100, primary_key=True)
    platforms = models.ManyToManyField('Platform', blank=False)

    def __str__(self):
        return self.title
