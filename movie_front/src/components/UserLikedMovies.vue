<template>
  <div class="mt-3">
    <MovieList :movies="userLikedMoviesList"/>
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
  }
  
}
</script>

<style>
</style>