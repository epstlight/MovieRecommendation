from rest_framework import serializers
from .models import Movie, Genre, Rating

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'naver_score', 'avr_score', 'poster_url']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['comment', 'score', 'created_at', 'user', 'movie']


class MovieDetailSerializer(serializers.ModelSerializer):
    ratings = RatingSerializer(many=True)
    class Meta:
        model = Movie
        fields = ['director', 'summary', 'avr_score', 'trailer_url', 'ratings', 'liked_users']


class GenreSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True)
    class Meta:
        model = Genre
        fields = ['genreType', 'movies']