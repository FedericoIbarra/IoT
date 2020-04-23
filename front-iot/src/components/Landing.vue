<template>
  <div class="hello">
    <b-container fluid>
      <b-row>
        <b-col class="cont" lg="6">
          <img alt="Choya logo" class="imgp" src="../assets/img1.jpg">
        </b-col>
        <b-col lg="6">
          <div class="txt">
            <h4 class="h41">Ayudando a restaurantes a cultivar sus propios vegetales con un sistema de bajo mantenimiento</h4>
            <p>Nuestros sistemas hidrológicos requieren un uso mínimo de energía eléctrica y agua para funcionar lo que los hace ideales para restaurantes de todo tipo. Con dicho sistema cualquier restaurante puede tener su propio huerto sin necesidad de contar con gran cantidad de espacio</p>
            <router-link to="/" class="reg">Registrarse</router-link>
          </div>
        </b-col>
      </b-row>

      <b-row >
        <b-col class="cont secrow" lg="6">
          <h4 class="h42">Ventajas de la hidroponia</h4>
          <ul id="example-1">
            <li v-for="perk in perks" v-bind:key="perk">
              <div style="float: left;">
                  <img src="../assets/Choya2.png" class="checkmark">
              </div>
              <div style="float: left;">
                  <p style="color: #F2F2F2;">{{perk.str}}</p>
              </div>
              <div style="float: none; clear: both;"></div>
            </li>
          </ul>
        </b-col>
        <b-col class="cont secrow" lg="6">
          <img alt="Choya logo" class="imgp" src="../assets/img2.jpg">
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>

export default {
  name: 'Landing',
  data () {
      return {
        perks: [
          { str: 'Requiere menos nutrientes' },
          { str: 'Requiere menor espacio' },
          { str: 'Uso eficiente de agua' },
          { str: 'Bajo mantenimiento' },
          { str: 'Más limpio' }
        ]
      }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.txt {
  width: 85%;
  max-height: 10%;
  margin: 5em auto;
}
.h41{
  color: #016653;
}

.h42 {
  margin: 10% 0 -10% 0;
  color: #02B392;
}

ul {
  list-style-type: none;
  margin: 20% auto 15% auto;
  width: inherit;
}
li {
  margin-top: 2%;
}

.imgp {
  max-height: 20em;
  max-width: 80%;
  margin: 10%;
}


.checkmark{
  height: 2em;
  margin-right: 2em;
}

.secrow{
  background-color: #262626;
}

.reg {
  font-size: 1.3em;
  color: #02B392;
  font-weight: bold;
}

.reg:hover {
  color: #016653;
  text-decoration: none;
}
</style>
