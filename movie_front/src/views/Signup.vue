<template>
  <div class="container">
    <h1>Sign Up</h1>
    <hr>
    <SignupForm />
  </div>
  
</template>

<script>
import SignupForm from '@/components/SignupForm'

export default {
  name: 'Signup',
  components: {
    SignupForm, 
  }
}
</script>

<style>

</style>