<template>
  <div class="flex flex-row w-screen h-screen overflow-hidden shadow-inner bg-grey-100" v-bind:class="{'pl-96':navbarVisible}">
    <AppNavbar v-if="navbarVisible" :selected="selected" />
    <div class="w-full">
      <div v-if="navbarVisible" class="flex items-center justify-start py-4 px-4 bg-gray-200">
        <div class="flex items-center space-x-2 bg-white-100 rounded-lg shadow-md p-2 w-2/5 ml-5 h-11">
          <input type="text" class="flex-grow outline-none rounded-l-full px-4 py-2" @keydown="showSearchResults" placeholder="Search" v-model="searchTerm" />
          <button class="bg-transparent p-2 rounded-full text-gray-100 hover:text-gray-700 focus:outline-none" @click="showSearchResults">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 fill-grey-200" viewBox="0 0 50 50">
            <path d="M 21 3 C 11.621094 3 4 10.621094 4 20 C 4 29.378906 11.621094 37 21 37 C 24.710938 37 28.140625 35.804688 30.9375 33.78125 L 44.09375 46.90625 L 46.90625 44.09375 L 33.90625 31.0625 C 36.460938 28.085938 38 24.222656 38 20 C 38 10.621094 30.378906 3 21 3 Z M 21 5 C 29.296875 5 36 11.703125 36 20 C 36 28.296875 29.296875 35 21 35 C 12.703125 35 6 28.296875 6 20 C 6 11.703125 12.703125 5 21 5 Z"></path>
          </svg>
          </button>
        </div>
        <ProfilePreview class="ml-auto mr-5" />
      </div>

      <router-view
        class="w-full p-5"
        @show-navbar="showNavbar"
        @hide-navbar="hideNavbar"
        @logout-possible="logoutPossible = true"
        @logout-not-possible="logoutPossible = false"
        @toggle-selected="toggleSelected"
      />
      <LogoutOverlay v-if="logout" />
    </div>
  </div>
</template>

