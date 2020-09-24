import Vue from 'vue'
import Router from 'vue-router'
import Register from '../components/Register';
import Login from '../components/Login';
import index from '../components/index';
import Add from "../components/Add";
import update_emp from "../components/update_emp";
Vue.use(Router)

export default new Router({
  routes: [
    {
      path:'/',
      name:'Register',
      component:Register,
    },
    {
      path: '/Register',
      name: 'Register',
      component:Register,
    },
    {
      path: '/Login',
      name: 'Login',
      component:Login,
    },
    {
      path: '/index',
      name: 'index',
      component:index,
    },
    {
      path: '/Add',
      name: 'Add',
      component:Add,
    },
    {
      path:'/update_emp',
      name: 'update_emp',
      component:update_emp,
    },
    {
      path: '/update_emp/:id',
      name: 'update_emp',
      component:update_emp,
    },
  ]
})
