<template>
  <div>
    <UserLikedMovies />
    <br>
    <UserRatings />
  </div>
</template>

<script>
import UserLikedMovies from '@/components/UserLikedMovies'
import UserRatings from '@/components/UserRatings'
// import axios from "axios";
import { mapGetters } from "vuex";
// import router from "@/router";

export default {
  name:'Userpage',
  components:{
    UserLikedMovies,
    UserRatings
  },
  computed: {
    // ...A ; A 가 가진 아이템 다 뿌려 / js 문법
    ...mapGetters(["isLoggedIn", "options", "userId"])
  }
}
</script>

<style>

</style>