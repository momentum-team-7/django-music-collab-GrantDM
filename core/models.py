from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class Artist(models.Model):
    name = models.CharField(max_length=280)
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=280)
    release_date = models.IntegerField(blank=True, null=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, blank=True, null=True, related_name="albums")

    def __str__(self):
        return self.title
