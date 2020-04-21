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
            <Chart class="chart" v-bind:charoptions="this.option" v-bind:chardata="this.temp"></Chart>
            <Chart class="chart" v-bind:charoptions="this.option" v-bind:chardata="this.ph"></Chart>
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
        allData: [
          ["Mock 17", 7, 22, 22, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          ["Mock 5", 7, 22, 19, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          ["Mock 1", 7, 22, 18, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          ["Mock 10", 7, 22, 20, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          ["Mock 13", 7, 22, 21, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"]
        ],
        items: [],
        temp: {
          //Data to be represented on x-axis
          labels: ['Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab', 'Dom'],
          datasets: [
            {
              label: 'Temperatura',
              backgroundColor: '#02B392',
              pointBackgroundColor: '#016653',
              borderWidth: 1,
              pointBorderColor: '#249EBF',
              //Data to be represented on y-axis
              data: [20, 21, 17, 21, 24, 22, 22]
            }
          ]
        },
        ph: {
          //Data to be represented on x-axis
          labels: ['Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab', 'Dom'],
          datasets: [
            {
              label: 'pH',
              backgroundColor: '#02B392',
              pointBackgroundColor: '#016653',
              borderWidth: 1,
              pointBorderColor: '#249EBF',
              //Data to be represented on y-axis
              data: [7, 7.2, 7.1, 6.9, 7, 7.2, 6.8]
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
  mounted () {
    axios
      .get(URL + '/api/data/all')
      .then(response => (this.allData = response))

    console.log("All data: " + this.allData);

    const row = {
      Dispositivo: 'Mock 1', Fecha: '01/01/2020', Temperatura: '20', ph: 7.0
    }

    this.allData.forEach(e => {
        let newRow = Object.create(row);

        newRow.Dispositivo = e[0];
        newRow.Fecha = e[3] + '/' + e[4] + '/' +e[5];
        newRow.Temperatura = e[2];
        newRow.ph = e[1];

        console.log(newRow);
        this.items.push(newRow);
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
  margin: auto;
  width: 70%;
}

.tab {
  display: block;
  margin: auto;
  width: 100%;
}

</style>
