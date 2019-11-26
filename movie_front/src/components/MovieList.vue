<template>
  <div>
    <b-card-group deck class="card-deck mt-2 mb-5">
      <MovieListItem v-for="movie in selectMovies1" :key="movie.id" :movie="movie" />
    </b-card-group>
    <b-card-group deck class="card-deck mb-5">
      <MovieListItem v-for="movie in selectMovies2" :key="movie.id" :movie="movie" />
    </b-card-group>
  </div>
</template>

<script>
// import router from "@/router";
import MovieListItem from "@/components/MovieListItem";
import { mapGetters } from "vuex";

export default {
  name: "MovieList",
  props: {
    movies: {
      type: Array,
      required: true
    },
  },
  components: {
    MovieListItem
  },
  date() {
    return {
    };
  },
  computed: {
    ...mapGetters(["isLoggedIn", "options", "userId"]),
    selectMovies1: function() {
      // if (this.sortNum === 1){
      //   return this.movies.slice(0,5)
      // }
      // else if (this.sortNum === 2){
      //   return this.movies.slice(0,5)
      // }
      return this.movies.slice(0, 5);
    },
    selectMovies2: function() {
      // if (this.seleteSort === 1){
      //   return this.movies.slice(6,10)
      // }
      // else{
      //    return this.movies.filter(movie => {
      //     return movie.genre_id === this.selectedGenreId
      //   })
      // }

      return this.movies.slice(5, 10);
    }
  },
  methods: {
  }
};
</script>

<style>

</style>