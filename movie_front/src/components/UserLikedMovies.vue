<template>
  <div class="mt-3">
    <MovieList :movies="userLikedMoviesList" :currentPage="currentPage"/>
  </div>
</template>

<script>
import MovieList from '@/components/MovieList'
export default {
  name: 'UserLikedMovies',
  props:{
    userLikedMoviesList:{
      type:Array,
      required :true
    }
  },
  components:{
    MovieList
  },
  data(){
    return{
      currentPage:1,
    }
  }
  
}
</script>

<style>
</style>