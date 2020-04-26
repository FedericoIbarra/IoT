<template>
  <div class="hello">
    <Chart v-if="fetched" class="chart" v-bind:charoptions="this.option" v-bind:chardata="this.temp"></Chart>
    <Chart v-if="fetched" class="chart" v-bind:charoptions="this.option" v-bind:chardata="this.ph"></Chart>
  </div>
</template>

<script>
import axios from 'axios'
import Chart from './Chart.vue'
import URL from '../constants.js'

export default {
  name: 'ChartLoader',
  components: {
    Chart
  },
  props: {
    msg: String
  },
  data () {
      return {
        user: "usr1",
        node: "Mock 1",
        info: null,
        fetched: false,
        weekData: [
          ["Mock 0", "Choya", 7, 22, 70, 18, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          ["Mock 0", "Choya", 7, 22, 70, 19, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          ["Mock 0", "Choya", 7, 22, 70, 20, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          ["Mock 0", "Choya", 7, 22, 70, 21, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          ["Mock 0", "Choya", 7, 22, 70, 22, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"]
        ],
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
    let body = this.user + ',' + this.node;

    //Charts setup
    axios
      .post(URL + '/api/data/week', body)
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

a{

}

.tab {
  display: block;
  margin: auto;
  padding: 1em;
  width: 90%;
}

</style>
