<template>
  <div id="app">
    <div id="nav">
      <div v-if="isLoggedIn">
        <!-- prevent로 사용하는 이유는 리다이렉트를 방지하기 위해 -->
        <router-link to="/">Home</router-link> 
        <a class="float-right" @click.prevent="logout" href="logout/">Logout</a>
        <span class="float-right mx-1"> | </span>
        <router-link class="float-right" to="/userprofile" ><img src="@/images/user_1.png" alt="userprofile"></router-link> 
      </div>
      <div v-else>
        <router-link to="/">Home</router-link>
        <router-link class="float-right" to="/login" >Login</router-link>
        <span class="float-right mx-1"> | </span>
        <router-link class="float-right" to="/signup" >Signup</router-link> 
      </div>
    </div>
    <div class="container col-6">
      <router-view/>
    </div>
  </div>
</template>


<script>
import router from '@/router'
export default {
  name:'App',
  data(){
    return {
      // isLoggedIn: this.$session.has('jwt')
    } 
  },
  methods:{
    logout(){
      this.$session.destroy()
      this.$store.dispatch('logout')
      router.push('/')
    },
  },
  computed:{
    isLoggedIn(){
      return this.$store.getters.isLoggedIn
    }
  },
  // data에 변화가 일어나느 시점에 실행하는 함수 
  // updated(){
  //   this.isLoggedIn = this.$session.has('jwt')
  // },
  mounted(){
    if(this.$session.has('jwt')){
      const token = this.$session.get('jwt')
      this.$store.dispatch('login', token)
    }
  }
}
</script>


<style>boot
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
#nav a.router-link-exact-active{
  color: #42b983;
}
</style>