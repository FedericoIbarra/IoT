<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="dark" fixed="top">
      <b-navbar-brand href="/"><img alt="Choya logo" src="../assets/Choya.png">Choya Labs</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>

          <b-nav-item><router-link v-if="login" to="/dashboard">Panel de control</router-link></b-nav-item>
          <b-nav-item><router-link v-if="login" to="/data">Datos</router-link></b-nav-item>
          <b-nav-item><router-link to="/about">Quienes Somos</router-link></b-nav-item>

        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto" >


          <b-nav-item v-if="login">
            <NewProject></NewProject>
            <p class="reg" v-on:click="showNPModal">Nuevo proyecto</p>
          </b-nav-item>

          <b-nav-item v-else>
            <p class="reg" v-b-modal.modalreg>Registrarse</p>
            <Logup></Logup>
          </b-nav-item>


          <b-nav-item v-if="login">
            <p class="ini" v-on:click="logOut">Cerrar Sesión</p>
          </b-nav-item>

          <b-nav-item v-else>
            <p class="ini" v-b-modal.modal-ini hide-footer=true>Iniciar Sesión</p>
            <b-modal id="modal-ini" title="Iniciar Sesión">
              <b-form @submit="onSubmit">
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
          </b-nav-item>

        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>

import Logup from './Logup.vue'
import NewProject from './NewProject.vue'
import axios from 'axios'
import URL from '../constants.js'

export default {
  name: 'NavBar',
  components: {
    Logup,
    NewProject
  },
  data() {
      return {
        form: {
          user: '',
          password: ''
        },
        res: '',
        login: false
      }
    },
    mounted () {
      /*Local debug
      sessionStorage.setItem('usr', 'usr1');
      sessionStorage.setItem('usrNodes', ['Mock 1', 'Mock 2']);
      console.log(sessionStorage.getItem('usr'));
      this.login = true;
      */
    },

    methods: {
      showNPModal() {
        this.$bvModal.show("modalproj");
      },
      logOut() {
        sessionStorage.clear();
        this.login = false;
        this.unlog = true;
      },

      onSubmit(evt) {
        evt.preventDefault();
        this.login = true;
        this.unlog = false;
        //Post request
        let body = this.form.user + ',' + this.form.password;
        axios
          .post(URL+'/api/login', body)
          .then(response => {
            this.res = response.data

            if (this.res == this.form.user) {
              this.login = true;
              sessionStorage.setItem('usr', this.form.user);
            }


          });
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

