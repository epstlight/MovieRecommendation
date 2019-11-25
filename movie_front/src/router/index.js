import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
// @ => src 폴더 / .vue 도 생략 가능 
import Login from '@/views/Login'
import Signup from '@/views/Signup'
import Userprofile from '@/views/Userprofile'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/signup',
    name: 'signup',
    component: Signup
  },
  {
    path: '/userprofile',
    name: 'userprofile',
    component: Userprofile
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router