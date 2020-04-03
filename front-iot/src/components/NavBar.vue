<template>
  <div class="regp">
    <b-navbar toggleable="lg" type="dark" variant="dark" >
      <b-navbar-brand href="/">Choya Labs</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item><router-link to="/data" class="regp">Datos</router-link></b-nav-item>
          <b-nav-item><router-link to="/dashboard" class="regp">Dashboard</router-link></b-nav-item>
          <b-nav-item><router-link to="/about" class="regp">Quienes Somos</router-link></b-nav-item>

        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">

          <b-nav-item href="#">Registrarse</b-nav-item>
          <b-nav-item href="#">Iniciar Sesión</b-nav-item>


        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>


export default {
  name: 'NavBar',
  data () {
      return {
        info: null
      }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  a {
    color: #F2F2F2;
  }

  a:hover{
    color: #a2a2a2;
    text-decoration: none;
  }

</style>
