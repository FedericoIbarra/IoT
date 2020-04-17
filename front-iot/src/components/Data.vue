<template>
  <div class="hello">
    <h3>Aquí van los Datos</h3>

    <b-container fluid>
      <b-row>
        <b-col class="cont" lg="6">
          <b-table responsive striped hover :items="items"></b-table>
        </b-col>
        <b-col lg="6">
          <Chart></Chart>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import axios from 'axios'
import Chart from './Chart.vue'

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
        items: [
          { Dispositivo: 40, Fecha: 'Dickerson', Temperatura: 'Macdonald', ph: 7.0 },
          { Dispositivo: 21, Fecha: 'Larsen', Temperatura: 'Shaw', ph: 7.0 },
          { Dispositivo: 89, Fecha: 'Geneva', Temperatura: 'Wilson', ph: 7.0 },
          { Dispositivo: 38, Fecha: 'Jami', Temperatura: 'Carney', ph: 7.0 }
        ]
      }
  },
  mounted () {
    axios
      .get('http://54.175.166.57:5000/api')
      .then(response => (this.info = response))
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.hello{
    min-height: 19em;
}

</style>
