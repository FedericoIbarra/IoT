<template>
  <div class="regp">
    <b-navbar toggleable="lg" type="dark" variant="dark" >
      <b-navbar-brand href="/"><img alt="Choya logo" src="../assets/Choya.png">Choya Labs</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item><router-link to="/data">Datos</router-link></b-nav-item>
          <b-nav-item><router-link to="/dashboard">Dashboard</router-link></b-nav-item>
          <b-nav-item><router-link to="/about">Quienes Somos</router-link></b-nav-item>

        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">

          <b-nav-item><router-link to="/" class="reg">Registrarse</router-link></b-nav-item>
          <b-nav-item><router-link to="/">Iniciar Sesión</router-link></b-nav-item>


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
  img {
    margin-left: 0.5em;
    
    height: 2.6em;
  }
  a {
    color: #F2F2F2;
  }

  a:hover{
    color: #a2a2a2;
    text-decoration: none;
  }

  .reg {
    color: #02B392;
    font-weight: bold;
  }

  .reg:hover {
    color: #016653;
  }

</style>
