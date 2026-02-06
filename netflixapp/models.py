from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import uuid

AGE_CHOICES = (
    ('All', 'All'),
    ('Kids', 'Kids'),
)

class CustomUser(AbstractUser):
    pass


class Profile(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profiles'
    )
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(default=18)
    age_limit = models.CharField(max_length=10, choices=AGE_CHOICES)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)

    @property
    def is_kid(self):
        return self.age_limit == 'Kids'

    def __str__(self):
        return self.name


class Movie(models.Model):
    tmdb_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=255)
    overview = models.TextField(blank=True)
    poster_path = models.CharField(max_length=255, blank=True)
    release_date = models.DateField(null=True, blank=True)
    rating = models.FloatField(default=0)
    trailer_key = models.CharField(max_length=50, blank=True, null=True)
    age_limit = models.PositiveIntegerField(default=18)

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=1000)
    file = models.FileField(upload_to='movies')

    def __str__(self):
        return self.title

