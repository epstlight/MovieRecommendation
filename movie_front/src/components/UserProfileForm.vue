<template>
  <div class="user-profile-div">
    <h1>User Profile</h1>
    <hr />
    <h4 class="mb-5">ID : {{ credential.username }}</h4>
    <h4 class="mb-5">E-mail : {{ credential.email }}</h4>
    <h4 class="mb-5" v-if="credential.gender===false">Gender : Man</h4>
    <h4 class="mb-5" v-else>Gender : Woman</h4>
  </div>
</template>

<script>

import router from "@/router";
import { mapGetters } from "vuex"; 

export default {
  name: "UserProfileForm",
  props:{
    credential:{
      type: Object,
      require : true
    }
  },
  
  data() {
    return {
    };
  },
  computed: {
    ...mapGetters(["isLoggedIn", "options", "userId"])
  },
  methods: {
    checkLoggedIn() {
      if (!this.isLoggedIn) {
        router.push("/login");
      }
    }
  },
  
  mounted() {
    if (this.isLoggedIn) {
      this.checkLoggedIn();
    }
  }
};
</script>

<style>
</style>