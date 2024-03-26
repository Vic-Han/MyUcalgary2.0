<template>
  <div class="flex flex-row w-screen h-screen overflow-hidden shadow-inner bg-grey-100" v-bind:class="{'pl-96':navbarVisible}">
    <AppNavbar v-if="navbarVisible" :selected="selected" />
    <div class="w-full">
      <div v-if="navbarVisible" class="flex items-center justify-start py-4 px-4 bg-gray-200">
        <div class="flex flex-col w-2/5">
          <div class="flex items-center space-x-2 bg-white-100 rounded-lg shadow-md p-2 w-full ml-5 h-11">
            <input type="text" class="flex-grow outline-none rounded-l-full px-4 py-2" @input="showSearchResults" placeholder="Search" v-model="searchTerm" />
            <div v-if="filteredComponents.length || filteredLinks.length" @click="clearSearch">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 fill-grey-200 cursor-pointer hover:fill-red-100" viewBox="0 -960 960 960">
                <path d="m256-200-56-56 224-224-224-224 56-56 224 224 224-224 56 56-224 224 224 224-56 56-224-224-224 224Z"/>
              </svg>
            </div>
            <div v-else>
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 fill-grey-200" viewBox="0 0 50 50">
                <path d="M 21 3 C 11.621094 3 4 10.621094 4 20 C 4 29.378906 11.621094 37 21 37 C 24.710938 37 28.140625 35.804688 30.9375 33.78125 L 44.09375 46.90625 L 46.90625 44.09375 L 33.90625 31.0625 C 36.460938 28.085938 38 24.222656 38 20 C 38 10.621094 30.378906 3 21 3 Z M 21 5 C 29.296875 5 36 11.703125 36 20 C 36 28.296875 29.296875 35 21 35 C 12.703125 35 6 28.296875 6 20 C 6 11.703125 12.703125 5 21 5 Z"></path>
              </svg>
            </div>
          </div>
          <div id="search-dropdown" v-if="filteredComponents.length || filteredLinks.length" v class="relative w-full">
            <div class="absolute h-fit z-50 left-4 -bottom-4 translate-y-full p-2 bg-white-100 w-full shadow-xl rounded-lg">
              <div class="h-fit max-h-200 overflow-y-auto">
                <div v-if="filteredComponents.length">
                  <div class="font-semibold text-left text-3xl p-4">Components</div>
                  <div class="flex flex-col divide-y divide-grey-100">
                    <div v-for="(component,index) in filteredComponents" :key="index" @click="clearSearchNavigate(component.item.target)">
                      <router-link :to="component.item.target" class="flex flex-row py-2 hover:bg-grey-100">
                        <div class="flex items-center mx-4">
                          <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 fill-black-100" :viewBox="component.item.viewBox">
                            <path :d="component.item.path"/>
                          </svg>
                        </div>
                        <div class="flex flex-col">
                          <div class="font-semibold text-xl text-left">{{ component.item.name }}</div>
                          <div class="text-grey-200 text-sm text-left">{{ component.item.target }}</div>
                        </div>
                      </router-link>
                    </div>
                  </div>
                </div>
                <div v-if="filteredLinks.length">
                  <div class="font-semibold text-left text-3xl pl-4">Links</div>
                  <div class="flex flex-col divide-y divide-grey-100">
                    <div v-for="(link,index) in filteredLinks" :key="index">
                      <a :href="link.item.target" target="_blank" class="flex flex-row py-2 hover:bg-grey-100">
                        <div class="flex items-center mx-4">
                          <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 fill-black-100" :viewBox="link.item.viewBox">
                            <path :d="link.item.path"/>
                          </svg>
                        </div>
                        <div class="flex flex-col">
                          <div class="font-semibold text-xl text-left">{{ link.item.name }}</div>
                          <div class="text-grey-200 text-sm text-left">{{ link.item.target }}</div>
                        </div>
                      </a>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
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
          target: "/dashboard",
          viewBox: "0 -960 960 960",
          path: "M160-120v-480l320-240 320 240v480H560v-280H400v280H160Z"
        },
        {
          name: "Academics",
          terms: [
            "grades",
            "academics",
            "report",
            "requirements"
          ],
          target: "/academics",
          viewBox: "0 -960 960 960",
          path: "M840-280v-276L480-360 40-600l440-240 440 240v320h-80ZM480-120 200-272v-200l280 152 280-152v200L480-120Z"
        },
        {
          name: "Finances",
          terms: [
            "money",
            "finances",
            "report",
            "due"
          ],
          target: "/finances",
          viewBox: "0 -960 960 960",
          path: "M444-200h70v-50q50-9 86-39t36-89q0-42-24-77t-96-61q-60-20-83-35t-23-41q0-26 18.5-41t53.5-15q32 0 50 15.5t26 38.5l64-26q-11-35-40.5-61T516-710v-50h-70v50q-50 11-78 44t-28 74q0 47 27.5 76t86.5 50q63 23 87.5 41t24.5 47q0 33-23.5 48.5T486-314q-33 0-58.5-20.5T390-396l-66 26q14 48 43.5 77.5T444-252v52Zm36 120q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Z"
        },
        {
          name: "Grades",
          terms: [
            "grades",
            "academics",
            "gpa"
          ],
          target: "/grades",
          viewBox: "0 -960 960 960",
          path: "m40-200 210-560h100l210 560h-96l-51-143H187l-51 143H40Zm176-224h168l-82-232h-4l-82 232Zm504 104v-120H600v-80h120v-120h80v120h120v80H800v120h-80Z"
        },
        {
          name: "Applications",
          terms: [
            "applications",
            "programs"
          ],
          target: "/application",
          viewBox: "0 -960 960 960",
          path: "M400-400h160v-80H400v80Zm0-120h320v-80H400v80Zm0-120h320v-80H400v80Zm-80 400q-33 0-56.5-23.5T240-320v-480q0-33 23.5-56.5T320-880h480q33 0 56.5 23.5T880-800v480q0 33-23.5 56.5T800-240H320ZM160-80q-33 0-56.5-23.5T80-160v-560h80v560h560v80H160Z"
        },
        {
          name: "AroundU",
          terms: [
            "links",
            "aroundu",
            "misc"
          ],
          target: "/misc",
          viewBox: "0 -960 960 960",
          path: "M200-280v-280h80v280h-80Zm240 0v-280h80v280h-80ZM80-120v-80h800v80H80Zm600-160v-280h80v280h-80ZM80-640v-80l400-200 400 200v80H80Z"
        },
        {
          name: "Profile",
          terms: [
            "settings",
            "profile",
            "account"
          ],
          target: "/profile",
          viewBox: "0 -960 960 960",
          path: "M480-480q-66 0-113-47t-47-113q0-66 47-113t113-47q66 0 113 47t47 113q0 66-47 113t-113 47ZM160-160v-112q0-34 17.5-62.5T224-378q62-31 126-46.5T480-440q66 0 130 15.5T736-378q29 15 46.5 43.5T800-272v112H160Z"
        },
        {
          name: "Schedule Builder",
          terms: [
            "schedule",
            "calendar",
            "classes"
          ],
          target: "/schedule",
          viewBox: "0 -960 960 960",
          path: "M200-80q-33 0-56.5-23.5T120-160v-560q0-33 23.5-56.5T200-800h40v-80h80v80h320v-80h80v80h40q33 0 56.5 23.5T840-720v200h-80v-40H200v400h280v80H200Zm360 0v-123l221-220q9-9 20-13t22-4q12 0 23 4.5t20 13.5l37 37q8 9 12.5 20t4.5 22q0 11-4 22.5T903-300L683-80H560Zm263-224 37-39-37-37-38 38 38 38Z"
        }
      ],
      links: [
        {
          "name": "Events at UCalgary",
          "section": "Get Involved",
          "target": "https://events.ucalgary.ca",
          "viewBox": "0 -960 960 960",
          "path": "M40-160v-160q0-34 23.5-57t56.5-23h131q20 0 38 10t29 27q29 39 71.5 61t90.5 22q49 0 91.5-22t70.5-61q13-17 30.5-27t36.5-10h131q34 0 57 23t23 57v160H640v-91q-35 25-75.5 38T480-200q-43 0-84-13.5T320-252v92H40Zm440-160q-38 0-72-17.5T351-386q-17-25-42.5-39.5T253-440q22-37 93-58.5T480-520q63 0 134 21.5t93 58.5q-29 0-55 14.5T609-386q-22 32-56 49t-73 17ZM160-440q-50 0-85-35t-35-85q0-51 35-85.5t85-34.5q51 0 85.5 34.5T280-560q0 50-34.5 85T160-440Zm640 0q-50 0-85-35t-35-85q0-51 35-85.5t85-34.5q51 0 85.5 34.5T920-560q0 50-34.5 85T800-440ZM480-560q-50 0-85-35t-35-85q0-51 35-85.5t85-34.5q51 0 85.5 34.5T600-680q0 50-34.5 85T480-560Z"
        },
        {
          "name": "Dinos Athletics",
          "section": "Get Involved",
          "target": "https://godinos.com/",
          "viewBox": "0 -960 960 960",
          "path": "M40-160v-160q0-34 23.5-57t56.5-23h131q20 0 38 10t29 27q29 39 71.5 61t90.5 22q49 0 91.5-22t70.5-61q13-17 30.5-27t36.5-10h131q34 0 57 23t23 57v160H640v-91q-35 25-75.5 38T480-200q-43 0-84-13.5T320-252v92H40Zm440-160q-38 0-72-17.5T351-386q-17-25-42.5-39.5T253-440q22-37 93-58.5T480-520q63 0 134 21.5t93 58.5q-29 0-55 14.5T609-386q-22 32-56 49t-73 17ZM160-440q-50 0-85-35t-35-85q0-51 35-85.5t85-34.5q51 0 85.5 34.5T280-560q0 50-34.5 85T160-440Zm640 0q-50 0-85-35t-35-85q0-51 35-85.5t85-34.5q51 0 85.5 34.5T920-560q0 50-34.5 85T800-440ZM480-560q-50 0-85-35t-35-85q0-51 35-85.5t85-34.5q51 0 85.5 34.5T600-680q0 50-34.5 85T480-560Z"
        },
        {
          "name": "Active Living Centre",
          "section": "Get Involved",
          "target": "https://active-living.ucalgary.ca/",
          "viewBox": "0 -960 960 960",
          "path": "M40-160v-160q0-34 23.5-57t56.5-23h131q20 0 38 10t29 27q29 39 71.5 61t90.5 22q49 0 91.5-22t70.5-61q13-17 30.5-27t36.5-10h131q34 0 57 23t23 57v160H640v-91q-35 25-75.5 38T480-200q-43 0-84-13.5T320-252v92H40Zm440-160q-38 0-72-17.5T351-386q-17-25-42.5-39.5T253-440q22-37 93-58.5T480-520q63 0 134 21.5t93 58.5q-29 0-55 14.5T609-386q-22 32-56 49t-73 17ZM160-440q-50 0-85-35t-35-85q0-51 35-85.5t85-34.5q51 0 85.5 34.5T280-560q0 50-34.5 85T160-440Zm640 0q-50 0-85-35t-35-85q0-51 35-85.5t85-34.5q51 0 85.5 34.5T920-560q0 50-34.5 85T800-440ZM480-560q-50 0-85-35t-35-85q0-51 35-85.5t85-34.5q51 0 85.5 34.5T600-680q0 50-34.5 85T480-560Z"
        },
        {
          "name": "ClubHub: Clubs & Organisations",
          "section": "Get Involved",
          "target": "https://suuofc.campuslabs.ca/engage/organizations",
          "viewBox": "0 -960 960 960",
          "path": "M40-160v-160q0-34 23.5-57t56.5-23h131q20 0 38 10t29 27q29 39 71.5 61t90.5 22q49 0 91.5-22t70.5-61q13-17 30.5-27t36.5-10h131q34 0 57 23t23 57v160H640v-91q-35 25-75.5 38T480-200q-43 0-84-13.5T320-252v92H40Zm440-160q-38 0-72-17.5T351-386q-17-25-42.5-39.5T253-440q22-37 93-58.5T480-520q63 0 134 21.5t93 58.5q-29 0-55 14.5T609-386q-22 32-56 49t-73 17ZM160-440q-50 0-85-35t-35-85q0-51 35-85.5t85-34.5q51 0 85.5 34.5T280-560q0 50-34.5 85T160-440Zm640 0q-50 0-85-35t-35-85q0-51 35-85.5t85-34.5q51 0 85.5 34.5T920-560q0 50-34.5 85T800-440ZM480-560q-50 0-85-35t-35-85q0-51 35-85.5t85-34.5q51 0 85.5 34.5T600-680q0 50-34.5 85T480-560Z"
        },
        {
          "name": "Continuing Education",
          "section": "Get Involved",
          "target": "https://conted.ucalgary.ca/index.jsp",
          "viewBox": "0 -960 960 960",
          "path": "M40-160v-160q0-34 23.5-57t56.5-23h131q20 0 38 10t29 27q29 39 71.5 61t90.5 22q49 0 91.5-22t70.5-61q13-17 30.5-27t36.5-10h131q34 0 57 23t23 57v160H640v-91q-35 25-75.5 38T480-200q-43 0-84-13.5T320-252v92H40Zm440-160q-38 0-72-17.5T351-386q-17-25-42.5-39.5T253-440q22-37 93-58.5T480-520q63 0 134 21.5t93 58.5q-29 0-55 14.5T609-386q-22 32-56 49t-73 17ZM160-440q-50 0-85-35t-35-85q0-51 35-85.5t85-34.5q51 0 85.5 34.5T280-560q0 50-34.5 85T160-440Zm640 0q-50 0-85-35t-35-85q0-51 35-85.5t85-34.5q51 0 85.5 34.5T920-560q0 50-34.5 85T800-440ZM480-560q-50 0-85-35t-35-85q0-51 35-85.5t85-34.5q51 0 85.5 34.5T600-680q0 50-34.5 85T480-560Z"
        },
        {
          "name": "University of Calgary: International",
          "section": "Get Involved",
          "target": "http://www.ucalgary.ca/international/",
          "viewBox": "0 -960 960 960",
          "path": "M40-160v-160q0-34 23.5-57t56.5-23h131q20 0 38 10t29 27q29 39 71.5 61t90.5 22q49 0 91.5-22t70.5-61q13-17 30.5-27t36.5-10h131q34 0 57 23t23 57v160H640v-91q-35 25-75.5 38T480-200q-43 0-84-13.5T320-252v92H40Zm440-160q-38 0-72-17.5T351-386q-17-25-42.5-39.5T253-440q22-37 93-58.5T480-520q63 0 134 21.5t93 58.5q-29 0-55 14.5T609-386q-22 32-56 49t-73 17ZM160-440q-50 0-85-35t-35-85q0-51 35-85.5t85-34.5q51 0 85.5 34.5T280-560q0 50-34.5 85T160-440Zm640 0q-50 0-85-35t-35-85q0-51 35-85.5t85-34.5q51 0 85.5 34.5T920-560q0 50-34.5 85T800-440ZM480-560q-50 0-85-35t-35-85q0-51 35-85.5t85-34.5q51 0 85.5 34.5T600-680q0 50-34.5 85T480-560Z"
        },
        {
          "name": "Students' Union: Volunteer Programs",
          "section": "Get Involved",
          "target": "http://www.su.ucalgary.ca/page/quality-student-life/volunteer-services/volunteer-programs",
          "viewBox": "0 -960 960 960",
          "path": "M40-160v-160q0-34 23.5-57t56.5-23h131q20 0 38 10t29 27q29 39 71.5 61t90.5 22q49 0 91.5-22t70.5-61q13-17 30.5-27t36.5-10h131q34 0 57 23t23 57v160H640v-91q-35 25-75.5 38T480-200q-43 0-84-13.5T320-252v92H40Zm440-160q-38 0-72-17.5T351-386q-17-25-42.5-39.5T253-440q22-37 93-58.5T480-520q63 0 134 21.5t93 58.5q-29 0-55 14.5T609-386q-22 32-56 49t-73 17ZM160-440q-50 0-85-35t-35-85q0-51 35-85.5t85-34.5q51 0 85.5 34.5T280-560q0 50-34.5 85T160-440Zm640 0q-50 0-85-35t-35-85q0-51 35-85.5t85-34.5q51 0 85.5 34.5T920-560q0 50-34.5 85T800-440ZM480-560q-50 0-85-35t-35-85q0-51 35-85.5t85-34.5q51 0 85.5 34.5T600-680q0 50-34.5 85T480-560Z"
        },
        {
          "name": "Donate",
          "section": "Get Involved",
          "target": "http://netcommunity.ucalgary.ca/Page.aspx?pid=518&srcid=486",
          "viewBox": "0 -960 960 960",
          "path": "M400-186v-228l56-160q5-11 14.5-18.5T494-600h292q14 0 23.5 7.5T824-574l56 160v228q0 11-7.5 18.5T854-160h-28q-11 0-18.5-7.5T800-186v-34H480v34q0 11-7.5 18.5T454-160h-28q-11 0-18.5-7.5T400-186Zm80-274h320l-28-80H508l-28 80Zm40 160q17 0 28.5-11.5T560-340q0-17-11.5-28.5T520-380q-17 0-28.5 11.5T480-340q0 17 11.5 28.5T520-300Zm240 0q17 0 28.5-11.5T800-340q0-17-11.5-28.5T760-380q-17 0-28.5 11.5T720-340q0 17 11.5 28.5T760-300ZM160-160v-40l40-40q-50 0-85-35t-35-85v-320q0-66 59-93t201-27q148 0 204 26t56 94v40h-80v-40H160v240h200v280H160Zm40-160q17 0 28.5-11.5T240-360q0-17-11.5-28.5T200-400q-17 0-28.5 11.5T160-360q0 17 11.5 28.5T200-320Z"
        },
        {
          "name": "Find a Faculty",
          "section": "Get Around",
          "target": "http://contacts.ucalgary.ca/directory/faculties",
          "viewBox": "0 -960 960 960",
          "path": "M400-186v-228l56-160q5-11 14.5-18.5T494-600h292q14 0 23.5 7.5T824-574l56 160v228q0 11-7.5 18.5T854-160h-28q-11 0-18.5-7.5T800-186v-34H480v34q0 11-7.5 18.5T454-160h-28q-11 0-18.5-7.5T400-186Zm80-274h320l-28-80H508l-28 80Zm40 160q17 0 28.5-11.5T560-340q0-17-11.5-28.5T520-380q-17 0-28.5 11.5T480-340q0 17 11.5 28.5T520-300Zm240 0q17 0 28.5-11.5T800-340q0-17-11.5-28.5T760-380q-17 0-28.5 11.5T720-340q0 17 11.5 28.5T760-300ZM160-160v-40l40-40q-50 0-85-35t-35-85v-320q0-66 59-93t201-27q148 0 204 26t56 94v40h-80v-40H160v240h200v280H160Zm40-160q17 0 28.5-11.5T240-360q0-17-11.5-28.5T200-400q-17 0-28.5 11.5T160-360q0 17 11.5 28.5T200-320Z"
        },
        {
          "name": "Find a Building/Room",
          "section": "Get Around",
          "target": "http://www.ucalgary.ca/map",
          "viewBox": "0 -960 960 960",
          "path": "M400-186v-228l56-160q5-11 14.5-18.5T494-600h292q14 0 23.5 7.5T824-574l56 160v228q0 11-7.5 18.5T854-160h-28q-11 0-18.5-7.5T800-186v-34H480v34q0 11-7.5 18.5T454-160h-28q-11 0-18.5-7.5T400-186Zm80-274h320l-28-80H508l-28 80Zm40 160q17 0 28.5-11.5T560-340q0-17-11.5-28.5T520-380q-17 0-28.5 11.5T480-340q0 17 11.5 28.5T520-300Zm240 0q17 0 28.5-11.5T800-340q0-17-11.5-28.5T760-380q-17 0-28.5 11.5T720-340q0 17 11.5 28.5T760-300ZM160-160v-40l40-40q-50 0-85-35t-35-85v-320q0-66 59-93t201-27q148 0 204 26t56 94v40h-80v-40H160v240h200v280H160Zm40-160q17 0 28.5-11.5T240-360q0-17-11.5-28.5T200-400q-17 0-28.5 11.5T160-360q0 17 11.5 28.5T200-320Z"
        },
        {
          "name": "Find a Library",
          "section": "Get Around",
          "target": "http://library.ucalgary.ca/",
          "viewBox": "0 -960 960 960",
          "path": "M400-186v-228l56-160q5-11 14.5-18.5T494-600h292q14 0 23.5 7.5T824-574l56 160v228q0 11-7.5 18.5T854-160h-28q-11 0-18.5-7.5T800-186v-34H480v34q0 11-7.5 18.5T454-160h-28q-11 0-18.5-7.5T400-186Zm80-274h320l-28-80H508l-28 80Zm40 160q17 0 28.5-11.5T560-340q0-17-11.5-28.5T520-380q-17 0-28.5 11.5T480-340q0 17 11.5 28.5T520-300Zm240 0q17 0 28.5-11.5T800-340q0-17-11.5-28.5T760-380q-17 0-28.5 11.5T720-340q0 17 11.5 28.5T760-300ZM160-160v-40l40-40q-50 0-85-35t-35-85v-320q0-66 59-93t201-27q148 0 204 26t56 94v40h-80v-40H160v240h200v280H160Zm40-160q17 0 28.5-11.5T240-360q0-17-11.5-28.5T200-400q-17 0-28.5 11.5T160-360q0 17 11.5 28.5T200-320Z"
        },
        {
          "name": "Campus Food Services",
          "section": "Get Around",
          "target": "http://www.ucalgary.ca/ancillary/food-services",
          "viewBox": "0 -960 960 960",
          "path": "M400-186v-228l56-160q5-11 14.5-18.5T494-600h292q14 0 23.5 7.5T824-574l56 160v228q0 11-7.5 18.5T854-160h-28q-11 0-18.5-7.5T800-186v-34H480v34q0 11-7.5 18.5T454-160h-28q-11 0-18.5-7.5T400-186Zm80-274h320l-28-80H508l-28 80Zm40 160q17 0 28.5-11.5T560-340q0-17-11.5-28.5T520-380q-17 0-28.5 11.5T480-340q0 17 11.5 28.5T520-300Zm240 0q17 0 28.5-11.5T800-340q0-17-11.5-28.5T760-380q-17 0-28.5 11.5T720-340q0 17 11.5 28.5T760-300ZM160-160v-40l40-40q-50 0-85-35t-35-85v-320q0-66 59-93t201-27q148 0 204 26t56 94v40h-80v-40H160v240h200v280H160Zm40-160q17 0 28.5-11.5T240-360q0-17-11.5-28.5T200-400q-17 0-28.5 11.5T160-360q0 17 11.5 28.5T200-320Z"
        },
        {
          "name": "Sustainable Transportation",
          "section": "Get Around",
          "target": "https://www.ucalgary.ca/sustainability/our-sustainable-campus/transportation",
          "viewBox": "0 -960 960 960",
          "path": "M400-186v-228l56-160q5-11 14.5-18.5T494-600h292q14 0 23.5 7.5T824-574l56 160v228q0 11-7.5 18.5T854-160h-28q-11 0-18.5-7.5T800-186v-34H480v34q0 11-7.5 18.5T454-160h-28q-11 0-18.5-7.5T400-186Zm80-274h320l-28-80H508l-28 80Zm40 160q17 0 28.5-11.5T560-340q0-17-11.5-28.5T520-380q-17 0-28.5 11.5T480-340q0 17 11.5 28.5T520-300Zm240 0q17 0 28.5-11.5T800-340q0-17-11.5-28.5T760-380q-17 0-28.5 11.5T720-340q0 17 11.5 28.5T760-300ZM160-160v-40l40-40q-50 0-85-35t-35-85v-320q0-66 59-93t201-27q148 0 204 26t56 94v40h-80v-40H160v240h200v280H160Zm40-160q17 0 28.5-11.5T240-360q0-17-11.5-28.5T200-400q-17 0-28.5 11.5T160-360q0 17 11.5 28.5T200-320Z"
        },
        {
          "name": "Parking on Campus",
          "section": "Get Around",
          "target": "http://www.ucalgary.ca/parking",
          "viewBox": "0 -960 960 960",
          "path": "M400-186v-228l56-160q5-11 14.5-18.5T494-600h292q14 0 23.5 7.5T824-574l56 160v228q0 11-7.5 18.5T854-160h-28q-11 0-18.5-7.5T800-186v-34H480v34q0 11-7.5 18.5T454-160h-28q-11 0-18.5-7.5T400-186Zm80-274h320l-28-80H508l-28 80Zm40 160q17 0 28.5-11.5T560-340q0-17-11.5-28.5T520-380q-17 0-28.5 11.5T480-340q0 17 11.5 28.5T520-300Zm240 0q17 0 28.5-11.5T800-340q0-17-11.5-28.5T760-380q-17 0-28.5 11.5T720-340q0 17 11.5 28.5T760-300ZM160-160v-40l40-40q-50 0-85-35t-35-85v-320q0-66 59-93t201-27q148 0 204 26t56 94v40h-80v-40H160v240h200v280H160Zm40-160q17 0 28.5-11.5T240-360q0-17-11.5-28.5T200-400q-17 0-28.5 11.5T160-360q0 17 11.5 28.5T200-320Z"
        },
        {
          "name": "Accessibility Services",
          "section": "Get Around",
          "target": "http://www.ucalgary.ca/access",
          "viewBox": "0 -960 960 960",
          "path": "M400-186v-228l56-160q5-11 14.5-18.5T494-600h292q14 0 23.5 7.5T824-574l56 160v228q0 11-7.5 18.5T854-160h-28q-11 0-18.5-7.5T800-186v-34H480v34q0 11-7.5 18.5T454-160h-28q-11 0-18.5-7.5T400-186Zm80-274h320l-28-80H508l-28 80Zm40 160q17 0 28.5-11.5T560-340q0-17-11.5-28.5T520-380q-17 0-28.5 11.5T480-340q0 17 11.5 28.5T520-300Zm240 0q17 0 28.5-11.5T800-340q0-17-11.5-28.5T760-380q-17 0-28.5 11.5T720-340q0 17 11.5 28.5T760-300ZM160-160v-40l40-40q-50 0-85-35t-35-85v-320q0-66 59-93t201-27q148 0 204 26t56 94v40h-80v-40H160v240h200v280H160Zm40-160q17 0 28.5-11.5T240-360q0-17-11.5-28.5T200-400q-17 0-28.5 11.5T160-360q0 17 11.5 28.5T200-320Z"
        },
        {
          "name": "Workroom Booking",
          "section": "Help & Support",
          "target": "http://workrooms.ucalgary.ca/",
          "viewBox": "0 -960 960 960",
          "path": "M478-240q21 0 35.5-14.5T528-290q0-21-14.5-35.5T478-340q-21 0-35.5 14.5T428-290q0 21 14.5 35.5T478-240Zm-36-154h74q0-33 7.5-52t42.5-52q26-26 41-49.5t15-56.5q0-56-41-86t-97-30q-57 0-92.5 30T342-618l66 26q5-18 22.5-39t53.5-21q32 0 48 17.5t16 38.5q0 20-12 37.5T506-526q-44 39-54 59t-10 73Zm38 314q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Zm0-80q134 0 227-93t93-227q0-134-93-227t-227-93q-134 0-227 93t-93 227q0 134 93 227t227 93Zm0-320Z"
        },
        {
          "name": "UService",
          "section": "Help & Support",
          "target": "https://www.ucalgary.ca/uservice",
          "viewBox": "0 -960 960 960",
          "path": "M478-240q21 0 35.5-14.5T528-290q0-21-14.5-35.5T478-340q-21 0-35.5 14.5T428-290q0 21 14.5 35.5T478-240Zm-36-154h74q0-33 7.5-52t42.5-52q26-26 41-49.5t15-56.5q0-56-41-86t-97-30q-57 0-92.5 30T342-618l66 26q5-18 22.5-39t53.5-21q32 0 48 17.5t16 38.5q0 20-12 37.5T506-526q-44 39-54 59t-10 73Zm38 314q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Zm0-80q134 0 227-93t93-227q0-134-93-227t-227-93q-134 0-227 93t-93 227q0 134 93 227t227 93Zm0-320Z"
        },
        {
          "name": "IT Services",
          "section": "Help & Support",
          "target": "http://www.ucalgary.ca/it/help",
          "viewBox": "0 -960 960 960",
          "path": "M478-240q21 0 35.5-14.5T528-290q0-21-14.5-35.5T478-340q-21 0-35.5 14.5T428-290q0 21 14.5 35.5T478-240Zm-36-154h74q0-33 7.5-52t42.5-52q26-26 41-49.5t15-56.5q0-56-41-86t-97-30q-57 0-92.5 30T342-618l66 26q5-18 22.5-39t53.5-21q32 0 48 17.5t16 38.5q0 20-12 37.5T506-526q-44 39-54 59t-10 73Zm38 314q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Zm0-80q134 0 227-93t93-227q0-134-93-227t-227-93q-134 0-227 93t-93 227q0 134 93 227t227 93Zm0-320Z"
        },
        {
          "name": "Audio/Visual Support",
          "section": "Help & Support",
          "target": "https://ucalgary.service-now.com/it?id=it_catalog_by_category&sys_id=373facbc13deea4053f2d7b2e144b00c",
          "viewBox": "0 -960 960 960",
          "path": "M478-240q21 0 35.5-14.5T528-290q0-21-14.5-35.5T478-340q-21 0-35.5 14.5T428-290q0 21 14.5 35.5T478-240Zm-36-154h74q0-33 7.5-52t42.5-52q26-26 41-49.5t15-56.5q0-56-41-86t-97-30q-57 0-92.5 30T342-618l66 26q5-18 22.5-39t53.5-21q32 0 48 17.5t16 38.5q0 20-12 37.5T506-526q-44 39-54 59t-10 73Zm38 314q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Zm0-80q134 0 227-93t93-227q0-134-93-227t-227-93q-134 0-227 93t-93 227q0 134 93 227t227 93Zm0-320Z"
        },
        {
          "name": "Printing Services",
          "section": "Help & Support",
          "target": "http://www.ucalgary.ca/printshop/",
          "viewBox": "0 -960 960 960",
          "path": "M478-240q21 0 35.5-14.5T528-290q0-21-14.5-35.5T478-340q-21 0-35.5 14.5T428-290q0 21 14.5 35.5T478-240Zm-36-154h74q0-33 7.5-52t42.5-52q26-26 41-49.5t15-56.5q0-56-41-86t-97-30q-57 0-92.5 30T342-618l66 26q5-18 22.5-39t53.5-21q32 0 48 17.5t16 38.5q0 20-12 37.5T506-526q-44 39-54 59t-10 73Zm38 314q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Zm0-80q134 0 227-93t93-227q0-134-93-227t-227-93q-134 0-227 93t-93 227q0 134 93 227t227 93Zm0-320Z"
        },
        {
          "name": "Student Services",
          "section": "Help & Support",
          "target": "http://www.ucalgary.ca/ses",
          "viewBox": "0 -960 960 960",
          "path": "M478-240q21 0 35.5-14.5T528-290q0-21-14.5-35.5T478-340q-21 0-35.5 14.5T428-290q0 21 14.5 35.5T478-240Zm-36-154h74q0-33 7.5-52t42.5-52q26-26 41-49.5t15-56.5q0-56-41-86t-97-30q-57 0-92.5 30T342-618l66 26q5-18 22.5-39t53.5-21q32 0 48 17.5t16 38.5q0 20-12 37.5T506-526q-44 39-54 59t-10 73Zm38 314q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Zm0-80q134 0 227-93t93-227q0-134-93-227t-227-93q-134 0-227 93t-93 227q0 134 93 227t227 93Zm0-320Z"
        },
        {
          "name": "UCalgary Webmail",
          "section": "Get Connected",
          "target": "http://office365.ucalgary.ca/",
          "viewBox": "0 -960 960 960",
          "path": "M720-360v-80h80q17 0 28.5 11.5T840-400q0 17-11.5 28.5T800-360h-80Zm0 160v-80h80q17 0 28.5 11.5T840-240q0 17-11.5 28.5T800-200h-80Zm-160 40q-33 0-56.5-23.5T480-240h-80v-160h80q0-33 23.5-56.5T560-480h120v320H560ZM280-280q-66 0-113-47t-47-113q0-66 47-113t113-47h60q25 0 42.5-17.5T400-660q0-25-17.5-42.5T340-720H200q-17 0-28.5-11.5T160-760q0-17 11.5-28.5T200-800h140q58 0 99 41t41 99q0 58-41 99t-99 41h-60q-33 0-56.5 23.5T200-440q0 33 23.5 56.5T280-360h80v80h-80Z"
        },
        {
          "name": "Contacts Directory",
          "section": "Get Connected",
          "target": "http://contacts.ucalgary.ca/",
          "viewBox": "0 -960 960 960",
          "path": "M720-360v-80h80q17 0 28.5 11.5T840-400q0 17-11.5 28.5T800-360h-80Zm0 160v-80h80q17 0 28.5 11.5T840-240q0 17-11.5 28.5T800-200h-80Zm-160 40q-33 0-56.5-23.5T480-240h-80v-160h80q0-33 23.5-56.5T560-480h120v320H560ZM280-280q-66 0-113-47t-47-113q0-66 47-113t113-47h60q25 0 42.5-17.5T400-660q0-25-17.5-42.5T340-720H200q-17 0-28.5-11.5T160-760q0-17 11.5-28.5T200-800h140q58 0 99 41t41 99q0 58-41 99t-99 41h-60q-33 0-56.5 23.5T200-440q0 33 23.5 56.5T280-360h80v80h-80Z"
        },
        {
          "name": "UCalgary Social Media",
          "section": "Get Connected",
          "target": "http://contacts.ucalgary.ca/directory/socialmedia",
          "viewBox": "0 -960 960 960",
          "path": "M720-360v-80h80q17 0 28.5 11.5T840-400q0 17-11.5 28.5T800-360h-80Zm0 160v-80h80q17 0 28.5 11.5T840-240q0 17-11.5 28.5T800-200h-80Zm-160 40q-33 0-56.5-23.5T480-240h-80v-160h80q0-33 23.5-56.5T560-480h120v320H560ZM280-280q-66 0-113-47t-47-113q0-66 47-113t113-47h60q25 0 42.5-17.5T400-660q0-25-17.5-42.5T340-720H200q-17 0-28.5-11.5T160-760q0-17 11.5-28.5T200-800h140q58 0 99 41t41 99q0 58-41 99t-99 41h-60q-33 0-56.5 23.5T200-440q0 33 23.5 56.5T280-360h80v80h-80Z"
        },
        {
          "name": "Students' Union",
          "section": "Get Connected",
          "target": "http://www.su.ucalgary.ca/",
          "viewBox": "0 -960 960 960",
          "path": "M720-360v-80h80q17 0 28.5 11.5T840-400q0 17-11.5 28.5T800-360h-80Zm0 160v-80h80q17 0 28.5 11.5T840-240q0 17-11.5 28.5T800-200h-80Zm-160 40q-33 0-56.5-23.5T480-240h-80v-160h80q0-33 23.5-56.5T560-480h120v320H560ZM280-280q-66 0-113-47t-47-113q0-66 47-113t113-47h60q25 0 42.5-17.5T400-660q0-25-17.5-42.5T340-720H200q-17 0-28.5-11.5T160-760q0-17 11.5-28.5T200-800h140q58 0 99 41t41 99q0 58-41 99t-99 41h-60q-33 0-56.5 23.5T200-440q0 33 23.5 56.5T280-360h80v80h-80Z"
        },
        {
          "name": "Grad Students' Association",
          "section": "Get Connected",
          "target": "http://gsa.ucalgary.ca/",
          "viewBox": "0 -960 960 960",
          "path": "M720-360v-80h80q17 0 28.5 11.5T840-400q0 17-11.5 28.5T800-360h-80Zm0 160v-80h80q17 0 28.5 11.5T840-240q0 17-11.5 28.5T800-200h-80Zm-160 40q-33 0-56.5-23.5T480-240h-80v-160h80q0-33 23.5-56.5T560-480h120v320H560ZM280-280q-66 0-113-47t-47-113q0-66 47-113t113-47h60q25 0 42.5-17.5T400-660q0-25-17.5-42.5T340-720H200q-17 0-28.5-11.5T160-760q0-17 11.5-28.5T200-800h140q58 0 99 41t41 99q0 58-41 99t-99 41h-60q-33 0-56.5 23.5T200-440q0 33 23.5 56.5T280-360h80v80h-80Z"
        },
        {
          "name": "Book Space",
          "section": "Welcome Guests",
          "target": "http://www.ucalgary.ca/mse",
          "viewBox": "0 -960 960 960",
          "path": "M480-80q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q146 0 255.5 91.5T872-559h-82q-19-73-68.5-130.5T600-776v16q0 33-23.5 56.5T520-680h-80v80q0 17-11.5 28.5T400-560h-80v80h80v120h-40L168-552q-3 18-5.5 36t-2.5 36q0 131 92 225t228 95v80Zm364-20L716-228q-21 12-45 20t-51 8q-75 0-127.5-52.5T440-380q0-75 52.5-127.5T620-560q75 0 127.5 52.5T800-380q0 27-8 51t-20 45l128 128-56 56ZM620-280q42 0 71-29t29-71q0-42-29-71t-71-29q-42 0-71 29t-29 71q0 42 29 71t71 29Z"
        },
        {
          "name": "Give Directions",
          "section": "Welcome Guests",
          "target": "https://www.ucalgary.ca/about/our-campuses/campus-maps-and-room-finder",
          "viewBox": "0 -960 960 960",
          "path": "M480-80q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q146 0 255.5 91.5T872-559h-82q-19-73-68.5-130.5T600-776v16q0 33-23.5 56.5T520-680h-80v80q0 17-11.5 28.5T400-560h-80v80h80v120h-40L168-552q-3 18-5.5 36t-2.5 36q0 131 92 225t228 95v80Zm364-20L716-228q-21 12-45 20t-51 8q-75 0-127.5-52.5T440-380q0-75 52.5-127.5T620-560q75 0 127.5 52.5T800-380q0 27-8 51t-20 45l128 128-56 56ZM620-280q42 0 71-29t29-71q0-42-29-71t-71-29q-42 0-71 29t-29 71q0 42 29 71t71 29Z"
        },
        {
          "name": "Arrange Parking",
          "section": "Welcome Guests",
          "target": "https://www.ucalgary.ca/ancillary/parking",
          "viewBox": "0 -960 960 960",
          "path": "M480-80q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q146 0 255.5 91.5T872-559h-82q-19-73-68.5-130.5T600-776v16q0 33-23.5 56.5T520-680h-80v80q0 17-11.5 28.5T400-560h-80v80h80v120h-40L168-552q-3 18-5.5 36t-2.5 36q0 131 92 225t228 95v80Zm364-20L716-228q-21 12-45 20t-51 8q-75 0-127.5-52.5T440-380q0-75 52.5-127.5T620-560q75 0 127.5 52.5T800-380q0 27-8 51t-20 45l128 128-56 56ZM620-280q42 0 71-29t29-71q0-42-29-71t-71-29q-42 0-71 29t-29 71q0 42 29 71t71 29Z"
        },
        {
          "name": "Book a Campus Tour",
          "section": "Welcome Guests",
          "target": "https://choose.ucalgary.ca/events/campusVisitRequest.do",
          "viewBox": "0 -960 960 960",
          "path": "M480-80q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q146 0 255.5 91.5T872-559h-82q-19-73-68.5-130.5T600-776v16q0 33-23.5 56.5T520-680h-80v80q0 17-11.5 28.5T400-560h-80v80h80v120h-40L168-552q-3 18-5.5 36t-2.5 36q0 131 92 225t228 95v80Zm364-20L716-228q-21 12-45 20t-51 8q-75 0-127.5-52.5T440-380q0-75 52.5-127.5T620-560q75 0 127.5 52.5T800-380q0 27-8 51t-20 45l128 128-56 56ZM620-280q42 0 71-29t29-71q0-42-29-71t-71-29q-42 0-71 29t-29 71q0 42 29 71t71 29Z"
        },
        {
          "name": "Pickup a Souvenir/Gift",
          "section": "Welcome Guests",
          "target": "https://shop.ucalgary.ca/",
          "viewBox": "0 -960 960 960",
          "path": "M480-80q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q146 0 255.5 91.5T872-559h-82q-19-73-68.5-130.5T600-776v16q0 33-23.5 56.5T520-680h-80v80q0 17-11.5 28.5T400-560h-80v80h80v120h-40L168-552q-3 18-5.5 36t-2.5 36q0 131 92 225t228 95v80Zm364-20L716-228q-21 12-45 20t-51 8q-75 0-127.5-52.5T440-380q0-75 52.5-127.5T620-560q75 0 127.5 52.5T800-380q0 27-8 51t-20 45l128 128-56 56ZM620-280q42 0 71-29t29-71q0-42-29-71t-71-29q-42 0-71 29t-29 71q0 42 29 71t71 29Z"
        },
        {
          "name": "Visit Libraries/Museums",
          "section": "Welcome Guests",
          "target": "https://library.ucalgary.ca/",
          "viewBox": "0 -960 960 960",
          "path": "M480-80q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q146 0 255.5 91.5T872-559h-82q-19-73-68.5-130.5T600-776v16q0 33-23.5 56.5T520-680h-80v80q0 17-11.5 28.5T400-560h-80v80h80v120h-40L168-552q-3 18-5.5 36t-2.5 36q0 131 92 225t228 95v80Zm364-20L716-228q-21 12-45 20t-51 8q-75 0-127.5-52.5T440-380q0-75 52.5-127.5T620-560q75 0 127.5 52.5T800-380q0 27-8 51t-20 45l128 128-56 56ZM620-280q42 0 71-29t29-71q0-42-29-71t-71-29q-42 0-71 29t-29 71q0 42 29 71t71 29Z"
        },
        {
          "name": "Discover Calgary",
          "section": "Welcome Guests",
          "target": "http://www.visitcalgary.com/",
          "viewBox": "0 -960 960 960",
          "path": "M480-80q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q146 0 255.5 91.5T872-559h-82q-19-73-68.5-130.5T600-776v16q0 33-23.5 56.5T520-680h-80v80q0 17-11.5 28.5T400-560h-80v80h80v120h-40L168-552q-3 18-5.5 36t-2.5 36q0 131 92 225t228 95v80Zm364-20L716-228q-21 12-45 20t-51 8q-75 0-127.5-52.5T440-380q0-75 52.5-127.5T620-560q75 0 127.5 52.5T800-380q0 27-8 51t-20 45l128 128-56 56ZM620-280q42 0 71-29t29-71q0-42-29-71t-71-29q-42 0-71 29t-29 71q0 42 29 71t71 29Z"
        },
        {
          "name": "Discover Alberta",
          "section": "Welcome Guests",
          "target": "http://travelalberta.com/",
          "viewBox": "0 -960 960 960",
          "path": "M480-80q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q146 0 255.5 91.5T872-559h-82q-19-73-68.5-130.5T600-776v16q0 33-23.5 56.5T520-680h-80v80q0 17-11.5 28.5T400-560h-80v80h80v120h-40L168-552q-3 18-5.5 36t-2.5 36q0 131 92 225t228 95v80Zm364-20L716-228q-21 12-45 20t-51 8q-75 0-127.5-52.5T440-380q0-75 52.5-127.5T620-560q75 0 127.5 52.5T800-380q0 27-8 51t-20 45l128 128-56 56ZM620-280q42 0 71-29t29-71q0-42-29-71t-71-29q-42 0-71 29t-29 71q0 42 29 71t71 29Z"
        },
        {
          "name": "UC Safety App",
          "section": "Stay Safe",
          "target": "https://ucalgary.ca/risk/emergency-management/emergency-communication/uc-emergency-mobile",
          "viewBox": "0 -960 960 960",
          "path": "M200-160v-80h64l79-263q8-26 29.5-41.5T420-560h120q26 0 47.5 15.5T617-503l79 263h64v80H200Zm148-80h264l-72-240H420l-72 240Zm92-400v-200h80v200h-80Zm238 99-57-57 142-141 56 56-141 142Zm42 181v-80h200v80H720ZM282-541 141-683l56-56 142 141-57 57ZM40-360v-80h200v80H40Zm440 120Z"
        },
        {
          "name": "Accident Report (OARS)",
          "section": "Stay Safe",
          "target": "https://ucalgary.chematix.com/Oars",
          "viewBox": "0 -960 960 960",
          "path": "M200-160v-80h64l79-263q8-26 29.5-41.5T420-560h120q26 0 47.5 15.5T617-503l79 263h64v80H200Zm148-80h264l-72-240H420l-72 240Zm92-400v-200h80v200h-80Zm238 99-57-57 142-141 56 56-141 142Zm42 181v-80h200v80H720ZM282-541 141-683l56-56 142 141-57 57ZM40-360v-80h200v80H40Zm440 120Z"
        },
        {
          "name": "Contact Campus Security",
          "section": "Stay Safe",
          "target": "http://www.ucalgary.ca/security",
          "viewBox": "0 -960 960 960",
          "path": "M200-160v-80h64l79-263q8-26 29.5-41.5T420-560h120q26 0 47.5 15.5T617-503l79 263h64v80H200Zm148-80h264l-72-240H420l-72 240Zm92-400v-200h80v200h-80Zm238 99-57-57 142-141 56 56-141 142Zm42 181v-80h200v80H720ZM282-541 141-683l56-56 142 141-57 57ZM40-360v-80h200v80H40Zm440 120Z"
        },
        {
          "name": "Be Safe Working Alone",
          "section": "Stay Safe",
          "target": "https://live-risk.ucalgary.ca/risk/environment-health-safety/programs-standards-cops/working-alone",
          "viewBox": "0 -960 960 960",
          "path": "M200-160v-80h64l79-263q8-26 29.5-41.5T420-560h120q26 0 47.5 15.5T617-503l79 263h64v80H200Zm148-80h264l-72-240H420l-72 240Zm92-400v-200h80v200h-80Zm238 99-57-57 142-141 56 56-141 142Zm42 181v-80h200v80H720ZM282-541 141-683l56-56 142 141-57 57ZM40-360v-80h200v80H40Zm440 120Z"
        },
        {
          "name": "Request Safe Walk",
          "section": "Stay Safe",
          "target": "http://www.ucalgary.ca/security/safewalk",
          "viewBox": "0 -960 960 960",
          "path": "M200-160v-80h64l79-263q8-26 29.5-41.5T420-560h120q26 0 47.5 15.5T617-503l79 263h64v80H200Zm148-80h264l-72-240H420l-72 240Zm92-400v-200h80v200h-80Zm238 99-57-57 142-141 56 56-141 142Zm42 181v-80h200v80H720ZM282-541 141-683l56-56 142 141-57 57ZM40-360v-80h200v80H40Zm440 120Z"
        },
        {
          "name": "Environment, Health, Safety",
          "section": "Stay Safe",
          "target": "http://www.ucalgary.ca/safety/",
          "viewBox": "0 -960 960 960",
          "path": "M200-160v-80h64l79-263q8-26 29.5-41.5T420-560h120q26 0 47.5 15.5T617-503l79 263h64v80H200Zm148-80h264l-72-240H420l-72 240Zm92-400v-200h80v200h-80Zm238 99-57-57 142-141 56 56-141 142Zm42 181v-80h200v80H720ZM282-541 141-683l56-56 142 141-57 57ZM40-360v-80h200v80H40Zm440 120Z"
        },
        {
          "name": "Chematix",
          "section": "Stay Safe",
          "target": "https://ucalgary.chematix.com/Chematix",
          "viewBox": "0 -960 960 960",
          "path": "M200-160v-80h64l79-263q8-26 29.5-41.5T420-560h120q26 0 47.5 15.5T617-503l79 263h64v80H200Zm148-80h264l-72-240H420l-72 240Zm92-400v-200h80v200h-80Zm238 99-57-57 142-141 56 56-141 142Zm42 181v-80h200v80H720ZM282-541 141-683l56-56 142 141-57 57ZM40-360v-80h200v80H40Zm440 120Z"
        }
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
      eventLister(e) {
        const dropdown = document.getElementById("search-dropdown")
        if(!dropdown.contains(e.target)) {
            this.clearSearch()
            document.removeEventListener("click",this.eventLister)
        }
      },
      hideNavbar(){
        this.navbarVisible = false
        this.searchTerm = ""
      },
      showSearchResults(){
        document.removeEventListener("click",this.eventLister)
        if(this.searchTerm.length) {
          document.addEventListener("click",this.eventLister)
        }
        this.filteredComponents = this.componentFuse.search(this.searchTerm)
        this.filteredLinks = this.linkFuse.search(this.searchTerm)
      },
      clearSearch() {
        document.removeEventListener("click",this.eventLister)
        this.searchTerm =""
        this.filteredComponents = []
        this.filteredLinks = []
      },
      clearSearchNavigate(target) {
        document.removeEventListener("click",this.eventLister)
        this.searchTerm =""
        this.filteredComponents = []
        this.filteredLinks = []
        this.$router.push(target)
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
    this.componentFuse = new Fuse(this.components, {
      keys:['terms'],
      threshold: 0.3
    })
    this.linkFuse = new Fuse(this.links, {
      keys:['name', 'section'],
      threshold: 0.3
    })
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
  },
  watch: {
    navbarVisible: {
      handler(oldvalue, newvalue) {
        if(newvalue) {
          this.clearSearch()
        }
      }
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
