<template>
  <div class="card-deck">
    <MovieListItem v-for="movie in selectMovies" :key="movie.id" :movie="movie" />
  </div>
</template>

<script>
import MovieListItem from '@/components/MovieListItem'
export default {
  name: "MovieList",
  props: {
    movies: {
      type: Array,
      required: true
    }
  },
  components :{
    MovieListItem
  },
  date(){
    return {
      seleteSort : 0, 
    }
  },
  computed :{
    selectMovies : function() {
      if (this.seleteSort === 0){
        return this.movies
      }
      // else{
      //    return this.movies.filter(movie => {
      //     return movie.genre_id === this.selectedGenreId
      //   })
      // }
      return this.movies
    }
  }
};
</script>

<style>
</style>