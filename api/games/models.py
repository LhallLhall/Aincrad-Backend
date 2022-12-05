from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    games = models.ManyToManyField('Game', through='GameUser', related_name='users')

    def __str__(self):
        return f"{self.username}"

class Game(models.Model):
    game_id = models.IntegerField()
    name = models.CharField(max_length=255)
    summary = models.TextField(max_length=1000)
    release_date = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    rating = models.IntegerField()
    platform = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    


class GameUser(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    hours_played = models.IntegerField()