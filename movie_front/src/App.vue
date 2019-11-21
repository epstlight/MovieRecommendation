<template>
  <div id="app">
    <div id="nav">
      <!-- 조건부 렌더링 -->
      <div v-if="isLoggedIn">
        <router-link to="/">Home</router-link> |
        <!-- a tag 는 새로고침을 해준다. -->
        <!-- prevent 를 사용하는 이유는 href 로 redirect 를 방지하기 위함 -->
        <!-- 기능적으로는 login 으로 바로 가도 되지만 명시적으로 하기 위해 -->
        <a @click.prevent="logout" href="/logout">Logout</a>
      </div>
      <div v-else>
        <router-link to="/login">Login</router-link>
      </div>
    </div>
    <!-- click 했을 때 home / about 이 된다. -->
    <div class="container col-6">
      <router-view/>
    </div>
  </div>
</template>

<script>
import router from '@/router'
export default {
  name: 'App',
  // data() {
  //   return {
  //     isLoggedIn: this.$session.has('jwt')
  //   }
  // },
  computed: {
    isLoggedIn() {
      return this.$store.getters.isLoggedIn
    }
  },
  // 최상위  App 컴퍼넌트가 렌더링 되면 실행되는 함수 
  mounted() {
    // 새로고침해도 로그인 유지됨 
    if(this.$session.has('jwt')) {
      const token = this.$session.get('jwt')
      this.$store.dispatch('login', token)
    }
  },
  methods: {
    logout() {
      this.$session.destroy()
      // 우리가 관리하는 상태값에서도 토큰을 없애줘야함 
      this.$store.dispatch('logout')
      router.push('/login')
    }
  },
  // data 에 변화가 일어나는 시점에 실행하는 함수 
  // updated() {
  //   this.isLoggedIn = this.$session.has('jwt')
  // }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  padding: 30px;
}
#nav a {
  font-weight: bold;
  color: #2c3e50;
}
#nav a.router-link-exact-active {
  color: #42b983;
}
</style>