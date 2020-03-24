<template>
  <div class="hello">
    <h1>Equipo 5</h1>
    <h3>Front-End</h3>
    <p> {{ info }} </p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'HelloWorld',
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
  margin: 40px 0 0;
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
