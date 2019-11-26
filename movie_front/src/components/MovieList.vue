<template>
  <div>
    <b-card-group deck class="card-deck mt-2 mb-5">
      <MovieListItem v-for="movie in selectMovies1" :key="movie.id" :movie="movie"/>
    </b-card-group>
    <b-card-group deck class="card-deck mb-5">
      <MovieListItem v-for="movie in selectMovies2" :key="movie.id" :movie="movie"/>
    </b-card-group>
    <div class="mt-3">
      <b-pagination-nav base-url="#" align="center" v-model="page"></b-pagination-nav>
    </div>
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
    }
  },
  components: {
    MovieListItem
  },
  data() {
    return {
      page: 10
    };
  },
  computed: {
    ...mapGetters(["isLoggedIn", "options", "userId"]),
    selectMovies1: function() {
      return this.movies.slice(0, 5);
    },
    selectMovies2: function() {
      return this.movies.slice(5, 10);
    }
  },
  methods: {
    pageGet(pageNum) {
      console.log(pageNum);
    },
    getDetailData(movie_data){
      this.$emit('getDetailData', movie_data)
    },
  }
};
</script>

<style>
</style>