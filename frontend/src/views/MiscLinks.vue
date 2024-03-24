<!-- <template>
    <div class="ml-4">
      <div v-for="(groupKey, index) in sortedGroupKeys" :key="index" class="text-left text-red-500 mb-4">
        <h3 class="font-bold">{{ groupKey }}</h3>
        <a v-for="link in linkGroups[groupKey]" :key="link.name" :href="link.url" class="block hover:underline">{{ link.name }}</a>
      </div>
    </div>
  </template>   -->
  
<template>
  <div class="bg-grey-100 shadow-inner h-fit">
    <div class="grid grid-rows-24 grid-cols-12 w-full gap-4 pt-5 pb-4 px-4">
      <div class="row-span-12 col-span-4 bg-white-100 w-full  h-100 rounded-lg shadow-xl">
        <h2 class="relative w-fit mx-4 pt-4 border-b-4 border-yellow-400 font-bold text-xl">Get Involved</h2>
        <div class="pt-4 pb-2 px-4 text-lg">
            <div class="flex flex-row pb-3">
                <a href="https://events.ucalgary.ca" target="_blank" class="w-fit pr-1 hover:underline">Events at UCalgary</a>
            </div>
            <div class="flex flex-row pb-3">
                <a href="https://godinos.com/" target="_blank" class="w-fit pr-1 hover:underline">Dinos Athletics</a>
            </div>
            <div class="flex flex-row pb-3">
                <a href="https://active-living.ucalgary.ca/" target="_blank" class="w-fit pr-1 hover:underline">Active Living Centre</a>
            </div>
            <div class="flex flex-row pb-3">
                <a href="https://suuofc.campuslabs.ca/engage/organizations" target="_blank" class="w-fit pr-1 hover:underline">ClubHub: Clubs & Organisations</a>
            </div>
            <div class="flex flex-row pb-3">
                <a href="https://conted.ucalgary.ca/index.jsp" target="_blank" class="w-fit pr-1 hover:underline">Continuing Education</a>
            </div>
            <div class="flex flex-row pb-3">
                <a href="http://www.ucalgary.ca/international/" target="_blank" class="w-fit pr-1 hover:underline">University of Calgary: International</a>
            </div>
            <div class="flex flex-row pb-3">
                <a href="http://www.su.ucalgary.ca/page/quality-student-life/volunteer-services/volunteer-programs" target="_blank" class="w-fit pr-1 hover:underline">Students' Union: Volunteer Programs</a>
            </div>
            <div class="flex flex-row pb-3">
                <a href="http://netcommunity.ucalgary.ca/Page.aspx?pid=518&srcid=486" target="_blank" class="w-fit pr-1 hover:underline">Donate</a>
            </div>
        </div>
      </div>

      <div class="row-span-12 col-span-3 bg-white-100 w-full  h-100 rounded-lg shadow-xl">
        <h2 class="relative w-fit mx-4 pt-4 border-b-4 border-yellow-400 font-bold text-xl">Get Around</h2>
        <div class="pt-4 pb-2 px-4 text-lg">
            <div class="flex flex-row pb-3">
                <a href="http://contacts.ucalgary.ca/directory/faculties" target="_blank" class="w-fit pr-1 hover:underline">Find a Faculty</a>
            </div>
            <div class="flex flex-row pb-3">
                <a href="http://www.ucalgary.ca/map" target="_blank" class="w-fit pr-1 hover:underline">Find a Building/Room</a>
            </div>
            <div class="flex flex-row pb-3">
                <a href="http://library.ucalgary.ca/" target="_blank" class="w-fit pr-1 hover:underline">Find a Library</a>
            </div>
            <div class="flex flex-row pb-3">
                <a href="http://www.ucalgary.ca/ancillary/food-services" target="_blank" class="w-fit pr-1 hover:underline">Campus Food Services</a>
            </div>
            <div class="flex flex-row pb-3">
                <a href="https://www.ucalgary.ca/sustainability/our-sustainable-campus/transportation" target="_blank" class="w-fit pr-1 hover:underline">Sustainable Transportation</a>
            </div>
            <div class="flex flex-row pb-3">
                <a href="http://www.ucalgary.ca/parking" target="_blank" class="w-fit pr-1 hover:underline">Parking on Campus</a>
            </div>
            <div class="flex flex-row pb-3">
                <a href="http://www.ucalgary.ca/access" target="_blank" class="w-fit pr-1 hover:underline">Accessibility Services</a>
            </div>
        </div>
      </div>

      <div class="row-span-12 col-span-3 bg-white-100 w-full  h-100 rounded-lg shadow-xl">
        <h2 class="relative w-fit mx-4 pt-4 border-b-4 border-yellow-400 font-bold text-xl">Help & Support</h2>
        <div class="flex flex-col justify-between pt-4 pb-2 px-4 text-lg">
            <div class="flex flex-row pb-3">
                <router-link to="/profile" class="w-fit pr-1 hover:underline">Account Management</router-link>
            </div>
            <div class="flex flex-row pb-3">
                <a href="http://workrooms.ucalgary.ca/" target="_blank" class="w-fit pr-1 hover:underline">Workroom Booking</a>
            </div>
            <div class="flex flex-row pb-3">
                <a href="https://www.ucalgary.ca/uservice" target="_blank" class="w-fit pr-1 hover:underline">UService</a>
            </div>
            <div class="flex flex-row pb-3">
                <a href="http://www.ucalgary.ca/it/help" target="_blank" class="w-fit pr-1 hover:underline">IT Services</a>
            </div>
            <div class="flex flex-row pb-3">
                <a href="https://ucalgary.service-now.com/it?id=it_catalog_by_category&sys_id=373facbc13deea4053f2d7b2e144b00c" target="_blank" class="w-fit pr-1 hover:underline">Audio/Visual Support</a>
            </div>
            <div class="flex flex-row pb-3">
                <a href="http://www.ucalgary.ca/printshop/" target="_blank" class="w-fit pr-1 hover:underline">Printing Services</a>
            </div>
            <div class="flex flex-row pb-3">
                <a href="http://www.ucalgary.ca/ses" target="_blank" class="w-fit pr-1 hover:underline">Student Services</a>
            </div>
        </div>
      </div>
    
      <div class="row-span-12 col-span-3 bg-white-100 w-full  h-100 rounded-lg shadow-xl">
        <h2 class="relative w-fit mx-4 pt-4 border-b-4 border-yellow-400 font-bold text-xl">Get Connected</h2>
        <div class="flex flex-col justify-between pt-4 pb-2 px-4 text-lg">
            <div class="flex flex-row pb-3">
                <a href="http://office365.ucalgary.ca/" target="_blank" class="w-fit pr-1 hover:underline">UCalgary Webmail</a>
            </div>
            <div class="flex flex-row pb-3">
                <a href="http://contacts.ucalgary.ca/" target="_blank" class="w-fit pr-1 hover:underline">Contacts Directory</a>
            </div>
            <div class="flex flex-row pb-3">
                <a href="http://contacts.ucalgary.ca/directory/socialmedia" target="_blank" class="w-fit pr-1 hover:underline">UCalgary Social Media</a>
            </div>
            <div class="flex flex-row pb-3">
                <a href="http://www.su.ucalgary.ca/" target="_blank" class="w-fit pr-1 hover:underline">Students' Union</a>
            </div>
            <div class="flex flex-row pb-3">
                <a href="http://gsa.ucalgary.ca/" target="_blank" class="w-fit pr-1 hover:underline">Grad Students' Association</a>
            </div>
        </div>
      </div>
      
    </div>
  </div>
