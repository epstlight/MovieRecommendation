from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Genre, Movie, Rating
from .serializers import GenreSerializer, MovieDetailSerializer, MovieSerializer, RatingSerializer

import requests, csv
from pprint import pprint
from decouple import config
from datetime import datetime, timedelta
# Create your views here.

def movies(request):
    pass

def movies_genre(request):
    pass

def movie_detail(request, movie_id):
    pass

def ratings(request, user_id):
    pass


@api_view(['POST'])
def movies_update(request):
    pass 


KEY = config('MOVIE_API_KEY')
url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={KEY}&weekGb=0'
CLIENT_ID = config('NAVER_API_ID')
CLIENT_SECRET = config('NAVER_API_SECRET')
BASE_URL = f'https://openapi.naver.com/v1/search/movie.json'
URL_HEADER = {
    'X-Naver-Client-Id': CLIENT_ID,
    'X-Naver-Client-Secret': CLIENT_SECRET
}


def movies_update(request):
    targetDt = (datetime.now().strftime('%Y%m%d') - timedelta(weeks=i)).strftime('%Y%m%d')
    result = requests.get(f'{url}&targetDt={targetDt}').json()
    for movie_info in result.get('boxOfficeResult').get('weeklyBoxOfficeList'): 
        movie_code = movie_info.get('movieCd')
        movie_name = movie_info.get('movieNm')ww
        movie_audinum = f'({targetDt}) ' + movie_info.get('audiAcc')  

        if movie_code not in movie_list:  # 중복을 제거하기 위한 if문
            movie_list.append(movie_code)
            movie_info_row = {
                '영화 대표코드': movie_code, 
                '영화명': movie_name, 
                '(해당일) 누적관객수': movie_audinum,
            }
            writer.writerow(movie_info_row)


