<template>
  <div class="flex flex-row w-screen" v-bind:class="{'pl-96':navbarVisible}">
    <AppNavbar v-if="navbarVisible" :selected="selected" />
    <div class="w-full">
      <div class="flex flex-row w-full">
        <input type="text" v-if="navbarVisible" 
        placeholder="Search"
        v-model="searchTerm">
        <button v-if="navbarVisible" @click="showSearchResults">Search</button>
        <ProfilePreview v-if="navbarVisible"/>
      </div>
      
      <router-view class="w-full" 
        @show-navbar="showNavbar" @hide-navbar = "hideNavbar"
        @logout-possible = "logoutPossible = true" @logout-not-possible = "logoutPossible = false"
        @toggle-selected = "toggleSelected"/>
      <LogoutOverlay v-if="logout"/>
    </div>
  </div>
</template>

<script>
import AppNavbar from './components/AppNavbar'
import ProfilePreview from './components/ProfilePreview.vue'
import LogoutOverlay from './components/LogoutOverlay.vue'
export default {
  name: 'App',
  components: {
    AppNavbar,
    ProfilePreview,
    LogoutOverlay
},
  data: () => {
    return{
      navbarVisible : false,
      selected: "",
      logoutPossible: true,
      noCookie : false,
      searchTerm: "",
    }
  },
  computed: {
    logout(){
      return this.logoutPossible && this.noCookie
    }
  },
  methods: {
      showNavbar(){
        this.navbarVisible = true
      },
      hideNavbar(){
        this.navbarVisible = false
        this.searchTerm = ""
      },
      showSearchResults(){
        console.log("Searching for " + this.searchTerm)
      },
      toggleSelected(selected){
        if(selected === "grades"){
          this.selected = 'dashboard'
        }
        else if(selected === "finances"){
          this.selected = 'dashboard'
        }
        else if(selected === "profile"){
          this.selected = 'dashboard'
        }
        else{
          this.selected = selected
        }
      },
      resetAuth(){
        const token = this.$cookies.get('auth-token')
        if(token){
          this.$cookies.set('auth-token', token)
          return true;
        }
        else{
          return false;
        }
      },
      eventHandler(){
        if(!this.resetAuth()){
          this.noCookie = true
        }
        else{
          this.noCookie = false
        }
        //console.log(this.noCookie && this.logoutPossible)
      }
  },
  created(){
    
  },
  mounted(){
    document.addEventListener('click', this.eventHandler)
    document.addEventListener('keydown', this.eventHandler)
    document.addEventListener('mousemove', this.eventHandler)
  },
  beforeUnmount(){
    document.removeEventListener('click', this.eventHandler)
    document.removeEventListener('keydown', this.eventHandler)
    document.removeEventListener('mousemove', this.eventHandler)
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
