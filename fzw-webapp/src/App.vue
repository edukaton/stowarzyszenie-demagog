<template>
  <div id="app">
    <transition name="fade">
      <router-view></router-view>
    </transition>
  </div>
</template>

<script>
export default {
  name: 'app',
  mounted () {
    if (navigator.userAgent.indexOf('Chrome') !== -1) {
      this.calcVH()
      window.addEventListener('onorientationchange', this.calcVH);
    }
    document.querySelector('body').setAttribute('style', 'font-size:' + document.documentElement.clientHeight * 0.04 + 'px;');
  },
  methods: {
    calcVH () {
      var vH = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);
      document.querySelector('#app').setAttribute('style', 'height:' + vH + 'px;');
      // document.querySelector('#app > div').setAttribute('style', 'height:' + vH + 'px;');
    }
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Montserrat:300,400,700&subset=latin-ext');

:root {
  --color-orange: #EF420C;
  --color-blue: #0A264F;
  --color-gray: #B8B8B8;
  --color-lgray: #F3F3F3;
  --color-white: #FFFFFF;
}
html, option, input {
  font-family: 'Montserrat', sans-serif;
  color: var(--color-blue);
  user-select: none;
}
body {
  position: fixed;
  /* font-size: 4vh; */
  margin: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  width: 100%;
  background: black;
  overflow: hidden;
}
h2, h3, h4, h5, p {
  margin-top: 0;
}
h1 {
  font-size: 150%;
  font-weight: bold;
}
h2 {
  font-size: 120%;
  font-weight: light;
}
h3 {
  font-size: 110%;
  font-weight: light;
}
h4 {
  font-size: 90%;
  font-weight: bold;
  text-transform: uppercase;
}
p {
  font-weight: lighter;
}
#logo {
  height: 20%;
}
#logo.land {
  height: 40%;
}
#app {
  border-radius: 1vh;
  background: white;
  width: 100%;
  position: absolute;
  top: 0;
  height: 100%;
  display: flex;
  justify-content: space-around;
}
#app > div {
  position: absolute;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  text-align: center;
  height: 100%;
  width: 100%;
  box-sizing: border-box;
  padding: 0 5%;
}
@media screen and (min-device-aspect-ratio: 1/1) {
  #app {
    width: calc(100vh/16*10);
  }
}
button {
  border: none;
  margin:  4vh 0;
  padding: 3vh 10vh;
  text-transform: uppercase;
  font-weight: 900;
  cursor: pointer;
  color: var(--color-white);
  text-decoration: none;
  border-radius: 1.5vh;
  font-size: 65%;
  letter-spacing: 0.1em;
}
button:focus {
  outline:0;
}
.main-cta{
  background: var(--color-orange);
  box-shadow: 0 1vh 2vh rgba(239, 16, 22, .6);
}
.main-cta:hover{
  background: #E63F0C;
}
.secondary-cta{
  background: var(--color-blue);
  box-shadow: 0 1vh 2vh rgba(10, 38, 79, .5);
}
.secondary-cta:hover{
  background: var(--color-blue);
}
.ghost-cta{
  background: var(--color-white);
  color: var(--color-blue);
  box-shadow: 0 0 0 1vh var(--color-blue) inset;
}
.ghost-cta:hover{
  background: #E63F0C;
  border-radius: 2.5vh;
  text-decoration: none;
}
.input{
  display: flex;
  align-items: flex-start;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}
.radio{
  display: flex;
  font-size: inherit;
}
input{
  font-family: 'Montserrat', sans-serif;
  border: none;
  box-sizing: border-box;
  text-align: center;
  padding: 3vh;
  font-size: 120%;
  font-weight: bold;
  color: inherit;
}
input[type='text'], input[type='number']{
  width: 100%;
}

.card{
  background: white;
  height: 55vh;
  width: 100%;
  box-shadow: 0 1vh 2vh rgba(10, 38, 79, 1);
  border-radius: 2.5vh;
  overflow-y: auto;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity .2s;
}
.fade-enter-active {
  /* transition-delay: .5s; */
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
</style>
