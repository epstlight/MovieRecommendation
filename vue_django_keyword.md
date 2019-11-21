JWT => 유효기간이 짧다. 길어봤자 2주. 보통 몇 시간 단위로 처리함

정보를 비교적 안전하게 JSON 객체로 전송하기 위한 간결하고 독립적인 방법. (컴퓨터에 token이 남기 때문에 안전하기 않을수도 있다.)



header(어떻게 형성되어 있는지).payload(data).signature => 라이브러리 존재

xxxx.yyyy.zzzz  형태로 생김



vue.js, django

가상환경 만들기

python -m venv venv

source venv/Scripts/activate  => venv 활성화

deactivate => 비활성

장고시작

django-admin startproject todo-back .

django 로 backend 구현



vue, node js, npm version 필요

npm i -g @vue/cli => 글로벌 옵션으로 설정



vue create todo-front

vue 로 frontend 구현

rm -rf .git

rm .gitignore





view router => url 별로 어떤 동작할지 정해주는 

설치 방법

```bash
vue ui
```

플러그인 추가 => vue/cli-plugin-router 설치

use history mode 체크 ==> single page application 의 단점을 보완하기 위해





npm i bootstrap bootstrap-vue



로그인할때 axios 반드시 필요

npm i axios



CORS

=> 허락한 곳에서만 접근 가능하도록 하기 위해서 사용하는 기능, 쟝고에서 vue를 화이트리스팅 처리





##### todo-back

```
python manage.py startapp todos
```

```
pip install djangorestframework
```

```
pip install djangorestframework-jwt
```

```
pip install django-cors-headers
```

settings.py

```python
import datetime
```

```python
INSTALLED_APPS = [
    # local apps
    'todos',

    # Third party app
    'rest_framework',
    'corsheaders',
]
```



google에 django rest framework jwt 검색 => github 접속

INSTALLED_APPS 와 MIDDLEWARE 사이에 복붙

```python
# http://jpadilla.github.io/django-rest-framework-jwt/#usage
REST_FRAMEWORK = {
    # 로그인 여부를 확인해주는 클래스
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),

    # 인증 여부를 확인하는 클래스
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

# https://jpadilla.github.io/django-rest-framework-jwt/#additional-settings
JWT_AUTH = {
    # SECRET_KEY 위쪽에 있음
    # Token 을 서명할 시크릿 키를 등록 (절대 외부 노출 금지). default 가 settings.SECRET_KEY
    'JWT_SECRET_KEY': SECRET_KEY,
    'JWT_ALGORITHM': 'HS256', # default 값
    'JWT_ALLOW_REFRESH': True,
    # 유효기간, default 유효기간은 5분, 지금은 1주일간 유효한 토큰으로 설정
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7), 
    # 28일 마다 토큰이 갱신 (유효기간 연장시)
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=28),

}
```

로그인을 하면 톡큰 2개 access token, refresh token

access token => data에 접근할 수 있는 token

refresh token =>  Access token의 수명이 다했을 때 새로운 access token을 발급 받는 방법이 refresh token 이다.

`````

`````

미들웨어 추가

```python
# https://github.com/adamchainz/django-cors-headers/#Setup
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
]

# https://github.com/adamchainz/django-cors-headers/#CORS_ORIGIN_REGEX_WHITELIST
# CORS_ORIGIN_WHITELIST = [
#     "http://localhost:8080",
# ]
# 전 세계 모든 곳에서 접근 가능
CORS_ORIGIN_ALLOW_ALL = True
```



urls.py

```python
from rest_framework.views import obtain_jwt_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_jwt_token)
]
```



models.py

```python
from django.conf import settings
from django.contrib.auth.models import AbstractUser



# 유저는 커스텀 유저(명시적)를 사용 
# (default 유저를 사용하더라도 장고에서는 *강력히* 커스텀 유저를 사용하라고 권장)
class User(AbstractUser):
    pass


class Todo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MDOEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
```



setting.py

```python
# 끝부분
# 앞으로 todos 에 정의한 User 모델을 기본으로
AUTH_USER_MODEL = 'todos.User'
```



settings.json

```python
{
    "git.ignoreLimitWarning": true,
    "python.pythonPath": "todo-back\\venv\\Scripts\\python.exe",
}
# python 인식 못하는 문제 해결
```



##### todo-front

LoginForm.vue

```js
// methods:
// 
login() {
      if (this.checkForm()) {
        this.loading = true
        // http://127.0.0.1:8000
        const SERVER_IP = process.env.VUE_APP_SERVER_IP

        axios.post(SERVER_IP + '/api-token-auth/', this.credentials)
          .then(response => {
            console.log(response)
            this.loading = false
          })
          .catch(error => {
            console.error(error)
            this.loading = false
          })  
      }
    },
```

token 은 브라우저에 저장해야 한다.(쿠키, 로컬스토리지, 세션 스토리지,) (로컬 스토리지는 브라우저에 저장하면 계속 유지, 세션 스토리지는 브라우저가 켜져있는 동안 유지)

```bash
npm i vue-session  // session storage
```

