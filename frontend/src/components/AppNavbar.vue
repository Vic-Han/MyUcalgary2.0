<template>
  <div class="flex flex-col w-1/5 bg-white rounded-lg shadow-md"> <!-- Added shadow effect -->
    <img src="@/assets/unilogo.png" alt="University Logo" class="h-16 my-4 self-center">
    
    <div class="flex flex-col mt-4 space-y-4"> <!-- Increased vertical spacing -->
      <!-- Updated class name to nav-link -->
      <router-link to="/dashboard" class="group flex items-center py-4 px-4 pl-14 nav-link border-2 border-gray-300 hover:border-transparent hover:bg-red-500 focus:bg-red-500 mb-2 rounded-lg">
        <img src="@/assets/dashboard.jpg" alt="Dashboard" class="h-6 mr-2">
        <span class="group-hover:text-white focus:text-white">Dashboard</span>
      </router-link>
      
      <router-link to="/academics" class="group flex items-center py-4 px-4 pl-14 nav-link border-2 border-gray-300 hover:border-transparent hover:bg-red-500 focus:bg-red-500 mb-2 rounded-lg">
        <img src="@/assets/Academics.webp" alt="Academics" class="h-6 mr-2">
        <span class="group-hover:text-white focus:text-white">Academics</span>
      </router-link>
      
      <router-link to="/application" class="group flex items-center py-4 px-4 pl-14 nav-link border-2 border-gray-300 hover:border-transparent hover:bg-red-500 focus:bg-red-500 mb-2 rounded-lg">
        <img src="@/assets/application.png" alt="Application" class="h-6 mr-2">
        <span class="group-hover:text-white focus:text-white">Applications</span>
      </router-link>
      
      <router-link to="/aroundu" class="group flex items-center py-4 px-4 pl-14 nav-link border-2 border-gray-300 hover:border-transparent hover:bg-red-500 focus:bg-red-500 mb-2 rounded-lg">
        <img src="@/assets/aroundU.png" alt="Around U" class="h-6 mr-2">
        <span class="group-hover:text-white focus:text-white">Around U</span>
      </router-link>
    </div>
    
    <div class="mt-auto flex justify-between w-full p-10"> 
      <router-link to="/aboutus" class="hover:bg-gray-100 rounded-lg">
        <img src="@/assets/aboutus.png" alt="About Us" class="h-6">
      </router-link>
      
      <router-link to="/settings" class="hover:bg-gray-100 rounded-lg">
        <img src="@/assets/setting.png" alt="Settings" class="h-6">
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AppNavbar'
}
</script>

<style scoped>
/* Added nav-link style class */
.nav-link {
  width: 80%; /* Adjusted width to 80% of navbar width */
  margin-left: auto; /* Right align to center it */
  margin-right: auto; /* Left align to center it */
  border-radius: 20px; /* Made border more rounded */
}
</style>
