from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Movie(models.Model):

    title = models.CharField(max_length=100)
    popularity = models.FloatField()
    genres = models.ManyToManyField(Genre, related_name='genre_movies')
    release_date = models.DateField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    overview = models.TextField()
    poster_path = models.TextField()
    adult = models.BooleanField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    rank_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='user_rank', through='UserRank')

    def __Str__(self):
        return self.title

class UserRank(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rank = models.PositiveIntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(10)])


class Review(models.Model):
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rank = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])

