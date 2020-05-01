<template>
  <div class="hello">
    <h3>Estas son todas las lecturas de tus nodos</h3>
    <b-table class="tab" responsive striped hover :items="items"></b-table>
    <p></p>
    <a href="#">Descargar datos</a>
  </div>
</template>

<script>
import axios from 'axios'
import URL from '../constants.js'

export default {
  name: 'Data',
  data () {
      return {
        user: "usr1",
        node: "Mock 1",
        info: null,
        fetched: false,
        allData: [
          [ "Mock 1", "Choya", 7, 22, 70, 18, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          [ "Mock 10", "Choya", 7, 22, 70, 20, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          [ "Mock 11", "Choya", 7, 22, 70, 20, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          [ "Mock 12", "Choya", 7, 22, 70, 20, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          [ "Mock 13", "Choya", 7, 22, 70, 21, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          [ "Mock 14", "Choya", 7, 22, 70, 21, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          [ "Mock 15", "Choya", 7, 22, 70, 21, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          [ "Mock 16", "Choya", 7, 22, 70, 21, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          [ "Mock 17", "Choya", 7, 22, 70, 22, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          [ "Mock 18", "Choya", 7, 22, 70, 22, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          [ "Mock 19", "Choya", 7, 22, 70, 22, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          [ "Mock 2", "Choya", 7, 22, 70, 18, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          [ "Mock 20", "Choya", 7, 22, 70, 22, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          [ "Mock 3", "Choya", 7, 22, 70, 18, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          [ "Mock 4", "Choya", 7, 22, 70, 18, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          [ "Mock 5", "Choya", 7, 22, 70, 19, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          [ "Mock 6", "Choya", 7, 22, 70, 19, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          [ "Mock 7", "Choya", 7, 22, 70, 19, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          [ "Mock 8", "Choya", 7, 22, 70, 19, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          [ "Mock 9", "Choya", 7, 22, 70, 20, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"]
        ],
        weekData: [
          ["Mock 0", "Choya", 7, 22, 70, 18, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          ["Mock 0", "Choya", 7, 22, 70, 19, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          ["Mock 0", "Choya", 7, 22, 70, 20, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          ["Mock 0", "Choya", 7, 22, 70, 21, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"],
          ["Mock 0", "Choya", 7, 22, 70, 22, 4, 2020, "Thu, 01 Jan 1970 00:00:01 GMT"]
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
    this.user = sessionStorage.getItem('usr');
    this.node = sessionStorage.getItem('usrNodes');

    let body = this.user + ',' + this.node;
    //Table setup
    const row = {
      Dispositivo: 'Mock 1',
      Planta: 'Choya',
      Fecha: '01/01/2020',
      Temperatura: '20',
      ph: 7.0,
      Humedad: 70
    }
    /*
    axios
      .post(URL + '/api/data/all', body)
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
      */

      axios
        .post(URL + '/api/data/all', body)
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

      this.allData.forEach(e => {
          let newRow = Object.create(row);
          newRow.Dispositivo = e[0];
          newRow.planta = e[1];
          newRow.Fecha = e[5] + '/' + e[6] + '/' +e[7];
          newRow.Temperatura = e[2] + 'ºC';
          newRow.ph = e[3];
          newRow.humedad = e[4] + '%';
          this.items.push(newRow);
      });
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

h3{
    margin: 1em;
    padding-top: 1em;
}

a {
  background-color: #02B392;
  color: #262626;
  font-weight: bold;
  padding: 0.7em;
  border-radius: 7px;
}

a:hover{
  text-decoration: none;
}

.tab {
  display: block;
  margin: auto;
  padding: 1em;
  width: 90%;
}

.hello{
  padding-bottom: 3em;
}

</style>
