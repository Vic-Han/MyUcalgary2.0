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
          <div class="flex flex-row p-20 h-128 box-content border-x border-grey-200 border-b rounded-b-xl" v-if="selected === 'ugrad'">
            <div v-for="(app,index) in ugradApps" :key="index" class="bg-grey-100">
              <div>Faculty: {{app.faculty}}</div>
              <div>Program: {{app.program}}</div>
              <div>Major: {{app.major}}</div>
              <div>Minor: {{app.minor}}</div>
              <div>Concentration: {{app.concentration}}</div>
              <div>Status: {{app.status}}</div>
            </div>
          </div>
          <div class="flex flex-row p-20 h-128 box-content border-x border-grey-200 border-b rounded-b-xl" v-else-if="selected === 'award'">
            <div v-for="(award,index) in awards" :key="index" class="border border-black-100 p-3">
              <div>Name: {{award.name}}</div>
              <div>Amount: {{award.amount}}</div>
              <div>Status: {{award.status}}</div>
            </div>
          </div>
          <div class="flex flex-row p-20 h-128 box-content border-x border-grey-200 border-b rounded-b-xl" v-else-if="selected === 'scholarship'">
            <div v-for="(scholarship,index) in scholarships" :key="index" class="border border-black-100 p-3">
              <div>Name: {{scholarship.name}}</div>
              <div>Amount: {{scholarship.amount}}</div>
              <div>Status: {{scholarship.status}}</div>
            </div>
          </div>
          <div class="flex flex-row p-20 h-128 box-content border-x border-grey-200 border-b rounded-b-xl" v-else-if="selected === 'grad'">
            <div v-for="(app,index) in gradApps" :key="index" class="border border-black-100 p-3 m-5">
              <div>Faculty: {{app.faculty}}</div>
              <div>Program: {{app.program}}</div>
              <div>Major: {{app.major}}</div>
              <div>Type: {{app.type}}</div>
              <div>Advisor: {{app.Advisor}}</div>
              <div>Status: {{app.status}}</div>
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
    }],
    "awards": []
    }
    this.ugradApps = backend["Undergrad applications"]
    this.scholarships = backend["Scholarships"]
    this.gradApps = backend["Graduate applications"]
  }
}
</script>

