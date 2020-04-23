import '@babel/polyfill'
import 'mutationobserver-shim'
import Vue from 'vue'
import './plugins/bootstrap-vue'
import App from './App.vue'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import VueRouter from 'vue-router'

import Landing from './components/Landing.vue'
import AboutUs from './components/AboutUs.vue'
import Data from './components/Data.vue'
import Dashboard from './components/Dashboard.vue'

Vue.use(VueRouter)
Vue.config.productionTip = false

// Install BootstrapVue
Vue.use(BootstrapVue)

const router = new VueRouter({
  routes: [
    {
      path: '/',
      component: Landing
    },
    {
      path: '/about',
      component: AboutUs
    },
    {
      path: '/data',
      component: Data
    },
    {
      path: '/dashboard',
      component: Dashboard
    }

  ]
})

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
