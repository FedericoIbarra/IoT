<script>
  //Importing Line class from the vue-chartjs wrapper
  import { Line } from 'vue-chartjs'

  //Exporting this so it can be used in other components
  export default {
    extends: Line,
    props: ['chardata', 'charoptions'],

    mounted () {
      //renderChart function renders the chart with the datacollection and options object.
      this.renderChart(this.chardata, this.charoptions)
    }
  }
</script>
