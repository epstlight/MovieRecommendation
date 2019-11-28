<template>
  <div>
    <b-button-group id="twobtn" size="lg" class="position-fixed" vertical style="width: 20%; margin-top: 30%; margin-left:40%;">
      <b-button pill variant="success" @click="goLogin" class="mb-4 font-weight-bold">Login</b-button>
      <b-button pill variant="success" @click="goSignup" class="font-weight-bold">Signup</b-button>
    </b-button-group>
    <b-img :src="require('../assets/images/mainback.png')" fluid-grow alt="image" style="position:absolute; filter: blur(5px); z-index:-1;"></b-img>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import router from "@/router";
export default {
  name: "Mainpage",
  computed: {
    ...mapGetters(["isLoggedIn", "options", "userId"])
  },
  methods:{
    goLogin(){
      if (!this.isLoggedIn){
        router.push('/login')
      }
    },
    goSignup(){
      if (!this.isLoggedIn){
        router.push('/signup')
      }
    }
  },
  created() {
    if (this.isLoggedIn) {
      router.push("/home");
    }
  }
};
</script>

<style>
 #twobtn {
 }
</style>