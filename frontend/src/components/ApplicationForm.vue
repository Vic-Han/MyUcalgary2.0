<template> 
  <div class="bg-white-100 w-full rounded-xl drop-shadow-xl h-200 m-b-4">
    <div class="relative flex flex-row">
      <div class="p-4 font-semibold text-3xl">New Application</div>
      <div class="absolute m-4 h-10 w-10 right-0 fill-grey-200 hover:fill-red-100 cursor-pointer" @click="close">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10" viewBox="0 -960 960 960">
          <path d="m256-200-56-56 224-224-224-224 56-56 224 224 224-224 56 56-224 224 224 224-56 56-224-224-224 224Z"/>
        </svg>
      </div>
    </div>
    <div class="flex flex-col divide-y-2 divide-dashed divide-gray-300 px-2">
      <div class="flex flex-row pl-4 py-2">
        <div class="flex flex-col pl-4 pt-4 mr-52">
          <div class="font-semibold text-xl">Application Type:</div>
          <select v-model="selectedType" class="h-8 w-40 border-2 border-grey-200 rounded-lg pl-1 outline-blue-500 focus:border-blue-500">
            <option v-for="option in applicationTypes" :selected="option == selectedType" :value="option" :key="option">{{option}}</option>
          </select>
        </div>
        <div v-if="selectedType === 'Undergrad'" class="">
          <img src="../assets/UndergradApplication.png" alt="graduation cap" class="h-80 w-144 square shadow-inner border-2 border-gray-300 rounded-xl mt-5"/>
        </div>
        <div v-else-if="selectedType === 'Graduate'" class="">
          <img src="../assets/GraduateApplication.png" alt="graduation cap" class="h-80 w-144 square shadow-inner border-2 border-gray-300 rounded-xl mt-5"/>
        </div>
        <div v-else-if="selectedType === 'Award'" class="">
          <img src="../assets/AwardApplication.png" alt="graduation cap" class="h-80 w-144 square shadow-inner border-2 border-gray-300 rounded-xl mt-5"/>
        </div>
        <div v-else class="">
          <img src="../assets/ScholarshipApplication.png" alt="graduation cap" class="h-80 w-144 square shadow-inner border-2 border-gray-300 rounded-xl mt-5"/>
        </div>
      </div>
      <div v-if="selectedType === 'Undergrad' || selectedType === 'Graduate'" class="flex flex-col pt-4 pl-4 items-start">
        <div class="font-semibold text-xl">Faculty:</div>
        <select v-model="selectedFaculty" class="h-8 w-40 border-2 border-grey-200 rounded-lg pl-1 outline-blue-500 focus:border-blue-500">
          <option v-for="option in Object.keys(faculties)" :value="option" :key="option">{{option}}</option>
        </select>
        <div v-if="selectedFaculty!= ''" class="font-semibold text-xl">Program:</div>
        <select v-model="selectedProgram" v-if="selectedFaculty!= ''" class="h-8 w-64 border-2 border-grey-200 rounded-lg pl-1 outline-blue-500 focus:border-blue-500">
          <option v-for="option in Object.keys(faculties[selectedFaculty])" :value="option" :key="option">{{option}}</option>
        </select>
      </div>
      <div v-if="selectedType === 'Undergrad' && selectedProgram != ''" class="flex flex-col pt-4 pl-4 items-start">
        <div class="font-semibold text-xl">Concentration:</div>
        <select v-model="selectedConcentration" class="h-8 w-40 border-2 border-grey-200 rounded-lg pl-1 outline-blue-500 focus:border-blue-500">
          <option v-for="option in faculties[selectedFaculty][selectedProgram]" :value="option" :key="option">{{option}}</option>
        </select>
        <div class="font-semibold text-xl">Minor:</div>
        <select v-if="selectedType === 'Undergrad' && selectedProgram != ''" v-model="selectedMinor" class="h-8 w-40 border-2 border-grey-200 rounded-lg pl-1 outline-blue-500 focus:border-blue-500">
          <option v-for="option in Object.keys(faculties[selectedFaculty]).filter(i => i !== selectedProgram)" :value="option" :key="option">{{option}}</option>
        </select>
      </div>
      <div v-if="selectedType === 'Award'" class="flex flex-col pt-4 pl-4 items-start">
        <div class="font-semibold text-xl">Award:</div>
        <select v-model="selectedAward" class="h-8 w-40 border-2 border-grey-200 rounded-lg pl-1 outline-blue-500 focus:border-blue-500">
          <option v-for="option in awardOptions" :value="option" :key="option">{{option}}</option>
        </select>
      </div>
      <div v-else-if="selectedType === 'Scholarship'" class="flex flex-col pt-4 pl-4 items-start">
        <div class="font-semibold text-xl">Scholarship:</div>
        <select v-model="selectedScholarship" class="h-8 w-40 border-2 border-grey-200 rounded-lg pl-1 outline-blue-500 focus:border-blue-500">
          <option v-for="option in scholarShipOptions" :value="option" :key="option">{{option}}</option>
        </select>
      </div>
    </div>
    <div v-if="selectedConcentration !== '' &&  selectedType === 'Undergrad'" @click="submit" class="absolute bottom-4 right-6 h-12 pt-1.5 w-32 border-red-100 border-4 font-semibold text-xl text-red-100 rounded-xl hover:bg-red-100 cursor-pointer hover:text-white-100"> Submit </div>
    <div v-else-if="selectedProgram !== '' &&  selectedType === 'Graduate'" @click="submit" class="absolute bottom-4 right-6 h-12 pt-1.5 w-32 border-red-100 border-4 font-semibold text-xl text-red-100 rounded-xl hover:bg-red-100 cursor-pointer hover:text-white-100"> Submit </div>
    <div v-else-if="selectedAward !== ''" @click="submit" class="absolute bottom-4 right-6 h-12 pt-1.5 w-32 border-red-100 border-4 font-semibold text-xl text-red-100 rounded-xl hover:bg-red-100 cursor-pointer hover:text-white-100"> Submit </div>
    <div v-else-if="selectedScholarship !==''" @click="submit" class="absolute bottom-4 right-6 h-12 pt-1.5 w-32 border-red-100 border-4 font-semibold text-xl text-red-100 rounded-xl hover:bg-red-100 cursor-pointer hover:text-white-100"> Submit </div>
    <div v-else class="absolute bottom-4 right-6 h-12 pt-1.5 w-32 border-grey-200 border-4 font-semibold text-xl text-grey-200 rounded-xl">Submit</div>
  </div>
