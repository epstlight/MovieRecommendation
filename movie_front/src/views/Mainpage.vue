<template>
  <div>
    <b-button size="lg" pill variant="outline-secondary" class="position-absolute" @click="goLogin">login</b-button>
    <b-button size="lg" pill variant="outline-secondary" class="position-absolute" @click="goSignup">signup</b-button>
    <b-img src="https://picsum.photos/300/150/?image=41" fluid-grow alt="image"></b-img>
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
</style>