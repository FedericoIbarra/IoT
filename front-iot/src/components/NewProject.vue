<template>

  <div>

    <b-modal id="modalproj" title="Crear nuevo proyecto" ref="modalproj" hide-footer=true>
      <b-form @submit="onSubmit" v-if="show">

        <b-form-group id="nodeName"
                      label="Nombre del nodo:"
                      label-for="input-2">
          <b-form-input id="input-2"
                        v-model="form.nodeName"
                        type="text"
                        required
                        placeholder="Ingrese nodo"></b-form-input>
        </b-form-group>

        <b-form-group id="plant"
                      label="Tipo de planta:"
                      label-for="input-3">
          <b-form-input id="input-3"
                        v-model="form.plant"
                        type="text"
                        required
                        placeholder="Ingrese planta"></b-form-input>
        </b-form-group>

        <b-container fluid>
          <b-row>
            <b-col lg="4" class="col">
              <h5>Temp:</h5>
            </b-col>

            <b-col lg="4" class="col">
              <h5>pH:</h5>
            </b-col>

            <b-col lg="4" class="col">
              <h5>Humedad:</h5>
            </b-col>
          </b-row>

          <b-row>
            <b-col lg="4" class="col">
              <b-form-input id="input-3"
                            v-model="form.tempMin"
                            type="number"
                            required
                            placeholder="Min">
              </b-form-input>
            </b-col>

            <b-col lg="4" class="col">
              <b-form-input id="input-3"
                            v-model="form.phMin"
                            type="number"
                            required
                            placeholder="Min">
              </b-form-input>
            </b-col>

            <b-col lg="4" class="col">
              <b-form-input id="input-3"
                            v-model="form.humMin"
                            type="number"
                            required
                            placeholder="Min">
              </b-form-input>
            </b-col>
          </b-row>

        <b-row>
          <p></p>
        </b-row>

          <b-row>
            <b-col lg="4" class="col">
              <b-form-input id="input-3"
                            v-model="form.tempMax"
                            type="number"
                            required
                            placeholder="Max">
              </b-form-input>
            </b-col>

            <b-col lg="4" class="col">
              <b-form-input id="input-3"
                            v-model="form.phMax"
                            type="number"
                            required
                            placeholder="Max">
              </b-form-input>
            </b-col>

            <b-col lg="4" class="col">
              <b-form-input id="input-3"
                            v-model="form.humMax"
                            type="number"
                            required
                            placeholder="Max">
              </b-form-input>
            </b-col>
          </b-row>
        </b-container>



        <button class="sendbut" type="submit">Crear Proyecto</button>
      </b-form>

    </b-modal>
  </div>

</template>

<script>
  import axios from 'axios'
  import URL from '../constants.js'

  export default {
    name: 'NewProject',
    data() {
      return {
        form: {
          user: '',
          nodeName: '',
          plant: '',
          tempMax: '',
          tempMin: '',
          phMax: '',
          phMin: '',
          humMax: '',
          humMin: ''
        },
        show: true
      }
    },
    mounted () {
      //this.form.user = sessionStorage.getItem('usr');
    },
    methods: {
      onSubmit(evt) {
        evt.preventDefault()
        this.form.user = sessionStorage.getItem('usr');
          let body = this.form.user + ','
                   + this.form.nodeName + ','
                   + this.form.plant + ','
                   + this.form.tempMax + ','
                   + this.form.tempMin + ','
                   + this.form.phMax + ','
                   + this.form.phMin + ','
                   + this.form.humMax + ','
                   + this.form.humMin;

          axios
            .post(URL+'/api/project', body)
            .then(response => (this.res = response));

          //alert(JSON.stringify(this.form));
        this.$refs['modalproj'].hide();
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