</template>




<script>

export default {
  name: 'ApplicationForm',
  props : {
    default :{
        type: String,
        required: true
    }
  },
  data() {
    return {
      currentStep: 1,
      
      selectedType: '',
      applicationTypes: [
          'Undergrad',
          'Graduate',
          'Award',
          'Scholarship'
      ],
      selectedProgram: '',
      selectedFaculty: '',
      selectedConcentration: '',
      faculties: {
          "Engineering" :{
            'Software Engineering' : [
              'concentration1',
              'concentration2'
            ]
          },
          "Science":{
            'Computer Science' : [
              'concentration1',
              'concentration2'
            ],
            'Biology' : [
              'concentration1',
              'concentration2'
            ]
          },
          "Arts":{
            'English Literature':[
              'concentration1',
              'concentration2'
            ]
          }
        },


      selectedMinor: '',
      selectedScholarship: '',
      selectedAward: '',
      scholarShipOptions: [
          'scholarship1',
          'scholarship2',
          'scholarship3'
      ],
      awardOptions:[  
          'award1',
          'award2',
          'award3'
      ],
      


    }
    
  },
  created() {
    this.selectedType = this.default
  },
  watch:{
   selectedType:{
      handler(){
        this.selectedFaculty = ''
        this.selectedProgram = ''
        this.selectedConcentration = ''
        this.selectedScholarship = ''
        this.selectedAward = ''
      }
   },
    selectedFaculty:{
      handler(){
        this.selectedProgram = ''
        this.selectedConcentration = ''
      }
    },
    selectedProgram:{
      handler(){
        this.selectedConcentration = ''
      }
    },

  },
  methods: {
    close() {
      this.$emit('cancel')
    },
    submit() {
      const serverPath = this.$store.state.serverPath
      const apiPath = "/api/student-applications/"
      const headers ={
        'Authorization' :`Token ${this.$cookies.get("auth-token")}`
      }
      const body = new FormData()
      if(this.selectedType === 'undergrad'){
        body.append('type', 'undergrad')
        body.append('major', this.selectedProgram)
        body.append('minor', this.selectedConcentration)
        body.append('concentration', this.selectedConcentration)
      }
      else if(this.selectedType === 'grad'){
        body.append('type', 'grad')
        body.append('program', this.selectedProgram)
      }
      else if(this.selectedType === 'award'){
        body.append('type', 'award')
        body.append('award', this.selectedAward)
      }
      else if(this.selectedType === 'scholarship'){
        body.append('type', 'scholarship')
        body.append('scholarship', this.selectedScholarship)
      }


      this.$http.post(`${serverPath}${apiPath}`, body, {headers}).then(response => {
        console.log(response.data)
        this.$emit('submit')
      }).catch(error => {
        console.log(error)
      })
      this.$emit('submit')
    },
  },


}
</script>

<style scoped>
select{
  margin: 10px;
}
</style>