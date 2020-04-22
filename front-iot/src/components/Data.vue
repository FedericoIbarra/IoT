<template>
  <div class="hello">
    <h3>Datos de la última semana</h3>
    <b-container fluid>
      <b-row>
        <b-col class="cont" lg="6">
          <b-table class="tab" responsive striped hover :items="items"></b-table>
        </b-col>
        <b-col lg="6">
          <b-row>
            <Chart v-if="fetched" class="chart" v-bind:charoptions="this.option" v-bind:chardata="this.temp"></Chart>
            <Chart v-if="fetched" class="chart" v-bind:charoptions="this.option" v-bind:chardata="this.ph"></Chart>
          </b-row>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import axios from 'axios'
import Chart from './Chart.vue'
import URL from '../constants.js'

export default {
  name: 'Data',
  components: {
    Chart
  },
  props: {
    msg: String
  },
  data () {
      return {
        info: null,
	fetched: false,
        allData: [
          [ "Mock 1", 7, 22, 18, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          [ "Mock 10", 7, 22, 20, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          [ "Mock 11", 7, 22, 20, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          [ "Mock 12", 7, 22, 20, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          [ "Mock 13", 7, 22, 21, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          [ "Mock 14", 7, 22, 21, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          [ "Mock 15", 7, 22, 21, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          [ "Mock 16", 7, 22, 21, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          [ "Mock 17", 7, 22, 22, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          [ "Mock 18", 7, 22, 22, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          [ "Mock 19", 7, 22, 22, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          [ "Mock 2", 7, 22, 18, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          [ "Mock 20", 7, 22, 22, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          [ "Mock 3", 7, 22, 18, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          [ "Mock 4", 7, 22, 18, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          [ "Mock 5", 7, 22, 19, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          [ "Mock 6", 7, 22, 19, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          [ "Mock 7", 7, 22, 19, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          [ "Mock 8", 7, 22, 19, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          [ "Mock 9", 7, 22, 20, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"]
        ],
        weekData: [
          ["Mock 0", 7, 22, 18, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          ["Mock 0", 7, 22, 19, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          ["Mock 0", 7, 22, 20, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          ["Mock 0", 7, 22, 21, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          ["Mock 0", 7, 22, 22, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"]
        ],
        items: [],
        temp: {
          //Data to be represented on x-axis
          labels: [],
          datasets: [
            {
              label: 'Temperatura',
              backgroundColor: '#02B392',
              pointBackgroundColor: '#016653',
              borderWidth: 1,
              pointBorderColor: '#249EBF',
              //Data to be represented on y-axis
              data: []
            }
          ]
        },
        ph: {
          //Data to be represented on x-axis
          labels: [],
          datasets: [
            {
              label: 'pH',
              backgroundColor: '#02B392',
              pointBackgroundColor: '#016653',
              borderWidth: 1,
              pointBorderColor: '#249EBF',
              //Data to be represented on y-axis
              data: []
            }
          ]
        },
        options: {
          scales: {
            yAxes: [{
              ticks: {
                beginAtZero: true
              },
              gridLines: {
                display: true
              }
            }],
            xAxes: [ {
              gridLines: {
                display: false
              }
            }]
          },
          legend: {
            display: true
          },
          responsive: true,
          maintainAspectRatio: true
        }
      }
  },
  created () {

    //Table setup
    const row = {
      Dispositivo: 'Mock 1', Fecha: '01/01/2020', Temperatura: '20', ph: 7.0
    }
    axios
      .get(URL + '/api/data/all')
      .then(response => {
        this.allData = response.data
        this.items = [];

        this.allData.forEach(e => {
            let newRow = Object.create(row);

            newRow.Dispositivo = e[0];
            newRow.Fecha = e[3] + '/' + e[4] + '/' +e[5];
            newRow.Temperatura = e[2];
            newRow.ph = e[1];
            this.items.push(newRow);
        });

      });

    //Charts setup
    axios
      .get(URL + '/api/data/week')
      .then(response => {
        this.weekData = response.data;

        this.weekData.forEach(e => {
          this.temp.labels.push(e[3] + '/' + e[4]);
          this.temp.datasets[0].data.push(e[2]);

          this.ph.labels.push(e[3] + '/' + e[4]);
          this.ph.datasets[0].data.push(e[1]);
        });

	this.fetched = true;
      });




  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

h3{
    margin: 2em;
    padding-top: 1em;
}

.hello{
    min-height: 19em;
}

.chart{
  display: block;
  margin: 2em auto 3em auto;
  width: 70%;
}

.tab {
  display: block;
  margin: auto;
  padding-bottom: 1em;
  width: 100%;
}

</style>
