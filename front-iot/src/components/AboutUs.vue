<template>
  <div class="hello">
    <h2>Quienes Somos</h2>

    <b-container fluid>
      <b-row>
        <b-col lg="4">
          <div class="cont">
            <img alt="Choya logo" class="imgf" src="../assets/Fede.jpg">
          </div>
          <h3>Federico Ibarra</h3>
          <h5>Software Lead</h5>
        </b-col>

        <b-col lg="4">
          <div class="cont">
            <img alt="Choya logo" class="imgd" src="../assets/Diego.jpeg">
          </div>
          <h3>Diego Espinoza</h3>
          <h5>Experience Lead</h5>
        </b-col>

        <b-col lg="4">
          <div class="cont">
            <img alt="Choya logo" class="imgi" src="../assets/Isaac.jpeg">
          </div>
          <h3>Isaac Vázquez</h3>
          <h5>Hardware Lead</h5>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>

export default {
  name: 'AboutUs',
  data () {
      return {
        info: null
      }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h2 {
  padding: 2em 0 2em 0;
  color: #262626;
}

h3{
  padding: 2em 0 1em 0;
  color: #262626;
}

h5{
  padding: 0 0 6em 0;
  color: #262626;
}

.cont{
  width:15em; /*container-width*/
  height: 15em;
  border-radius: 50%;
  overflow:hidden; /*hide bounds of image */
  margin: auto;

}

.imgf{
  height: 100%;
  margin-left: -6em;
}

.imgd{
  width: 100%;
  margin-top: -2em;
  margin-left: -1em;
}

.imgi{
  width: 100%;
  margin-top: -4em;
  margin-left: 0em;
}
</style>
