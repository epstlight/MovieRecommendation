<template>
  <div class="container">
    <h1>Log In</h1>
    <hr>
    <LoginForm />
  </div>
</template>

<script>
import LoginForm from '@/components/LoginForm'
export default {
  name: 'Login',
  components: {
    LoginForm, 
  }
}
</script>

<style>
</style>