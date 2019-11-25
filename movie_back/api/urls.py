from django.urls import path, include
from . import views


app_name = 'api'

urlpatterns = [
    path('movies/', views.movies),
    path('movies/genre/', views.movies_genre),
    path('movies/<int:movie_id>/', views.movie_detail),
    path('ratings/<int:user_id>/', views.ratings),
    path('movies_update/', views.movies_update),
    path('movies/search/', views.search, name='api_search'),
]