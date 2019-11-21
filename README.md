# 1일차
# movie_back
```bash
$ python -m venv venv

$ source venv/Scripts/activate

$ python -m pip install --upgrade pip

$ pip install django

$ pip install djangorestframework

$ pip install djangorestframework-jwt

$ pip install django-cors-headers

$ django-admin startproject movierecommendation .

$ python manage.py startapp api


```

settings.py

```python
INSTALLED_APPS = [
    'api',
    # Third party app
    'rest_framework',
    'corsheaders',
    
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',

    
CORS_ORIGIN_ALLOW_ALL = True

AUTH_USER_MODEL = 'api.User'
    

```

urls.py

```python
from rest_framework.views import obtain_jwt_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_jwt_token)
]
```



.vscode/settings.json

```json
{
    "git.ignoreLimitWarning": true,
    "python.pythonPath": "movie_back\\venv\\Scripts\\python.exe",
    "python.linting.enabled": false
}
```
파이썬 개발환경 세팅 저장

```bash
$ pip3 freeze > requirements.txt  # 패키지 목록을 txt 파일로 만들기
$ pip3 install -r requirements.txt  # 한번에 패키지 설치
```



# movie_front

```bash
$ npm i -g @vue/cli

$ vue create movie-front

$vue ui
```

http://localhost:8000/plugins/add

vue ui에서 movie_front 연뒤

플러그인 추가 => @vue/cli-plugin-router 설치

use history mode 체크 ==> single page application 의 단점을 보완하기 위해

플러그인 추가 => @vue/cli-plugin-vuex 설치

```bash
$ npm i bootstrap bootstrap-vue

$ npm i axios

$ npm i vue-session

$ npm i jwt-decode

$ npm i #개발환경 불러오기
```



pakage.json

```json
"rules": {
      "no-console": "off"
    },
```

 