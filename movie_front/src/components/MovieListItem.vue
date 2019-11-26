<template>
  <b-card class="card border col-3" title="" :img-src="movie.poster_url" img-alt="poster" img-top>
    <b-card-text>
      <span class="badge badge-success" v-text="movie.naver_score"></span>
      <span class="badge badge-primary ml-1" v-text="movie.avr_score"></span>
      <br />
      <h4 class="card-title mt-1" v-text="movie.title"></h4>
      <small class="text-muted" v-text="movie.opendt"></small>
    </b-card-text>
  </b-card>
</template>

<script>
export default {
  name: "MovieListItem",
  props: {
    movie: {
      type: Object,
      required: true
    }
  },
  mouted() {
    console.log(this.movie);
  }
};
</script>

<style>
</style>