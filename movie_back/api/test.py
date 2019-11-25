import requests
from pprint import pprint
from datetime import datetime, timedelta
from decouple import config
import csv
import json
import urllib.request



movie_data = {}
movie_field = ['movieCd', 'movieNm', 'openDt', 'audiAcc']

key = config('API_KEY')
weekGb = '0'
base_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json'

for week in list(range(51))[::-1]:
    targetDt = datetime(2019, 11, 25) - timedelta(weeks=week)
    targetDt = targetDt.strftime('%Y%m%d')
    api_url = f'{base_url}?key={key}&targetDt={targetDt}&weekGb={weekGb}'
    response = requests.get(api_url)
    week_data = response.json()
    for i in range(10):
        movie_dict = {field : week_data['boxOfficeResult']['weeklyBoxOfficeList'][i][field] for field in movie_field}
        movie_data.update({movie_dict['movieCd'] : movie_dict})
        

# with open('boxoffice.csv', 'w', newline='', encoding='utf-8') as f:
#     fieldnames = ('movieCd', 'movieNm', 'openDt', 'audiAcc')
#     writer = csv.DictWriter(f, fieldnames=fieldnames)
#     writer.writeheader()

#     for movie in movie_data.values():
#         writer.writerow(movie)
movie_data = []
movie_field = ['movieCd', 'movieNm', 'movieNmEn', 'movieNmOg', 'audits', 'openDt',
'showTm', 'genres', 'directors', 'companys']





# with open('boxoffice.csv', 'r', newline='', encoding='utf-8') as f:
#     reader = csv.DictReader(f)
code_list = [row['movieCd'] for row in movie_data]


for code in code_list:
    api_url = f'{base_url}?key={key}&movieCd={code}'
    response = requests.get(api_url)
    all_data = response.json()
    movie_dict = {}
    for field in movie_field:
        value = all_data['movieInfoResult']['movieInfo'][field]
        if field == 'audits':
            value = [grade['watchGradeNm'] for grade in value]
            if len(value) >= 1:
                value = value[0]
            else:
                value = ', '.join(value)
        elif field == 'genres':
            value = [genre['genreNm'] for genre in value]
            value = ', '.join(value)
        elif field == 'directors':
            value = [director['peopleNm'] for director in value]
            value = ', '.join(value)
        elif field == 'companys':
            value = [company['companyNm'] for company in value if company['companyPartNm'] == '배급사']
            value = ', '.join(value)

        movie_dict.update({field: value})

    movie_data += [movie_dict]

    pprint(movie_dict)