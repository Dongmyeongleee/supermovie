import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import BoardList from '@/views/community/BoardList'
import BoardListDetail from '@/views/community/BoardListDetail'
import BoardCreate from '@/views/community/BoardCreate'
import Profile from '@/views/accounts/Profile'
import SearchBar from '@/views/SearchBar'
import Recommend from '@/views/movies/Recommend'
import MovieDetail from '@/views/movies/MovieDetail'
import Search from '@/views/movies/Search'

Vue.use(VueRouter)

const routes = [
  {
    path: '',
    name: 'Home',
    component: Home
  },
  {
    path: '/search/',
    name: 'SearchBar',
    component: SearchBar,
  },
  {
    path: '/accounts/signup/',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/accounts/login/',
    name: 'Login',
    component: Login
  },
  {
    path: '/community/boardlist/',
    name: 'BoardList',
    component: BoardList
  },
  {
    path: '/community/boardlistDetail/:boardId/',
    name: 'BoardListDetail',
    component: BoardListDetail
  },
  {
    path: '/community/boardcreate/',
    name: 'BoardCreate',
    component: BoardCreate
  },
  {
    path: '/accounts/profile/',
    name: 'Profile',
    component: Profile
  },
  {  
    path: '/recommend/',
    name: 'Recommend',
    component: Recommend
  },

  {  
    path: '/movies/:movieId',
    name: 'MovieDetail',
    component: MovieDetail
  },
  {
    path: '/search?query=:query',
    name: 'Search',
    component: Search,
    props: true
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
