<template>
  <div id="app">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <NavBar class="navb"/>

    <router-view class="bod"></router-view>
  </div>
</template>

<script>
import NavBar from './components/NavBar.vue'

export default {
  name: 'App',
  components: {
    NavBar
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  background-color: #F2F2F2;

}

.navb{
  margin-bottom: 5em;
}


</style>
