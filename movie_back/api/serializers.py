from rest_framework import serializers
from .models import Movie, Genre, Rating, Director, Actor

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
    class Meta:
        model = Genre
        fields = ['id', 'name' ]


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'name' ]

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'name' ]


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    directors = DirectorSerializer(many=True)
    actors = ActorSerializer(many=True)
    class Meta:
        model = Movie
        fields = ['id', 'movieCd', 'title', 'title_en', 'summary', 'naver_score', 'avr_score', 'poster_url', 'trailer_url', 'opendt', 'liked_users', 'genres', 'directors', 'actors']
