<template>
  <div class="flex flex-col w-96 bg-white-100 z-20 rounded-lg shadow-md fixed inset-0 h-screen p-8"> <!-- Added shadow effect -->
    <a href="https://www.ucalgary.ca/" target="_blank">
      <img  src="@/assets/unilogo.png" alt="University Logo" class="h-24 my-4 self-center">
    </a>
    
    <div class="flex flex-col mt-4 space-y-4"> <!-- Increased vertical spacing -->
      <!-- Updated class name to nav-link -->
      <router-link to="/dashboard" class="group flex flex-row items-center p-4 
      border border-white-300 shadow-md mt-4 rounded-xl text-black-100 hover:bg-grey-100" v-bind:class="{'bg-red-100 text-white-100 hover:bg-red-100' : selected === 'dashboard'}">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 mx-8" v-bind:class="{'fill-white-100' : selected === 'dashboard'}" viewBox="0 -960 960 960">
          <path d="M160-120v-480l320-240 320 240v480H560v-280H400v280H160Z"/>
        </svg>
        <span class="text-2xl">Dashboard</span>
      </router-link>

      <router-link to="/finances" class="group flex flex-row items-center p-4 border border-white-300 shadow-md mt-4 rounded-xl hover:bg-grey-100"
      v-bind:class="{'bg-red-100 text-white-100 hover:bg-red-100' : selected === 'finances'}">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 mx-8" v-bind:class="{'fill-white-100' : selected === 'finances'}" viewBox="0 -960 960 960">
          <path d="M444-200h70v-50q50-9 86-39t36-89q0-42-24-77t-96-61q-60-20-83-35t-23-41q0-26 18.5-41t53.5-15q32 0 50 15.5t26 38.5l64-26q-11-35-40.5-61T516-710v-50h-70v50q-50 11-78 44t-28 74q0 47 27.5 76t86.5 50q63 23 87.5 41t24.5 47q0 33-23.5 48.5T486-314q-33 0-58.5-20.5T390-396l-66 26q14 48 43.5 77.5T444-252v52Zm36 120q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Z"/>
        </svg>
        <span class="text-2xl group-hover:text-white focus:text-white">Finances</span>
      </router-link>

      <router-link to="/grades" class="group flex flex-row items-center p-4 border border-white-300 shadow-md mt-4 rounded-xl hover:bg-grey-100"
      v-bind:class="{'bg-red-100 text-white-100 hover:bg-red-100' : selected === 'grades'}">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 mx-8" v-bind:class="{'fill-white-100' : selected === 'grades'}" viewBox="0 -960 960 960">
          <path d="m40-200 210-560h100l210 560h-96l-51-143H187l-51 143H40Zm176-224h168l-82-232h-4l-82 232Zm504 104v-120H600v-80h120v-120h80v120h120v80H800v120h-80Z"/>
        </svg>
        <span class="text-2xl group-hover:text-white focus:text-white">Grades</span>
      </router-link>
      
      <router-link to="/academics" class="group flex flex-row items-center p-4 
      border border-white-300 shadow-md mt-4 rounded-xl hover:bg-grey-100" v-bind:class="{'bg-red-100 text-white-100 hover:bg-red-100'  : selected === 'academics'}">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 mx-8" v-bind:class="{'fill-white-100' : selected === 'academics'}" viewBox="0 -960 960 960">
          <path d="M840-280v-276L480-360 40-600l440-240 440 240v320h-80ZM480-120 200-272v-200l280 152 280-152v200L480-120Z"/>
        </svg>
        <span class="text-2xl group-hover:text-white focus:text-white">Academics</span>
      </router-link>
      
      <router-link to="/application" class="group flex flex-row items-center p-4 border border-white-300 shadow-md mt-4 rounded-xl hover:bg-grey-100"
      v-bind:class="{'bg-red-100 text-white-100 hover:bg-red-100' : selected === 'application'}">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 mx-8" v-bind:class="{'fill-white-100' : selected === 'application'}" viewBox="0 -960 960 960">
          <path d="M400-400h160v-80H400v80Zm0-120h320v-80H400v80Zm0-120h320v-80H400v80Zm-80 400q-33 0-56.5-23.5T240-320v-480q0-33 23.5-56.5T320-880h480q33 0 56.5 23.5T880-800v480q0 33-23.5 56.5T800-240H320ZM160-80q-33 0-56.5-23.5T80-160v-560h80v560h560v80H160Z"/>
        </svg>
        <span class="text-2xl group-hover:text-white focus:text-white">Applications</span>
      </router-link>
      
      <router-link to="/misc" class="group flex flex-row items-center p-4 border border-white-300 shadow-md mt-4 rounded-xl hover:bg-grey-100"
      v-bind:class="{'bg-red-100 text-white-100 hover:bg-red-100' : selected === 'misc'}">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 mx-8" v-bind:class="{'fill-white-100' : selected === 'misc'}" viewBox="0 -960 960 960">
          <path d="M200-280v-280h80v280h-80Zm240 0v-280h80v280h-80ZM80-120v-80h800v80H80Zm600-160v-280h80v280h-80ZM80-640v-80l400-200 400 200v80H80Z"/>
        </svg>
        <span class="text-2xl group-hover:text-white focus:text-white">Around U</span>
      </router-link>
    </div>
    
    <div class="mt-auto flex justify-between w-full p-10"> 
      <div class="flex flex-col">
        <div v-if="viewInfo" class="absolute -translate-x-1/3 -translate-y-36 h-32 w-40 bg-white-100 border border-white-300  shadow-lg rounded-lg">
          <div class="font-semibold">Contact IT</div>
          <div class="flex flex-row">
            <div class="text-sm mr-1 w-1/4 text-right text-grey-200">P:</div>
           <div class="text-sm text-grey-200">(403)-210-9300</div>
          </div>
          <div class="flex flex-row pb-5">
            <div class="text-sm mr-1 w-1/4 text-right text-grey-200">E:</div>
           <a href="mailto:it@ucalgary.ca" class="text-sm hover:underline text-grey-200">it@ucalgary.ca</a>
          </div>
          <a href="https://github.com/Vic-Han/SENG-401-Project/graphs/contributors" class="text-xs hover:underline text-grey-200">&copy; OhMyUCalgary</a>
          <div class="text-xs text-grey-200"> All rights Reserved.</div>
        </div>
        <svg xmlns="http://www.w3.org/2000/svg" @click="viewInfo = !viewInfo" class="h-10 w-10 fill-grey-200 hover:fill-red-100 cursor-pointer" viewBox="0 -960 960 960">
          <path d="M440-280h80v-240h-80v240Zm40-320q17 0 28.5-11.5T520-640q0-17-11.5-28.5T480-680q-17 0-28.5 11.5T440-640q0 17 11.5 28.5T480-600Zm0 520q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Zm0-80q134 0 227-93t93-227q0-134-93-227t-227-93q-134 0-227 93t-93 227q0 134 93 227t227 93Zm0-320Z"/>
          <title>Info</title>
        </svg>
      </div>
      <div class="has-tooltip">
        <svg xmlns="http://www.w3.org/2000/svg" @click="logout" class="h-10 w-10 fill-grey-200 hover:fill-red-100 cursor-pointer" viewBox="0 -960 960 960">
          <path d="M200-120q-33 0-56.5-23.5T120-200v-560q0-33 23.5-56.5T200-840h280v80H200v560h280v80H200Zm440-160-55-58 102-102H360v-80h327L585-622l55-58 200 200-200 200Z"/>
          <title>Logout</title>
        </svg>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AppNavbar',
  props: ['selected'],
  computed  : {
    selectedLink(link){
      return this.selected === link
    }
  },
  data() {
      return {
        viewInfo: false
      }
    },
  methods: {
    logout(){
      this.$cookies.remove('auth-token')
      this.$router.push('/')
    }
  }
}
</script>
