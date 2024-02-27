<template>
  <div class="flex flex-col w-96 bg-white rounded-lg shadow-md fixed inset-0 h-screen p-8"> <!-- Added shadow effect -->
    <img src="@/assets/unilogo.png" alt="University Logo" class="h-16 my-4 self-center">
    
    <div class="flex flex-col mt-4 space-y-4"> <!-- Increased vertical spacing -->
      <!-- Updated class name to nav-link -->
      <router-link to="/dashboard" class="group flex flex-row items-center p-4 
      border border-white-300 shadow-sm mt-4 rounded-lg text-black-100" v-bind:class="{'bg-red-100 text-white-100' : selected === 'dashboard'}">
        <img src="@/assets/dashboard.jpg" alt="Dashboard" class="h-10 mx-8">
        <span class="text-2xl">Dashboard</span>
      </router-link>
      
      <router-link to="/academics" class="group flex flex-row items-center p-4 
      border border-white-300 shadow-sm mt-4 rounded-lg" v-bind:class="{'bg-red-100 text-white-100' : selected === 'academics'}">
        <img src="@/assets/Academics.webp" alt="Academics" class="h-10 mx-8">
        <span class="text-2xl group-hover:text-white focus:text-white">Academics</span>
      </router-link>
      
      <router-link to="/application" class="group flex flex-row items-center p-4 border border-white-300 shadow-sm mt-4 rounded-lg"
      v-bind:class="{'bg-red-100 text-white-100' : selected === 'application'}">
        <img src="@/assets/application.png" alt="Application" class="h-10 mx-8">
        <span class="text-2xl group-hover:text-white focus:text-white">Applications</span>
      </router-link>
      
      <router-link to="/misc" class="group flex flex-row items-center p-4 border border-white-300 shadow-sm mt-4 rounded-lg"
      v-bind:class="{'bg-red-100 text-white-100' : selected === 'misc'}">
        <img src="@/assets/aroundU.png" alt="Around U" class="h-10 mx-8">
        <span class="text-2xl group-hover:text-white focus:text-white">Around U</span>
      </router-link>
    </div>
    
    <div class="mt-auto flex justify-between w-full p-10"> 
      <router-link to="/aboutus" class="hover:bg-gray-100 rounded-lg">
        <img src="@/assets/aboutus.png" alt="About Us" class="h-6">
      </router-link>
      
      <router-link to="/profile" class="hover:bg-gray-100 rounded-lg">
        <img src="@/assets/setting.png" alt="Settings" class="h-6">
      </router-link>
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
  }
}
</script>


