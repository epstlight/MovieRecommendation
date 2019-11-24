from django.db import models
from django.conf import settings
# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=150)
    title_en = models.CharField(max_length=150)
    summary = models.TextField()
    director = models.CharField(max_length=50)
    poster_url = models.TextField()
    trailer_url = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    naver_score = models.IntegerField()
    avr_score = models.IntegerField(default=0)
    liked_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_movies') 

class Genre(models.Model):
    genreType = models.CharField(max_length=150)
    movies = models.ManyToManyField(Movie, related_name='genres')

class Rating(models.Model):
    comment = models.TextField()
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='users')