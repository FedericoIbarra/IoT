<template>
  <div class="hello">

      <h5>Nodo: {{node}}, {{plant}}</h5>
    <b-container fluid v-if="status">
      <b-row>

        <b-col lg="2" class="col">
          <h5>Temperatura</h5>
          <p>Actual: {{temperature}}ºC</p>
          <p>Promedio: {{tavg}}ºC</p>
          <p>Rango: {{tmin}}ºC ~ {{tmax}}ºC</p>
        </b-col>

        <b-col lg="2" class="col">
          <div class="cont" v-bind:style="{ backgroundColor: tColor}"></div>
        </b-col>

        <b-col lg="2" class="col">
          <h5>pH</h5>
          <p>Actual: {{ph}}</p>
          <p>Promedio: {{pavg}}</p>
          <p>Rango: {{pmin}} ~ {{pmax}}</p>
        </b-col>

        <b-col lg="2" class="col">
          <div class="cont" v-bind:style="{ backgroundColor: pColor}"></div>
        </b-col>

        <b-col lg="2" class="col">
          <h5>Humedad</h5>
          <p>Actual: {{humidity}}%</p>
          <p>Promedio: {{havg}}%</p>
          <p>Rango: {{hmin}}% ~ {{hmax}}%</p>
        </b-col>

        <b-col lg="2" class="col">
          <div class="cont" v-bind:style="{ backgroundColor: tColor}"></div>
        </b-col>

      </b-row>
    </b-container>

    <ChartLoader fluid v-if="!status" v-bind:node="node"></ChartLoader>
    <Button v-on:click="loadCharts">Gráficas semanales</Button>
  </div>
</template>

<script>
import axios from 'axios'
import URL from '../constants.js'
import ChartLoader from './ChartLoader.vue'

export default {
  name: 'DashboardRow',
  props: ['node'],
  components: {
    ChartLoader
  },
  data () {
      return {
        user: "usr1",
        plant: "Lechuga romana",
        temperature: 22,
        tmax: 27,
        tmin: 23,
        tavg: 25,
        tColor: 'red',
        ph: '0',
        pmax: 7.5,
        pmin: 6.6,
        pavg: 7.0,
        pColor: 'green',
        humidity: 70,
        hmax: 72,
        hmin: 68,
        havg: 71,
        hColor: 'green',
        status: true
      }
  },
  methods: {
    loadCharts () {
      this.status = this.status ^ true;
    }
  },
  mounted () {
    let body = this.user + ',' + this.node;

    axios
      .post(URL + '/api/data/current', body)
      .then(res => {
        this.ph = res.data[0][0];
        this.pmin = res.data[0][1];
        this.pmax = res.data[0][2];

        if (this.ph > this.pmin && this.ph < this.pmax) {
          this.pColor = 'green';
        } else {
          this.pColor = 'red';
        }

        this.temperature = res.data[0][3];
        this.tmin = res.data[0][4];
        this.tmax = res.data[0][5];

        if (this.temperature > this.tmin && this.temperature < this.tmax) {
          this.tColor = 'green';
        } else {
          this.tColor = 'red';
        }

        this.humidity = res.data[0][6];
        this.hmin = res.data[0][7];
        this.hmax = res.data[0][8];

        if (this.humidity > this.hmin && this.humidity < this.hmax) {
          this.hColor = 'green';
        } else {
          this.hColor = 'red';
        }

        this.plant = res.data[0][9];


      });


      axios
        .post(URL + '/api/data/year', body)
        .then(res => {
          this.pavg = res.data[0][0];
          this.tavg = res.data[0][1];
          this.havg = res.data[0][2];
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
      padding-top: 1em;
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

  button {
    margin: 1em;
    font-size: 1.1em;
    color: #262626;
    background-color: #02B392;
    border: 0px;
    padding: 0.5em;
    border-radius: 5px;
  }


  </style>
