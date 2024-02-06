<template>
  <h1> Guys I really think we should keep this color scheme </h1>
  <h2> It looks really good and we will get 100% on the UX</h2>
  <AppNavbar v-if="navbarVisible"/>
  <router-view  @show-navbar="showNavbar" @hide-navbar = "hideNavbar"/>
</template>

<script>
import AppNavbar from './components/AppNavbar'

export default {
  name: 'App',
  components: {
    AppNavbar
  },
  data: () => {
    return{
      navbarVisible : false,
    }
  },
  methods: {
      showNavbar(){
        this.navbarVisible = true
      },
      hideNavbar(){
        this.navbarVisible = false
      },
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
