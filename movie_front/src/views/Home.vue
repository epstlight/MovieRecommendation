<template>
  <div class="home">
    <h1>Movie</h1>
  </div>
</template>

<script>
// import axios from 'axios'
// import jwtDecode from 'jwt-decode' // JWT 의 payload 값을 해석해주는 라이브러리 
// import { mapGetters } from 'vuex' // import vuex from 'vuex' ; vuex.mapGetters
// import router from '@/router'
export default {
  name: 'Home',
  data() {
    return {
      // todos: []
    }
  },
  // computed: {
    // ...A ; A 가 가진 아이템 다 뿌려 / js 문법 
    // ...mapGetters([
    //   'isLoggedIn',
    //   'options',
    //   'userId'
    // ]) 
  // },
  components: {
    
  },
  methods: {
    // 사용자 로그인 유무를 확인하여 로그인되어있지 않을 시 로그인 페이지로 보내겠다. 
    // checkLoggedIn() {
      // // 1. 세션을 시작해서 
      // this.$session.start()
      // // 2. 'jwt' 가 있는지 확인하겠다. 
      // if(!this.$session.has('jwt')) {
      //   // 로그인 페이지로 보내겠다. 
      //   router.push('/login')
      // }
      // if(!this.isLoggedIn) {
      //   router.push('/login')
      // }
    // },

  },

  // mounted() {
    // if(this.isLoggedIn) {
    //   this.checkLoggedIn()

    // }
  // },
  // watch: {
  //   isLoggedIn() {
  //     this.checkLoggedIn()
  //   }
  // }
}
</script>

<style>
</style>