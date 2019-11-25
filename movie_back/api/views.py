from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Genre, Movie, Rating, Actor
from .serializers import GenreSerializer, MovieDetailSerializer, MovieSerializer, RatingSerializer
import requests
from pprint import pprint
from datetime import datetime, timedelta
from decouple import config
import csv
import json
import urllib.request
from django.shortcuts import render
import time
import re
import bs4

# Create your views here.

def movies(request):
    pass

def movies_genre(request):
    pass

def movie_detail(request, movie_id):
    pass

def ratings(request, user_id):
    pass



def movies_update(request):
    pass

def remove_tag(content):
   cleanr =re.compile('<.*?>')
   cleantext = re.sub(cleanr, '', content)
   return cleantext

def search(request):
    # with open('DB.json', encoding='utf-8') as json_file:
    #     json_data = json.load(json_file)
    #     for key in json_data.keys():
            
    #         for genre in json_data[key]["genreType"]:
    #             genre = genre.strip()
    #             all_genre = Genre.objects.all()
    #             if all_genre.filter(genre=genre).exists():
    #                 continue
    #             temp_genre = Genre(genre=genre)
    #             temp_genre.save()
    #         for actor in json_data[key]["actor"]:
    #             actor.strip()
    #             all_actor = Actor.objects.all()              
    #             if all_actor.filter(actor=actor).exists():
    #                 continue
    #             temp_actor = Actor(actor=actor)
    #             temp_actor.save()
    
    # movie_field = ['movieCd', 'movieNm', 'openDt']

    # key = config('API_KEY')
    # weekGb = '0'
    # week_base_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json'

    # for week in list(range(25))[::-1]:
    #     targetDt = datetime(2019, 11, 20) - timedelta(weeks=week)
    #     targetDt = targetDt.strftime('%Y%m%d')
    #     api_url = f'{week_base_url}?key={key}&targetDt={targetDt}&weekGb={weekGb}'
    #     response = requests.get(api_url)
    #     week_data = response.json()
    #     for i in range(10):
    #         movie_dict = {field : week_data['boxOfficeResult']['weeklyBoxOfficeList'][i][field] for field in movie_field}
    #         if Movie.filter(movieCd=movie_dict['movieCd']).exists():
    #             continue

    #         movie_detail_field = ['movieNmEn', 'audits', 'genres', 'directors']
    #         base_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json'
    #         number = movie_dict['movieCd']
    #         api_url = f'{base_url}?key={key}&movieCd={number}'
    #         response = requests.get(api_url)
    #         all_data = response.json()

    #         for field in movie_detail_field:
    #             value = all_data['movieInfoResult']['movieInfo'][field]
    #             if field == 'audits':
    #                 value = [grade['watchGradeNm'] for grade in value]
    #                 if len(value) >= 1:
    #                     value = value[0]
    #                 else:
    #                     value = ', '.join(value)
    #             elif field == 'genres':
    #                 value = [genre['genreNm'] for genre in value]
    #                 value = ', '.join(value)
    #             elif field == 'directors':
    #                 value = [director['peopleNm'] for director in value]
    #                 value = ', '.join(value)
                
    #             movie_dict[field] = value
    #         time.sleep(0.1)

    #         # 유튜브 링크
    #         name = movie_dict['movieNm']
    #         bases_url = 'https://www.youtube.com/results?search_query='
    #         youtube_base_URL = f'{bases_url}{name}'
    #         response = requests.get(youtube_base_URL)
    #         # 파싱을 하기 위해 텍스트화 시켜 html에 담는다.
    #         html = response.text
    #         #bs4를 활용하여 파싱한 결과 값
    #         soup = bs4.BeautifulSoup(html, 'html.parser')
    #         paragraph_data = soup.find_all('a', class_='yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link')
    #         line = str(paragraph_data[0])
    #         hosts = re.findall('href="/watch\?v=(.*?)"\s', line)
    #         temp = 'https://www.youtube.com/embed/'
    #         youtube_url = temp  + hosts[0]

    #         # 네이버 크롤링
    #         BASE_URL = 'https://openapi.naver.com/v1/search/movie.json'
    #         HEADERS = {
    #             'X-Naver-Client-id' : config('NAVER_API_ID'),
    #             'X-Naver-Client-Secret' : config('NAVER_API_SECRET'),
    #         }
    #         query = movie_dict['movieNm']
    #         API_URL = f'{BASE_URL}?query={query}'
    #         response = requests.get(API_URL, headers=HEADERS).json()


    #         # route에 response 딕셔너리의 item 리스트로 접근한다.
    #         route = response['items']
    #         # for문을 활용하여 item 리스트에 있는 딕셔너리에 하나씩 접근한다.
    #         for item in route :
    #             # 만약 route리스트의 원소가 하나만 있다면 그 item을 info에 대입한다.
    #             if len(route) == 1 :
    #                 info = item
    #             # 그렇지 않다면 첫번째로 item 딕셔너리의 title과 한글 영화제목을 비교한다.
    #             # 맞다면 for문을 빠져나온다.
    #             else :  
    #                 if  remove_tag(item['title']) == query :
    #                     info = item
    #                     break
    #                 # 한글 영화제목이 일치하지 않으면 영어 제목을 비교한다.
    #                 # 대문자와 소문자의 혼용으로 일치하지 않을 수 있기 때문에 lower 함수를
    #                 # 사용하여 소문자로 비교한다.
    #             if '|' in movie_dict['actor']:     
    #                 info['actor'] = info['actor'].split('|')
    #                 info['actor'].pop()
    #             if ',' in movie_dict['genres']:
    #                 movie_dict['genres'] = movie_dict['genres'].split(',')
    #             else:
    #                 movie_dict['genres'] = [movie_dict['genres']]
    #             # 추출해온 info에서 알맞는 정보를 입력한다.
    #             story_URL = info['link']
    #             response = requests.get(story_URL)
    #             # 파싱을 하기 위해 텍스트화 시켜 html에 담는다.
    #             html = response.text
    #             #bs4를 활용하여 파싱한 결과 값
    #             soup = bs4.BeautifulSoup(html, 'html.parser')
    #             description = soup.find('p', class_='con_tx').get_text()
    #             temp = []
    #             for i in range(len(movie_dict['genres'])):
    #                 if Genre.filter(genretype=movie_dict['genres'][i]).exists():
    #                     temp_genre = Genre.objects.get(genretype=movie_dict['genres'][i])
    #                     temp.append(temp_genre.pk)

    #             movie.save()

    # #             data = {
    # #                     'movieCd' : movie_dict['movieCd'],    
    # #                     'title' : remove_tag(info['title']),
    # #                     'title_en' : movie_dict['movieNmEn'],
    # #                     'summary' : description,
    # #                     'director' : movie_dict['directors'],
    # #                     'poster_url' : info['image'],
    # #                     'trailer_url' : youtube_url,
    # #                     'opendt' : movie_dict['openDt'],
    # #                     'naver_score' : info['userRating'],
    # #                     'grade' : movie_dict['audits'],
    # #                     'genreType' : movie_dict['genres'],
    # #                     'actor' : info['actor'],
    # #                     'link' : info['link'],                                  
    # #                     }
    # #             movie_data.update({movie_dict['movieCd'] : data})
    # # pprint(movie_data)
    movie_data = {}
    with open('DB.json', encoding='utf-8') as json_file:
        json_data = json.load(json_file)
        for key in json_data.keys():
            
            for genre in json_data[key]["genreType"]:
                genre = genre.strip()
                all_genre = Genre.objects.all()
                if all_genre.filter(genre=genre).exists():
                    continue
                temp_genre = Genre(genre=genre)
                temp_genre.save()
            for actor in json_data[key]["actor"]:
                all_actor = Actor.objects.all()              
                if all_actor.filter(actor=actor).exists():
                    continue
                temp_actor = Actor(actor=actor)
                temp_actor.save()


            movie = Movie.objects.all()
            movieCd = json_data[key]['movieCd']
            if movie.filter(movieCd=movieCd).exists():
                continue
            movie = Movie(movieCd=json_data[key]['movieCd'], title=json_data[key]['title'], title_en=json_data[key]['title_en'],
            summary=json_data[key]['summary'], director=json_data[key]['director'], poster_url=json_data[key]['poster_url'],
            trailer_url=json_data[key]['trailer_url'], opendt=json_data[key]['opendt'], naver_score=json_data[key]['naver_score'], 
            grade=json_data[key]['grade'])
            movie.save()

    return render(request, 'api/search.html', movie_data)

