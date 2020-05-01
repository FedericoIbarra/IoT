<template>
  <div class="hello">
    <h3>Estatus actual de {{user}}</h3>
    <DashboardRow
      class="row"
      v-for="node in nodes"
      v-bind:key="node"
      v-bind:node="node">
    </DashboardRow>
  </div>
</template>

<script>
import URL from '../constants.js'
import axios from 'axios'
import DashboardRow from './DashboardRow.vue'

export default {
  name: 'Dashboard',
  props: {
    msg: String
  },
  components: {
    DashboardRow
  },
  data () {
      return {
        user: '',
        nodes: []
      }
  },
  mounted () {
    this.user = sessionStorage.getItem('usr');

    let body = this.user;

    axios
      .post(URL + '/api/nodes', body)
      .then(res => {
        this.nodes = [];
        res.data.forEach(e => this.nodes.push(e[0]));
      });

    /*For local debuggin only
    this.nodes = ['Mock 1', 'Mock 2', 'Mock 1', 'Mock 2', 'Mock 1', 'Mock 2']
    */
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

  .row{
    display: block;
    margin: auto;
    min-width: 23em;
  }

  .row:nth-of-type(2n-1){
    background-color: #EAF2E6;
  }

  </style>
