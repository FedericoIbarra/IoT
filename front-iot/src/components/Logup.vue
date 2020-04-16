<template>

  <div>

    <b-modal id="modalreg" title="Iniciar Sesión" ref="modalreg" hide-footer=true>
      <b-form @submit="onSubmit" v-if="show">
        <b-form-group id="username"
                      label="Usuario:"
                      label-for="input-1">
          <b-form-input id="input-1"
                        v-model="form.user"
                        type="text"
                        required
                        placeholder="Ingrese usuario"></b-form-input>
        </b-form-group>

        <b-form-group id="email"
                      label="Usuario:"
                      label-for="input-2">
          <b-form-input id="input-2"
                        v-model="form.email"
                        type="text"
                        required
                        placeholder="Ingrese usuario"></b-form-input>
        </b-form-group>

        <b-form-group id="pass-1" label="Contraseña:" label-for="input-3">
          <b-form-input id="input-3"
                        type="password"
                        v-model="form.password1"
                        required
                        placeholder="Ingrese contraseña"></b-form-input>
        </b-form-group>

        <b-form-group id="pass-2" label=" Confirmar Contraseña:" label-for="input-4">
          <b-form-input id="input-4"
                        type="password"
                        v-model="form.password2"
                        required
                        placeholder="Ingrese contraseña"></b-form-input>
        </b-form-group>

        <b-form-group id="plant" label="Tipo de cultivo:" label-for="input-5">
          <b-form-input id="input-5"
                        v-model="form.plant"
                        required></b-form-input>
        </b-form-group>

        <button class="sendbut" type="submit">Crear usuario</button>
      </b-form>

    </b-modal>
  </div>

</template>

<script>
  import axios from 'axios'
  import URL from '../constants.js'

  export default {
    name: 'Logup',
    data() {
      return {
        form: {
          user: '',
          email: '',
          password1: '',
          password2: '',
          plant: ''
        },
        show: true
      }
    },
    methods: {
      onSubmit(evt) {
        evt.preventDefault()

        if (this.form.password1 == this.form.password2) {
          //Post request
          let body = this.form.user + ','
                   + this.form.password1 + ','
                   + this.form.email + ','
                   + this.form.plant;

          axios
            .post(URL+'/api/logup', body)
            .then(response => (this.res = response));

          //alert(JSON.stringify(this.form));
        }
        this.$refs['modalreg'].hide();
      }
    }
  }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

  .sendbut {
    display: block;
    margin: 2em auto 1em auto;
    background-color: inherit;
    border: 0;
    color: #016653;
  }

</style>
