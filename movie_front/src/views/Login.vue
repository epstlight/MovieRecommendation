<template>
  <div>
    <h1>Log In</h1>
    <!-- 3. 컴포넌트 사용 -->
    <hr>
    <LoginForm />
  </div>
</template>

<script>
// 1. 컴포넌트 호출
import LoginForm from '@/components/LoginForm'
export default {
  name: 'Login',
  components: {
    // 2. 컴포넌트 등록
    LoginForm, 
  }
}
</script>

<style>
</style>