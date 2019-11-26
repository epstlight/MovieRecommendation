<template>
  <div class="home">
    <h1 class="text-center">Movie List</h1>
    <hr>
    <hr>
    <MovieList :movies="movies"/>
  </div>
</template>

<script>
import MovieList from '@/components/MovieList'
import axios from 'axios'
import { mapGetters } from 'vuex' 

export default {
  name: 'Home',
  data() {
    return {
      movies: []
    }
  },
  computed: {
    // ...A ; A 가 가진 아이템 다 뿌려 / js 문법 
    ...mapGetters([
      'isLoggedIn',
      'options',
      'userId'
    ]) 
  },
  components: {
    MovieList
  },
  methods: {
    // 사용자 로그인 유무를 확인하여 로그인되어있지 않을 시 로그인 페이지로 보내겠다. 
    getMovies(){
      const SERVER_IP = process.env.VUE_APP_SERVER_IP;
      axios.get(`${SERVER_IP}/api/v1/movies/`)
        .then(response =>{
          this.movies = response.data
        })
        .catch(error =>{
          console.log(error)
        })
    }
  },

  mounted() {
    this.getMovies()
  },
}
</script>

<style>
</style>