```js
// main.js
// https://www.npmjs.com/package/vue-session
import VueSession from 'vue-session'

Vue.use(VueSession)


// LoginForm.vue
import router from '@/router'
// methods:login()
axios.post(SERVER_IP + '/api-token-auth/', this.credentials)
          .then(response => {

            // 세션을 초기화, 사용하겠다
            this.$session.start()

            // 응답결과를 세션에 저장하겠다
            this.$session.set('jwt', response.data.token)
            this.loading = false
    
    		// vue router 를 통해 특정 페이지로 이동
            router.push('/')
          })
```



Home.vue

```js
import router from '@/router'
export default {
  name: 'Home',

  methods: {
    // 사용자 로그인 유무를 확인하여 로그인되어있지 않을 시 로그인 페이지로 보내겠다.
    checkLoggedIn() {
      // 1. 세션을 시작해서
      this.$session.start()

      // 2. 'jwt' 가 있는지 확인하겠다.
      if (!this.$session.has('jwt')) {
        // 로그인 페이지로 보내겠다.
        router.push('/login')
      }
    }
  },

  // Vue 가 화면에 그려지면 실행하는 함수
  mounted() {
    this.checkLoggedIn()
  }
}
```



##### Logout 구현

App.vue

```html
<!-- a-tag 는 새로고침을 해준다. 따라서 push(login)이 먹었다가 다시 logout으로 가게 된다. -->
<!-- prevent 를 사용하는 이유는 href 로 redirect 를 방지하기 위함 -->
<a @click.prevent="logout" herf="/logout">Logout</a>

<script>
import router from  '@/router'

export default {
  name: 'App',
  methods: {
      logout() {
          this.$session.destroy
          router.push('/login')
      }
  }
}
</script>
```

로그인 때만 logout, home 버튼이 보이게

```html
<div v-if="isLoggedIn">
    <router-link to="/">Home</router-link> |
    <!-- a-tag 는 새로고침을 해준다. 따라서 push(login)이 먹었다가 다시 logout으로 가게 된다. -->
    <!-- prevent 를 사용하는 이유는 href 로 redirect 를 방지하기 위함 -->
    <a @click.prevent="logout" herf="/logout">Logout</a>
</div>


<div v-else>
    <router-link to="/login">Login</router-link>
</div>

<script>
  data() {
    return {
      isLoggedIn: this.$session.has('jwt')
    }
  },
  // data 에 변화가 일어나는 시점에 실행하는 함수
  updated() {
    this.isLoggedIn = this.$session.has('jwt')
  }
</script>
```



django 를 통해 api server 생성



이후 front 만들기

component 폴더에 TodoList.vue 생성

Home.vue

```
npm i jwt-decode
```

```html
<script>
import axios from 'axios'
import jwtDecode from 'jwt-decode'  // JWT 의 payload 값을 해석해서 보여주는 library

import TodoList from '../components/TodoList.vue'
=> 추가
    
export default {
  components: {
    TodoList,
  },
  methods: {
      getTodo() {
      this.$session.start()
      const token = this.$session.get('jwt')
      const SERVER_IP = process.env.VUE_APP_SERVER_IP
	
      const options = {
        headers: {
          Authorization: 'JWT ' + token
        }
      }
      
      axios.get(SERVER_IP + '/api/v1/users/user_id/')
        .then(response => {
          console.log(response)
        })
        .catch(error => {
          console.error(error)
        })
    }
  }
}
</script>
```

Todolist.vue

```html

```



Vuex

참고 사이트

```
https://vuex.vuejs.org/kr/
```

state => data 와 같은 개념

mutate => state만 바꾸는 함수

action => method 와 같은 개념, 행위



설치

```bash
vue ui
```

'플러그인 추가'에서 'vuex' 검색 후 설치



```js
// App.vue  
// 최상위 App 컴포넌트가 렌더링 되면 실행하는 함수
  mounted() {
    if(this.$session.has('jwt')) {
      const token = this.$session.get('jwt')
      this.$store.dispatch('login', token)
    }
  }, 
  // 로그인 되어있으면 token 유지되도록 하는 함수
```



updated 를 자주 사용하는 것은 좋지 않다.

따라서 아래와 같이 바꿔준다.

```js
// App.vue
  computed: {
    isLoggedIn() {
      return this.$store.getters.isLoggedIn
    }
  },
  methods: {
      logout() {
          this.$session.destroy()
          this.$store.dispatch('login')
          router.push('/login')
      }
  },
```

```js
// TodoList.vue
computed: {
    options() {
      return this.$store.getters.options
    }
  },
methods: {
    deleteTodo(todo) {
      // option을 만들어 주는 것이 아닌 vuex store 에 있는 options 에 접근 해서 가져온다.
      // session 에 계속 접근하는 것은 프로그램에 부담이 간다.
      const SERVER_IP = process.env.VUE_APP_SERVER_IP

      axios.delete(`${SERVER_IP}/api/v1/todos/${todo.id}/`, this.options)
    }
}
```

```js
// Home.vue
// 로그인 정보는 많은 정보를 불러와야 하기 때문에 한번에 불러오는 mapGetters 를 사용한다.

import { mapGetters } from 'vuex'  // import vuex from 'vuex; vuex.mapGetters
computed: {
    // ...은 spread operator const z = {...x, ...y, e:5} 방식으로 사용 가능함(x, y 내용을 전부 뿌려줌)
    ...mapGetters([
      'isLoggedIn',
      'options',
      'userId'
    ])
  },
```

