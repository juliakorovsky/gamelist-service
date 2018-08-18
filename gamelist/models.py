from django.db import models

# Create your models here.

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

    def __str__(self):
        return self.title