</template>

  <script>
  export default {
    data() {
      return {
        links: [
          {name: 'Home', url: 'https://www.google.com'},
          {name: 'About Us', url: 'https://www.google.com'},
          {name: 'Admissions', url: 'https://www.google.com'},
          {name: 'Academic Programs', url: 'https://www.google.com'},
          {name: 'Faculty', url: 'https://www.google.com'},
          {name: 'Research', url: 'https://www.google.com'},
          {name: 'Student Life', url: 'https://www.google.com'},
          {name: 'Events', url: 'https://www.google.com'},
          {name: 'Alumni', url: 'https://www.google.com'},
          {name: 'Careers', url: 'https://www.google.com'},
          {name: 'Library', url: 'https://www.google.com'},
          {name: 'News', url: 'https://www.google.com'},
          {name: 'Support Services', url: 'https://www.google.com'},
          {name: 'Campus Store', url: 'https://www.google.com'},
          {name: 'Contact Us', url: 'https://www.google.com'},
          {name: 'FAQ', url: 'https://www.google.com'},
          {name: 'Financial Aid', url: 'https://www.google.com'},
          {name: 'International Students', url: 'https://www.google.com'},
        ],
        linkGroups: {}
      };
    },
    created() {
      this.$emit('show-navbar')
      this.$emit('toggle-selected', 'misc')
      this.groupLinks();
    },
    computed: {
    sortedGroupKeys() {
      return Object.keys(this.linkGroups).sort();
    }
  },
  methods: {
    groupLinks() {
      this.links.forEach(link => {
        const firstLetter = link.name.charAt(0).toUpperCase();
        if (!this.linkGroups[firstLetter]) {
          this.linkGroups[firstLetter] = [];
        }
        this.linkGroups[firstLetter].push(link);
      });
    }
  }
};
</script>