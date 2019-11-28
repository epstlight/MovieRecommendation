<template>
  <div class="container my-4">
    <h1>Sign Up</h1>
    <hr>
    <SignupForm />
  </div>
  
</template>

<script>
import SignupForm from '@/components/SignupForm'
import { mapGetters } from "vuex";
import router from "@/router"

export default {
  name: 'Signup',
  components: {
    SignupForm, 
  },
  computed: {
    ...mapGetters(["isLoggedIn", "options", "userId"])
  },
  created(){
    if (this.isLoggedIn) {
      router.push('/home')
    }
  }
}
</script>

<style>

</style>