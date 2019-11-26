<template>
  <div>
    <div id="nav" class="p-0">
      <b-nav pills class="justify-content-center">
        <b-nav-item class="mx-1" @click="seleteTotal">전체</b-nav-item>
        <b-nav-item-dropdown
          class="mx-1"
          id="my-nav-dropdown"
          text="장르별"
          toggle-class="nav-link-custom"
          right
        >
          <b-dropdown-item @click="seleteGenre">장르</b-dropdown-item>
        </b-nav-item-dropdown>

        <b-nav-item-dropdown
          class="mx-1"
          id="my-nav-dropdown"
          text="Search"
          toggle-class="nav-link-custom"
          right
        >
          <b-dropdown-item>감독</b-dropdown-item>
          <b-dropdown-item>배우</b-dropdown-item>
          <b-dropdown-item>영화제목</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-nav>
    </div>
    <hr />
    <div class="nav">
      <b-dropdown size="sm" :text="sort" class="ml-auto" variant="success" >
        <b-dropdown-item-button @click="selectSort(0)" >최신순</b-dropdown-item-button>
        <b-dropdown-item-button @click="selectSort(1)" >네이버 평점순</b-dropdown-item-button>
        <b-dropdown-item-button @click="selectSort(2)" >회원 평점순</b-dropdown-item-button>
      </b-dropdown>
    </div>

    <b-card-group deck class="card-deck mt-2 mb-5">
      <MovieListItem v-for="movie in selectMovies1" :key="movie.id" :movie="movie" />
    </b-card-group>
    <b-card-group deck class="card-deck mb-5">
      <MovieListItem v-for="movie in selectMovies2" :key="movie.id" :movie="movie" />
    </b-card-group>
  </div>
</template>

<script>
import router from "@/router";
import MovieListItem from "@/components/MovieListItem";
import { mapGetters } from "vuex";

export default {
  name: "MovieList",
  props: {
    movies: {
      type: Array,
      required: true
    },
    sortNm : {
      type: String,
      required : true
    }
  },
  components: {
    MovieListItem
  },
  date() {
    return {
      sortNum: 0,
      sort :""
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
    seleteTotal() {
      this.sortNum = 0;
    },
    seleteGenre() {
      if (!this.isLoggedIn) {
        router.push("/login");
      } else {
        this.sortNum = 1;
      }
    },
    
  },
};
</script>

<style>
#nav {
  padding: 0px;
  font-weight: bold;
  color: #2c3e50;
}
#nav li a {
  font-size: 20px;
  color: gray;
}

#nav li a:hover {
  font-size: 21px;
  color: white;
  background-color: gray;
}

#nav li a:active {
  font-size: 20px;
  color: white;
  background-color: gray;
}
</style>