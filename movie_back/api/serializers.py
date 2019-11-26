from rest_framework import serializers
from .models import Movie, Genre, Rating

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'movieCd', 'title', 'title_en', 'summary', 'director', 'naver_score', 'avr_score', 'poster_url', 'trailer_url', 'opendt', 'liked_users', 'genres']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'comment', 'score', 'created_at', 'user', 'movie']


class MovieDetailSerializer(serializers.ModelSerializer):
    ratings = RatingSerializer(many=True)
    class Meta:
        model = Movie
        fields = ['id', 'director', 'summary', 'avr_score', 'trailer_url', 'ratings', 'liked_users']


class GenreSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True)
    class Meta:
        model = Genre
        fields = ['id', 'genreType', 'movies']