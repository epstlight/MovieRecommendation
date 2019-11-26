<template>
  <div class="card border col-2">
    <a class="" @click="goDetailPage" href=''>
      <img :src="movie.poster_url" class="card-img-top" alt="poster" />
      <div class="card-body">
        <span class="badge badge-success" v-text="movie.naver_score"></span>
        <span class="badge badge-primary ml-1" v-text="movie.avr_score"></span>
        <h4 class="card-title mt-1" v-text="movie.title"></h4>
        <p class="card-text">
          <small class="text-muted" v-text="movie.opendt"></small>
        </p>
      </div>
    </a>
  </div>
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