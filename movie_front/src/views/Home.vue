<template>
  <div class="home mx-0 my-2">
    <h1 class="text-center">Movie List</h1>
    <hr />
    <MovieList :movies="movies" :sortNm="sortNm"/>
    
  </div>
</template>

<script>
import MovieList from "@/components/MovieList";
import axios from "axios";
import { mapGetters } from "vuex";

export default {
  name: "Home",
  data() {
    return {
      movies: [],
      sortNm : "최신순",
    };
  },
  computed: {
    // ...A ; A 가 가진 아이템 다 뿌려 / js 문법
    ...mapGetters(["isLoggedIn", "options", "userId"])
  },
  components: {
    MovieList
  },
  methods: {
    // 사용자 로그인 유무를 확인하여 로그인되어있지 않을 시 로그인 페이지로 보내겠다.
    getMovies() {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP;
      axios
        .get(`${SERVER_IP}/api/v1/movies/`)
        .then(response => {
          this.movies = response.data;
          this.movies.sort(function(a, b) {
            return a.opendt > b.opendt ? -1 : a.opendt < b.opendt ? 1 : 0;
          });
        })
        .catch(error => {
          console.log(error);
        });
    },
    selectSort(value){
      if (value === 1){
        this.movies.sort(function(a, b) {
          this.sort ="네이버 평점순"
          return a.naver_score > b.naver_score ? -1 : a.naver_score < b.naver_score ? 1 : 0;
        });
      }
      else if (value === 2){
        this.movies.sort(function(a, b) {
          this.sort ="회원 평점순"
          return a.avr_score > b.avr_score ? -1 : a.avr_score < b.avr_score ? 1 : 0;
        });
      }
      else {
        this.movies.sort(function(a, b) {
          this.sort ="최신순"
          return a.opendt > b.opendt ? -1 : a.opendt < b.opendt ? 1 : 0;
        });
      }
    }
  },

  mounted() {
    this.getMovies();
  }
};
</script>

<style>
</style>