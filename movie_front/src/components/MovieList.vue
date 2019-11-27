<template>
  <div>
    <b-card-group deck class="card-deck mt-2 mb-5">
      <MovieListItem
        v-for="movie in selectMovies1"
        :key="movie.id"
        :movie="movie"
        :per-page="perPage"
        :current-page="currentPage"
      />
    </b-card-group>
    <b-card-group deck class="card-deck mb-5">
      <MovieListItem
        v-for="movie in selectMovies2"
        :key="movie.id"
        :movie="movie"
        :per-page="perPage"
        :current-page="currentPage"
      />
    </b-card-group>
    <div class="d-flex justify-content-center mb-3">
      <b-pagination
        v-model="currentPage"
        :total-rows="rows"
        :per-page="perPage"
        aria-controls="my-table"
      ></b-pagination>
    </div>
  </div>
</template> 

<script>
// import router from "@/router";
import MovieListItem from "@/components/MovieListItem";
import { mapGetters } from "vuex";
import { BPagination } from "bootstrap-vue";

export default {
  name: "MovieList",
  props: {
    movies: {
      type: Array,
      required: true
    },
    currentPage:{
      type: Number,
      required: true
    }
  },
  components: {
    MovieListItem,
    BPagination
  },
  data() {
    return {
      perPage:10,
    };
  },
  computed: {
    ...mapGetters(["isLoggedIn", "options", "userId"]),
    selectMovies1: function() {
      const check = (this.currentPage - 1) * this.perPage;
      return this.movies.slice(check + 0, check + 5);
    },
    selectMovies2: function() {
      const check = (this.currentPage - 1) * this.perPage;
      return this.movies.slice(check + 5, check + 10);
    },
    rows() {
      return this.movies.length;
    }
  },
  methods: {
  },
  mounted(){
  }
};
</script>

<style>
</style>