<template>
  <div class="hello">
    <h3>Estatus actual</h3>

    <b-container fluid>
      <b-row>
        <b-col lg="2" class="col">
          <h5>Nodo: {{hw}}</h5>
          <p>Planta: {{plant}}</p>
          <p>Estado: {{status}}</p>
        </b-col>

        <b-col lg="2" class="col">
          <img alt="Choya logo" class="imgf" src="../assets/Choya.png">
        </b-col>

        <b-col lg="2" class="col">
          <h5>Temperatura</h5>
          <p>Actual: {{temperature}}ºC</p>
          <p>Promedio: {{tavg}}ºC</p>
          <p>Rango: {{tmin}}ºC~{{tmax}}ºC</p>
        </b-col>

        <b-col lg="2" class="col">
          <div class="cont" v-bind:style="{ backgroundColor: tColor}"></div>
        </b-col>

        <b-col lg="2" class="col">
          <h5>pH</h5>
          <p>Actual: {{ph}}</p>
          <p>Promedio: {{pavg}}</p>
          <p>Rango: {{pmin}}~{{pmax}}</p>
        </b-col>

        <b-col lg="2" class="col">
          <div class="cont" v-bind:style="{ backgroundColor: pColor}"></div>
        </b-col>

      </b-row>
    </b-container>

  </div>
</template>

<script>
import axios from 'axios'
import URL from '../constants.js'

export default {
  name: 'Dashboard',
  props: {
    msg: String
  },
  data () {
      return {
        hw: "Mock 1",
        plant: "Lechuga romana",
        status: "Ok",
        temperature: '',
        tmax: 27,
        tmin: 23,
        tavg: 25,
        tColor: 'red',
        ph: '0',
        pmax: 7.5,
        pmin: 6.6,
        pavg: 7.0,
        pColor: 'green'
      }
  },
  mounted () {
    axios
      .get(URL + '/api/data/current')
      .then(res => {
        this.ph = res.data[0][0];
        this.temperature = res.data[0][1];

        if (this.temperature < this.tmax && this.temperature > this.tmin) {
          this.tColor = 'green';
        } else {
          this.tColor = 'red';
        }

        if (this.ph < this.pmax && this.ph > this.pmin) {
          this.pColor = 'green';
        } else {
          this.pColor = 'red';
        }


        if (this.pColor == this.tColor == 'green') {
          this.status = 'Ok';
        } else if(this.pColor == 'red' && this.tColor == 'red') {
          this.status = 'Crítico';
        } else {
          this.status = 'Precaución';
        }
      });

      axios
        .get(URL + '/api/data/year')
        .then(res => {
          this.pavg = res.data[0][0];
          this.tavg = res.data[0][1];
        });
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  h3{
      margin-top: 2em;
      margin-bottom: 1em;
      padding-top: 1em;
  }

  h5{
      margin: 1em;
  }

  .imgf{
    display: block;
    width:9em;
    max-height: 9em;
    margin: auto;
  }

  .hello {
    padding-bottom: 3em;
  }

  .cont{
    width: 8em; /*container-width*/
    height: 8em;
    border-radius: 50%;
    margin: auto;
    background-color: black;
  }

  .col {
    margin-top: 3em;
  }

  </style>
