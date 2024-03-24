<template> 
  <div>
      <ApplicationForm v-if="applicationForm" @cancel="closeApplicationForm" @submit="closeApplicationForm"/>
      <div v-else class="bg-white-100 w-full rounded-xl shadow-xl">
        <div class="text-left p-5 text-3xl font-semibold"> My Applications </div>
        <div class = "flex flex-row px-20">
          <div class="border border-grey-200 rounded-tl-lg w-1/4 py-3 cursor-pointer bg-gray-300" 
          @click="selected='ugrad'" v-bind:class="{'bg-white-100 border-b-0' : selected==='ugrad'}"> Undergrad </div>
          <div class="border border-grey-200 w-1/4 py-3 cursor-pointer bg-gray-300" 
          @click="selected='award'" v-bind:class="{'bg-white-100 border-b-0' : selected==='award'}"> Awards </div>
          <div class="border border-grey-200 w-1/4 py-3 cursor-pointer bg-gray-300" 
          @click="selected='scholarship'" v-bind:class="{'bg-white-100 border-b-0' : selected==='scholarship'}"> Scholarships </div>
          <div class="border border-grey-200 rounded-tr-lg w-1/4 py-3 cursor-pointer bg-gray-300" 
          @click="selected='grad'" v-bind:class="{'bg-white-100 border-b-0' : selected==='grad'}"> Grad</div>
        </div>
        <div class = "px-20"> 
          <div class="p-5 h-128 box-content border-x border-grey-200 border-b rounded-b-xl flex-wrap" v-if="selected === 'ugrad'">
            <div class="flex flex-row overflow-x-auto bg-white-200 shadow-inner p-1 h-full rounded-xl">
            <div v-if="ugradApps.length == 0" class="text-4xl text-center w-full text-grey-200 p-16 leading-loose">
              No applications for undergrad programs. You can start an application below.
            </div>
            <div v-for="(app,index) in ugradApps" :key="index" class="bg-white-100 shadow-xl rounded-xl p-5 h-fit w-fit ml-8 mb-2 mt-8" :class="{'mr-8': index == ugradApps.length -1}">
              <div class="flex flex-row p-2 justify-between w-144">
                <div class="text-3xl text-left"> {{ app.program }}</div>
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -960 960 960" class="h-10 w-10 fill-grey-200 hover:fill-red-100" @click="deleteApplication(app.ID)">
                  <path d="M280-120q-33 0-56.5-23.5T200-200v-520h-40v-80h200v-40h240v40h200v80h-40v520q0 33-23.5 56.5T680-120H280Zm80-160h80v-360h-80v360Zm160 0h80v-360h-80v360Z"/>
                </svg>
              </div>
              <div class="my-1 text-sm font-semibold text-white-100 rounded-xl w-fit h-fit px-2 py-1" :class="statusColor(app.status)">{{app.status}}</div>
              <img src="../assets/UndergradApplication.png" alt="graduation cap" class="h-80 w-144 square rounded-xl mt-5"/>

              <div class='relative'>
                <div class="absolute opacity-80 -translate-y-full -bottom-4 right-4 bg-white-100 text-black-100 text-xl w-80 py-4 px-4 text-left rounded-xl">
                  <div class="mb-1">Faculty: {{app.faculty}}</div>
                  <div class="my-1">Major: {{app.major}}</div>
                  <div class="my-1">Minor: {{app.minor}}</div>
                  <div class="mt-1">Concentration: {{app.concentration}}</div>         
                </div>
              </div>
            </div>
            </div>
          </div>
          <div class="p-5 h-128 box-content border-x border-grey-200 border-b rounded-b-xl flex-wrap" v-else-if="selected === 'award'">
            <div class="flex flex-row overflow-x-auto bg-white-200 shadow-inner p-1 h-full rounded-xl">
            <div v-if="awards.length == 0" class="text-4xl text-center w-full text-grey-200 p-20 leading-loose">
              No applications for awards. You can start an application below.
            </div>
            <div v-for="(award,index) in awards" :key="index" class="bg-white-100 shadow-xl rounded-xl p-5 h-fit w-fit ml-8 mb-2 mt-8" :class="{'mr-8': index == awards.length -1}">
              <div class="flex flex-row p-2 justify-between w-144">
                <div class="text-3xl text-left"> {{ award.name }}</div>
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -960 960 960" class="h-10 w-10 fill-grey-200 hover:fill-red-100" @click="deleteApplication(award.ID)">
                  <path d="M280-120q-33 0-56.5-23.5T200-200v-520h-40v-80h200v-40h240v40h200v80h-40v520q0 33-23.5 56.5T680-120H280Zm80-160h80v-360h-80v360Zm160 0h80v-360h-80v360Z"/>
                </svg>
              </div>
              <div class="my-1 text-sm font-semibold text-white-100 rounded-xl w-fit h-fit px-2 py-1" :class="statusColor(award.status)">{{award.status}}</div>
              <img src="../assets/AwardApplication.png" alt="graduation cap" class="h-80 w-144 square rounded-xl mt-5"/>
              
              <div class='relative'>
                <div class="absolute opacity-80 bottom-4 left-4  bg-white-100 text-black-100 text-xl w-30 p-4 text-left rounded-xl">
                  <div class="my-1"> Value: ${{award.amount}}</div>
                </div>
              </div>
            </div>
            </div>
          </div>
          <div class=" p-5 h-128 box-content border-x border-grey-200 border-b rounded-b-xl" v-else-if="selected === 'scholarship'">
            <div class="overflow-x-auto bg-white-200 shadow-inner p-1 flex flex-row h-full rounded-xl">
              <div v-if="scholarships.length === 0" class="text-4xl text-center w-full text-grey-200 p-20 leading-loose">
                No applications for scholarships. You can start an application below.
              </div>
            <div v-for="(scholarship,index) in scholarships" :key="index" class="bg-white-100 shadow-xl rounded-xl p-5 h-fit w-fit ml-8 mb-2 mt-8" :class="{'mr-8': index == scholarships.length -1}">
              <div class="flex flex-row p-2 justify-between w-144">
                <div class="text-3xl text-left"> {{ scholarship.name }}</div>
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -960 960 960" class="h-10 w-10 fill-grey-200 hover:fill-red-100" @click="deleteApplication(scholarship.ID)">
                  <path d="M280-120q-33 0-56.5-23.5T200-200v-520h-40v-80h200v-40h240v40h200v80h-40v520q0 33-23.5 56.5T680-120H280Zm80-160h80v-360h-80v360Zm160 0h80v-360h-80v360Z"/>
                </svg>
              </div>
              <div class="my-1 text-sm font-semibold text-white-100 rounded-xl w-fit h-fit px-2 py-1" :class="statusColor(scholarship.status)">{{scholarship.status}}</div>
              <img src="../assets/ScholarshipApplication.png" alt="graduation cap" class="h-80 w-144 square rounded-xl mt-5"/>
              <div class='relative'>
                <div class="absolute opacity-80 bottom-4  right-4 bg-white-100 text-black-100 text-xl w-30 p-4 text-left rounded-xl">
                  <div class="my-1"> Value: ${{scholarship.amount}}</div>
                </div>
              </div>
            </div>
            </div>
          </div>
          <div class="p-5 h-128 box-content border-x border-grey-200 border-b rounded-b-xl " v-else-if="selected === 'grad'">
            <div class="overflow-x-auto bg-white-200 shadow-inner p-1 flex flex-row h-full rounded-xl">
              <div v-if="gradApps.length == 0" class="text-4xl text-center w-full text-grey-200 p-18 leading-loose">
                No applications for graduate programs. You can start an application below.
              </div>
              <div v-for="(app,index) in gradApps" :key="index" class="bg-white-100 shadow-xl rounded-xl p-5 h-fit w-fit ml-8 mb-2 mt-8" :class="{'mr-8': index == gradApps.length -1}">
              <div class="flex flex-row p-2 justify-between w-144">
                <div class="text-3xl text-left"> {{ app.program }}</div>
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -960 960 960" class="h-10 w-10 fill-grey-200 hover:fill-red-100" @click="deleteApplication(app.ID)">
                  <path d="M280-120q-33 0-56.5-23.5T200-200v-520h-40v-80h200v-40h240v40h200v80h-40v520q0 33-23.5 56.5T680-120H280Zm80-160h80v-360h-80v360Zm160 0h80v-360h-80v360Z"/>
                </svg>
              </div>
              <div class="my-1 text-sm font-semibold text-white-100 rounded-xl w-fit h-fit px-2 py-1" :class="statusColor(app.status)">{{app.status}}</div>
              <img src="../assets/GraduateApplication.png" alt="graduation cap" class="h-80 w-144 square rounded-xl mt-5"/>
              
              <div class='relative'>
                <div class="absolute opacity-80 left-4 bottom-4 bg-white-100 text-black-100 text-xl w-80 p-4 text-left rounded-xl">
                  <div class="mb-1">Faculty: {{app.faculty}}</div>
                  <div class="my-1">Major: {{app.major}}</div>
                  <div class="my-1">Type: {{app.type}}</div>
                  <div class="mt-1">Advisor: {{app.Advisor}}</div>
                </div>
              </div>
            </div>
            </div>
          </div>
        </div>
          <button class="px-4 py-2 text-lg border-2 border-red-100 rounded-lg text-red-100 relative transition hover:bg-red-100 hover hover:text-white-100 drop-shadow-sm -translate-x-full left-1/2 my-5 -mr-2"
           @click="openApplicationForm">New Application</button>
      </div>
    </div>