<script>
import Fuse from 'fuse.js';
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
      componentFuse: null,
      linkFuse: null,
      navbarVisible : false,
      selected: "",
      logoutPossible: true,
      noCookie : false,
      searchTerm: "",
      filteredComponents: [],
      filteredLinks: [],
      components:[
        {
          name: "Dashboard",
          terms: [
            "dashboard",
            "home",
            "main"
          ],
          target: "/dashboard"
        },
        {
          name: "Academics",
          terms: [
            "grades",
            "academics",
            "report",
            "requirements"
          ],
          target: "/academics"
        },
        {
          name: "Finances",
          terms: [
            "money",
            "finances",
            "report",
            "due"
          ],
          target: "/finances"
        },
        {
          name: "Grades",
          terms: [
            "grades",
            "academics",
            "gpa"
          ],
          target: "/grades"
        },
        {
          name: "Applications",
          terms: [
            "applications",
            "programs"
          ],
          target: "/application"
        },
        {
          name: "AroundU",
          terms: [
            "links",
            "aroundu",
            "misc"
          ],
          target: "/misc"
        },
        {
          name: "Profile",
          terms: [
            "settings",
            "profile",
            "account"
          ],
          target: "/profile"
        },
        {
          name: "Schedule Builder",
          terms: [
            "schedule",
            "calendar",
            "classes"
          ],
          target: "/schedule"
        }
      ],
      links: [
        {
          name: "Events at UCalgary" ,
          section: "Get Involved",
          target: "https://events.ucalgary.ca"
        },
        {
          name: "Dinos Athletics" ,
          section: "Get Involved",
          target: "https://godinos.com/"
        },
        {
          name: "Active Living Centre" ,
          section: "Get Involved",
          target: "https://active-living.ucalgary.ca/"
        },
        {
          name: "ClubHub: Clubs & Organisations" ,
          section: "Get Involved",
          target: "https://suuofc.campuslabs.ca/engage/organizations"
        },
        {
          name: "Continuing Education" ,
          section: "Get Involved",
          target: "https://conted.ucalgary.ca/index.jsp"
        },
        {
          name: "University of Calgary: International" ,
          section: "Get Involved",
          target: "http://www.ucalgary.ca/international/"
        },
        {
          name: "Students' Union: Volunteer Programs" ,
          section: "Get Involved",
          target: "http://www.su.ucalgary.ca/page/quality-student-life/volunteer-services/volunteer-programs"
        },
        {
          name: "Donate" ,
          section: "Get Involved",
          target: "http://netcommunity.ucalgary.ca/Page.aspx?pid=518&srcid=486"
        },
        {
          name: "Find a Faculty" ,
          section: "Get Around",
          target: "http://contacts.ucalgary.ca/directory/faculties"
        },
        {
          name: "Find a Building/Room" ,
          section: "Get Around",
          target: "http://www.ucalgary.ca/map"
        },
        {
          name: "Find a Library" ,
          section: "Get Around",
          target: "http://library.ucalgary.ca/"
        },
        {
          name: "Campus Food Services" ,
          section: "Get Around",
          target: "http://www.ucalgary.ca/ancillary/food-services"
        },
        {
          name: "Sustainable Transportation" ,
          section: "Get Around",
          target: "https://www.ucalgary.ca/sustainability/our-sustainable-campus/transportation"
        },
        {
          name: "Parking on Campus" ,
          section: "Get Around",
          target: "http://www.ucalgary.ca/parking"
        },
        {
          name: "Accessibility Services" ,
          section: "Get Around",
          target: "http://www.ucalgary.ca/access"
        },
        {
          name: "Workroom Booking" ,
          section: "Help & Support",
          target: "http://workrooms.ucalgary.ca/"
        },
        {
          name: "UService" ,
          section: "Help & Support",
          target: "https://www.ucalgary.ca/uservice"
        },
        {
          name: "IT Services" ,
          section: "Help & Support",
          target: "http://www.ucalgary.ca/it/help"
        },
        {
          name: "Audio/Visual Support" ,
          section: "Help & Support",
          target: "https://ucalgary.service-now.com/it?id=it_catalog_by_category&sys_id=373facbc13deea4053f2d7b2e144b00c"
        },
        {
          name: "Printing Services" ,
          section: "Help & Support",
          target: "http://www.ucalgary.ca/printshop/"
        },
        {
          name: "Student Services" ,
          section: "Help & Support",
          target: "http://www.ucalgary.ca/ses"
        },
        {
          name: "UCalgary Webmail" ,
          section: "Get Connected",
          target: "http://office365.ucalgary.ca/"
        },
        {
          name: "Contacts Directory" ,
          section: "Get Connected",
          target: "http://contacts.ucalgary.ca/"
        },
        {
          name: "UCalgary Social Media" ,
          section: "Get Connected",
          target: "http://contacts.ucalgary.ca/directory/socialmedia"
        },
        {
          name: "Students' Union" ,
          section: "Get Connected",
          target: "http://www.su.ucalgary.ca/"
        },
        {
          name: "Grad Students' Association" ,
          section: "Get Connected",
          target: "http://gsa.ucalgary.ca/"
        },
        {
          name: "Book Space" ,
          section: "Welcome Guests",
          target: "http://www.ucalgary.ca/mse"
        },
        {
          name: "Give Directions" ,
          section: "Welcome Guests",
          target: "https://www.ucalgary.ca/about/our-campuses/campus-maps-and-room-finder"
        },
        {
          name: "Arrange Parking" ,
          section: "Welcome Guests",
          target: "https://www.ucalgary.ca/ancillary/parking"
        },
        {
          name: "Book a Campus Tour" ,
          section: "Welcome Guests",
          target: "https://choose.ucalgary.ca/events/campusVisitRequest.do"
        },
        {
          name: "Pickup a Souvenir/Gift" ,
          section: "Welcome Guests",
          target: "https://shop.ucalgary.ca/"
        },
        {
          name: "Visit Libraries/Museums" ,
          section: "Welcome Guests",
          target: "https://library.ucalgary.ca/"
        },
        {
          name: "Discover Calgary" ,
          section: "Welcome Guests",
          target: "http://www.visitcalgary.com/"
        },
        {
          name: "Discover Alberta" ,
          section: "Welcome Guests",
          target: "http://travelalberta.com/"
        },
        {
          name: "UC Safety App" ,
          section: "Stay Safe",
          target: "https://ucalgary.ca/risk/emergency-management/emergency-communication/uc-emergency-mobile"
        },
        {
          name: "Accident Report (OARS)" ,
          section: "Stay Safe",
          target: "https://ucalgary.chematix.com/Oars"
        },
        {
          name: "Contact Campus Security" ,
          section: "Stay Safe",
          target: "http://www.ucalgary.ca/security"
        },
        {
          name: "Be Safe Working Alone" ,
          section: "Stay Safe",
          target: "https://live-risk.ucalgary.ca/risk/environment-health-safety/programs-standards-cops/working-alone"
        },
        {
          name: "Request Safe Walk" ,
          section: "Stay Safe",
          target: "http://www.ucalgary.ca/security/safewalk"
        },
        {
          name: "Environment, Health, Safety" ,
          section: "Stay Safe",
          target: "http://www.ucalgary.ca/safety/"
        },
        {
          name: "Chematix" ,
          section: "Stay Safe",
          target: "https://ucalgary.chematix.com/Chematix"
        },
      ]
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
        this.filteredComponents = this.componentFuse.search(this.searchTerm)
        this.filteredLinks = this.linkFuse.search(this.searchTerm)
        console.log(this.filteredComponents)
        console.log(this.filteredLinks)
      },
      toggleSelected(selected){
        this.selected = selected
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
      }
  },
  created(){
    this.componentFuse = new Fuse(this.components, {keys:['terms']})
    this.linkFuse = new Fuse(this.links, {keys:['name', 'section']})
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
