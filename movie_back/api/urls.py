
from django.urls import path, include
from . import views


app_name = 'api'

urlpatterns = [
    path('movies/', views.movies),
    path('movies/<int:movie_id>/', views.movie_detail),
    path('ratings/<int:user_id>/', views.ratings),
    path('genres/', views.genres),
    # path('movies_update/', views.movies_update),
]