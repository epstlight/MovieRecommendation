from django.db import models
from django.conf import settings
# Create your models here.
class Genre(models.Model):
    genre = models.CharField(max_length=150)

class Actor(models.Model):
    actor = models.CharField(max_length=100)

class Movie(models.Model):
    movieCd = models.IntegerField()
    title = models.CharField(max_length=150)
    title_en = models.CharField(max_length=150)
    summary = models.TextField()
    director = models.CharField(max_length=50)
    poster_url = models.TextField()
    trailer_url = models.TextField()
    opendt = models.DateTimeField(default="2019-11-25")
    naver_score = models.FloatField()
    grade = models.CharField(max_length=50)
    avr_score = models.IntegerField(default=0)
    liked_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_movies') 
    genres = models.ManyToManyField(Genre, related_name='genres_movies')
    actors = models.ManyToManyField(Actor, related_name='actors_movies')

class Rating(models.Model):
    comment = models.TextField()
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='users')