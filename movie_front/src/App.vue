<template>
  <div id="app">
    <div
      id="nav"
      class="header clearfix navbar-expand-sm navbar-light bg-light"
    >
      <div v-if="isLoggedIn" class="mb-4">
        <router-link to="/home">Movie Infomation</router-link>
        <router-link class="float-right" to="/userprofile">
          <img src="@/images/user_1.png" alt="userprofile" />
        </router-link>
        <span class="float-right mx-1">|</span>
        <a class="float-right" @click.prevent="logout" href="logout/">Logout</a>
        <span class="float-right mx-1">|</span>
        <router-link class="float-right" to="/userpage">UserPage</router-link>
      </div>
      <div v-else>
        <router-link to="/">Movie Infomation</router-link>
        <!-- <router-link class="float-right" to="/login" >Login</router-link>
        <span class="float-right mx-1"> | </span>
        <router-link class="float-right" to="/signup" >Signup</router-link>  -->
      </div>
    </div>
    <div>
      <router-view />
    </div>
  </div>
</template>


<script>
import { mapGetters } from "vuex";
import router from "@/router";
export default {
  name: "App",
  data() {
    return {};
  },

  methods: {
    logout() {
      this.$session.destroy();
      this.$store.dispatch("logout");
      router.push("/");
    }
  },
  computed: {
    ...mapGetters(["isLoggedIn", "options", "userId"])
  },
  created() {
    if (this.$session.has("jwt")) {
      const token = this.$session.get("jwt");
      this.$store.dispatch("login", token);
    }
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
#nav {
  padding: 30px;
  font-size: 25px;
}
#nav a {
  font-weight: bold;
  color: #2c3e50;
}
#nav a.router-link-exact-active {
  color: #42b983;
}
</style>