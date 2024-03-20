<template> 
  <div>
      <ApplicationForm v-if="applicationForm" @cancel="closeApplicationForm" @submit="closeApplicationForm"/>
      <div v-else class="bg-white-100 w-full rounded-xl">
        <div class="text-left p-5 text-3xl text-grey-200"> My Applications </div>
        <div class = "flex flex-row px-20">
          <div class="border border-grey-200 rounded-tl-lg w-1/4 py-3 bg-gray-300" 
          @click="selected='ugrad'" v-bind:class="{'bg-white-100 border-b-0' : selected==='ugrad'}"> Undergrad </div>
          <div class="border border-grey-200 w-1/4 py-3 bg-gray-300" 
          @click="selected='award'" v-bind:class="{'bg-white-100 border-b-0' : selected==='award'}"> Awards </div>
          <div class="border border-grey-200 w-1/4 py-3 bg-gray-300" 
          @click="selected='scholarship'" v-bind:class="{'bg-white-100 border-b-0' : selected==='scholarship'}"> Scholarships </div>
          <div class="border border-grey-200 rounded-tr-lg w-1/4 py-3 bg-gray-300" 
          @click="selected='grad'" v-bind:class="{'bg-white-100 border-b-0' : selected==='grad'}"> Grad</div>
        </div>
        <div class = "px-20"> 
          <div class="flex flex-row p-5 h-144 box-content border-x border-grey-200 border-b rounded-b-xl flex-wrap" v-if="selected === 'ugrad'">
            <div v-for="(app,index) in ugradApps" :key="index" class="bg-grey-100">
              <div>Faculty: {{app.faculty}}</div>
              <div>Program: {{app.program}}</div>
              <div>Major: {{app.major}}</div>
              <div>Minor: {{app.minor}}</div>
              <div>Concentration: {{app.concentration}}</div>
              <div>Status: {{app.status}}</div>
            </div>
          </div>
          <div class="flex flex-row p-5 h-144 box-content border-x border-grey-200 border-b rounded-b-xl flex-wrap" v-else-if="selected === 'award'">
            <div v-for="(award,index) in awards" :key="index" class="border border-black-100 p-3">
              <div>Name: {{award.name}}</div>
              <div>Amount: {{award.amount}}</div>
              <div>Status: {{award.status}}</div>
            </div>
          </div>
          <div class="flex flex-row p-5 h-144 box-content border-x border-grey-200 border-b rounded-b-xl flex-wrap" v-else-if="selected === 'scholarship'">
            <div v-for="(scholarship,index) in scholarships" :key="index" class="border border-black-100 p-3">
              <div>Name: {{scholarship.name}}</div>
              <div>Amount: {{scholarship.amount}}</div>
              <div>Status: {{scholarship.status}}</div>
            </div>
          </div>
          <div class="flex flex-row px-5 py-10 h-144 box-content border-x border-grey-200 border-b rounded-b-xl overflow-x-auto " v-else-if="selected === 'grad'">
            <div v-for="(app,index) in gradApps" :key="index" class="bg-grey-100 rounded-lg p-5 h-fit w-fit ml-12 mb-2 mt-12">
              <div class="flex flex-row p-2">
                <div class="text-3xl mx-2"> {{ app.program }}</div>
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -960 960 960" class="h-14 w-14 ml-36 fill-grey-200 hover:fill-red-100">
                  <path d="M280-120q-33 0-56.5-23.5T200-200v-520h-40v-80h200v-40h240v40h200v80h-40v520q0 33-23.5 56.5T680-120H280Zm80-160h80v-360h-80v360Zm160 0h80v-360h-80v360Z"/>
                </svg>
              </div>
              
              <img src="../assets/GraduateApplication.png" alt="graduation cap" class="h-80 w-144 square rounded-xl shadow-md mt-5"/>
              <div class="absolute opacity-80 top-0 text-black-100 text-xl w-96 p-2 text-left">
                <div class="my-1">Faculty: {{app.faculty}}</div>
                <div class="my-1">Program: {{app.program}}</div>
                <div class="my-1">Major: {{app.major}}</div>
                <div class="my-1">Type: {{app.type}}</div>
                <div class="my-1">Advisor: {{app.Advisor}}</div>
                <div class="my-1">Status: {{app.status}}</div>
              </div>
            </div>
          </div>
        </div>
        <div>
          <button class="bg-red-100 text-white-100 p-3 rounded-md mt-3" @click="openApplicationForm">New Application</button>
        </div>
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
      selected: "ugrad"
    }
  },
  methods: {
    openApplicationForm() {
      this.applicationForm = true
    },
    closeApplicationForm() {
      this.applicationForm = false
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
        "status": "pending"
    }],
    "Scholarships": [{
        "the primary key" : "we will use this to withdraw the application in a delete request",
        "name": "The you're a good student scholarship",
        "amount": 1000,
        "type": "idk but this is probably an enum in the back end. Or just don't include this",
        "status": "pending"
    }],
    "Graduate applications": [{
        "the primary key" : "we will use this to withdraw the application in a delete request",
        "faculty": "Faculty of Engineering",
        "program": "Master of Engineering",
        "major": "Software Engineering",
        "type": "Research",
        "Advisor": "Ronnie the sofytware architecture goat",
        "status": "pending"
    },
    {
        "the primary key" : "we will use this to withdraw the application in a delete request",
        "faculty": "Faculty of Engineering",
        "program": "Master of Engineering",
        "major": "Software Engineering",
        "type": "Research",
        "Advisor": "Ronnie the sofytware architecture goat",
        "status": "pending"
    },
    {
        "the primary key" : "we will use this to withdraw the application in a delete request",
        "faculty": "Faculty of Engineering",
        "program": "Master of Engineering",
        "major": "Software Engineering",
        "type": "Research",
        "Advisor": "Ronnie the sofytware architecture goat",
        "status": "pending"
    },
    {
        "the primary key" : "we will use this to withdraw the application in a delete request",
        "faculty": "Faculty of Engineering",
        "program": "Master of Engineering",
        "major": "Software Engineering",
        "type": "Research",
        "Advisor": "Ronnie the sofytware architecture goat",
        "status": "pending"
    }],
    "awards": []
    }
    this.ugradApps = backend["Undergrad applications"]
    this.scholarships = backend["Scholarships"]
    this.gradApps = backend["Graduate applications"]
  }
}
</script>

