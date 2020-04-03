<template>
  <div class="hello">
    <h3>Datos</h3>
    <p> {{ info }} </p>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Data',
  props: {
    msg: String
  },
  data () {
      return {
        info: null
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

h3 {
  margin: 1.5em;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
