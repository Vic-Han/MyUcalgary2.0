<template>
  <div class = "flex flex-row">
    <AppNavbar v-if="navbarVisible"/>
    <div>
      <div class = "flex flex-row">
        <input type="text" v-if="searchVisible" 
        placeholder="Search"
        v-model="searchTerm">
        <button v-if="searchVisible" @click="showSearchResults">Search</button>
        <ProfilePreview v-if="profileVisible"/>

      </div>
      
      <router-view  
        @show-navbar="showNavbar" @hide-navbar = "hideNavbar"
        @show-profile="showProfile" @hide-profile = "hideProfile"
        @show-search="showSearch" @hide-search = "hideSearch"
        @logout-possible = "logoutPossible = true" @logout-not-possible = "logoutPossible = false"
      />
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
      profileVisible : false,
      searchVisible : false,
      logoutPossible: true,
      noCookie : false,
      searchTerm: ""
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
