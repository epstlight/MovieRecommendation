<template>
  <b-card class="card border col-3" title="" :img-src="movie.poster_url" img-alt="poster" img-top>
    <b-card-text>
      <span class="badge badge-success" v-text="movie.naver_score"></span>
      <br />
      <h4 class="card-title mt-1 mb-0" v-text="movie.title" @click="goDetail"></h4>
      <small class="text-muted mb-0" >({{ movie.grade }})</small>
      <small class="text-muted mt-0 d-flex">개봉일 : {{ movie.opendt }}</small>
    </b-card-text>
  </b-card>
</template> 

<script>
import router from "@/router";
import { mapGetters } from "vuex";
export default {
  name: "MovieListItem",
  props: {
    movie: {
      type: Object,
      required: true
    },
  },
  data(){
    return{
      movie_detail : {},
    }
  },
  computed: {
    ...mapGetters(["isLoggedIn", "options", "userId"])
  },
  methods: {
    goDetail(){
      router.push(`/moviedetail/${this.movie.id}`)
    },
  },
  mounted(){
  }
};
</script>

<style>
</style>