</template>

<script>
import ApplicationForm from '../components/ApplicationForm'
export default {
  name: 'ApplicationHomepage',
  components: {
    ApplicationForm,
  },
  data: () => {
    return {
      applicationForm: false,
      ugradApps: [],
      scholarships: [],
      gradApps: [],
      awards: [],
      selected: "ugrad"
    }
  },
  methods: {
    openApplicationForm() {
      this.applicationForm = true
    },
    closeApplicationForm() {
      this.applicationForm = false
    },
    statusColor(status) {
      if(status === "Pending") {
        return "bg-blue-500"
      } else if(status === "Accepted") {
        return "bg-green-100"
      } else if(status === "Rejected") {
        return "bg-red-100"
      }
    },
    deleteApplication(appID) {
      // send a delete request to the backend
      return appID
    }
  },
  created() {
    this.$emit('show-navbar');
    this.$emit('toggle-selected', 'application');
    const backend = {
    "Undergrad applications": [{
        "the primary key" : "we will use this to withdraw the application in a delete request",
        "faculty": "Faculty of Engineering",
        "program": "Bachelor of Engineering",
        "major": "Software Engineering",
        "minor": "Embedded Systems",
        "concentration": "none",
        "status": "Pending"
    }],
    "Scholarships": [{
        "the primary key" : "we will use this to withdraw the application in a delete request",
        "name": "The you're a good student scholarship",
        "amount": 1000,
        "type": "idk but this is probably an enum in the back end. Or just don't include this",
        "status": "Pending"
    }],
    "Graduate applications": [{
        "the primary key" : "we will use this to withdraw the application in a delete request",
        "faculty": "Faculty of Engineering",
        "program": "Master of Engineering",
        "major": "Software Engineering",
        "type": "Research",
        "Advisor": "Ronnie the software architecture goat",
        "status": "Pending"
    },
    {
        "the primary key" : "we will use this to withdraw the application in a delete request",
        "faculty": "Faculty of Engineering",
        "program": "Master of Engineering",
        "major": "Software Engineering",
        "type": "Research",
        "Advisor": "Ronnie the software architecture goat",
        "status": "Accepted"
    },
    {
        "the primary key" : "we will use this to withdraw the application in a delete request",
        "faculty": "Faculty of Engineering",
        "program": "Master of Engineering",
        "major": "Software Engineering",
        "type": "Research",
        "Advisor": "Ronnie the software architecture goat",
        "status": "Rejected"
    },
    {
        "the primary key" : "we will use this to withdraw the application in a delete request",
        "faculty": "Faculty of Engineering",
        "program": "Master of Engineering",
        "major": "Software Engineering",
        "type": "Research",
        "Advisor": "Ronnie the software architecture goat",
        "status": "Pending"
    }],
    "awards": [{
        "the primary key" : "we will",
        "name": "The you're a good student scholarship",
        "amount": 1000,
        "type": "idk but this is probably an enum in the back end. Or just don't include this",
        "status": "Pending"
    }]
    }
    this.ugradApps = backend["Undergrad applications"]
    this.scholarships = backend["Scholarships"]
    this.gradApps = backend["Graduate applications"]
    this.awards = backend["awards"]

  }
}
</script>

