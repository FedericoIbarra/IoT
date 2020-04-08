<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="dark" fixed="top">
      <b-navbar-brand href="/"><img alt="Choya logo" src="../assets/Choya.png">Choya Labs</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item><router-link to="/data">Datos</router-link></b-nav-item>
          <b-nav-item><router-link to="/dashboard">Dashboard</router-link></b-nav-item>
          <b-nav-item><router-link to="/about">Quienes Somos</router-link></b-nav-item>

        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto" v-if="!login">
            <b-nav-item>
              <p class="reg" v-b-modal.modal-reg>Registrarse</p>
            </b-nav-item>

            <b-nav-item>
              <p class="ini" v-b-modal.modal-ini>Iniciar Sesión</p>
            </b-nav-item>

            <b-modal id="modal-ini" title="Iniciar Sesión" hide-footer=true>
              <b-form @submit="onSubmit" @reset="onReset" v-if="show">
                <b-form-group id="input-group-1"
                              label="Usuario:"
                              label-for="input-1">
                  <b-form-input id="input-1"
                                v-model="form.user"
                                type="text"
                                required
                                placeholder="Ingrese usuario"></b-form-input>
                </b-form-group>

                <b-form-group id="input-group-2" label="Contraseña:" label-for="input-2">
                  <b-form-input id="input-2"
                                type="password"
                                v-model="form.password"
                                required
                                placeholder="Ingrese contraseña"></b-form-input>
                </b-form-group>

                <button class="sendbut" type="submit">Iniciar Sesión</button>
              </b-form>

            </b-modal>

            <Logup></Logup>

        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>

import Logup from './Logup.vue'

export default {
  name: 'NavBar',
  components: {
    Logup
  },
  data() {
      return {
        form: {
          user: '',
          password: ''
        },
        show: true,
        login: false
      }
    },
    methods: {
      onSubmit(evt) {
        evt.preventDefault()
        this.login = true;
      },
      onReset(evt) {
        evt.preventDefault()
        // Reset our form values
        this.form.user = ''
        this.form.password = ''
        // Trick to reset/clear native browser form validation state
        this.show = false
        this.$nextTick(() => {
          this.show = true
        })
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
    margin: 0;
    border: 0px;
    background-color: inherit;
    color: #02B392;
    font-weight: bold;
  }

  .reg:hover {
    color: #016653;
  }

  .ini{
    margin: 0;
    border: 0px;
    background-color: inherit;
    color: #F2F2F2;
  }

  .custom-modal{
    background-color: #000000;
  }

  .sendbut{
    display: block;
    margin: 2em auto 1em auto;
    background-color: inherit;
    border: 0;
    color: #016653;
  }


</style>
