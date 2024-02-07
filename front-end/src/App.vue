<template>
  <h1> Guys I really think we should keep this color scheme </h1>
  <h2> It looks really good and we will get 100% on the UX</h2>
  <AppNavbar v-if="navbarVisible"/>
  <ProfilePreview v-if="profileVisible"/>
  <input type="text" v-if="searchVisible" 
  placeholder="Search"
  v-model="searchTerm"
  >
  <button v-if="searchVisible" @click="showSearchResults">Search</button>
  <router-view  
    @show-navbar="showNavbar" @hide-navbar = "hideNavbar"
    @show-profile="showProfile" @hide-profile = "hideProfile"
    @show-search="showSearch" @hide-search = "hideSearch"
  />
</template>

<script>
import AppNavbar from './components/AppNavbar'
import ProfilePreview from './components/ProfilePreview.vue'
export default {
  name: 'App',
  components: {
    AppNavbar,
    ProfilePreview
  },
  data: () => {
    return{
      navbarVisible : false,
      profileVisible : false,
      searchVisible : false,
      searchTerm: ""
    }
  },
  methods: {
      showNavbar(){
        this.navbarVisible = true
      },
      hideNavbar(){
        this.navbarVisible = false
      },
      showProfile(){
        this.profileVisible = true
      },
      hideProfile(){
        this.profileVisible = false
      },
      showSearch(){
        this.searchVisible = true
      },
      hideSearch(){
        this.searchVisible = false
        this.searchTerm = ""
      },
      showSearchResults(){
        console.log("Searching for " + this.searchTerm)
      }
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
