from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username

# class Game(model.Models):
#     game_id = models.IntField(max_)
#     name = models.CharField(max_length=255)
#     summary = models.TextField(max_length=1000)
#     release_date = models.CharField(max_length=255)
#     genre = models.CharField(max_length=255)
#     critic_score = 
#     platform = models.CharField(max_length=255)
#     studio = models.CharField(max_length=255)