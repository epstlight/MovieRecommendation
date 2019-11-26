from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Genre, Movie, Rating, Actor
from .serializers import GenreSerializer, MovieDetailSerializer, MovieSerializer, RatingSerializer
from rest_framework.permissions import AllowAny 


import json
import requests, csv
from pprint import pprint
from decouple import config
from datetime import datetime, timedelta
# Create your views here.

@api_view(['GET'])
@permission_classes([AllowAny])
def movies(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

def movies_genre(request):
    pass

def movie_detail(request, movie_id):
    pass

def ratings(request, user_id):
    pass


# def movies_update(request):
#     movie_data = {}
#     with open('db.json', encoding='utf-8') as json_file:
#         json_data = json.load(json_file)
#         for key in json_data.keys():
            
#             for genre in json_data[key]["genreType"]:
#                 genre = genre.strip()
#                 all_genre = Genre.objects.all()
#                 if all_genre.filter(genreType=genre).exists():
#                     continue
#                 temp_genre = Genre(genreType=genre)
#                 temp_genre.save()
#             for actor in json_data[key]["actor"]:
#                 all_actor = Actor.objects.all()              
#                 if all_actor.filter(actor=actor).exists():
#                     continue
#                 temp_actor = Actor(actor=actor)
#                 temp_actor.save()


#             movie = Movie.objects.all()
#             movieCd = json_data[key]['movieCd']
#             if movie.filter(movieCd=movieCd).exists():
#                 continue
#             movie = Movie(movieCd=json_data[key]['movieCd'], title=json_data[key]['title'], title_en=json_data[key]['title_en'],
#             summary=json_data[key]['summary'], director=json_data[key]['director'], poster_url=json_data[key]['poster_url'],
#             trailer_url=json_data[key]['trailer_url'], opendt=json_data[key]['opendt'], naver_score=json_data[key]['naver_score'], 
#             grade=json_data[key]['grade'])
#             movie.save()

#     return redirect('/')


