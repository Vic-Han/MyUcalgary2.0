<template> 
  <div class="bg-white-100 w-full ">
    <div @click="close"> Close </div>
    <select v-model="selectedType" class="h-40 w-96">
      <option v-for="option in applicationTypes" :selected="option == selectedType" :value="option" :key="option">{{option}}</option>
    </select>
    <div v-if="selectedType !== ''">
      Hi
      <div v-if="selectedType === 'undergrad' || selectedType === 'grad'" class="flex flex-col">
          <select v-model="selectedFaculty">
            <option value=""></option>

            <option v-for="option in Object.keys(faculties)" :value="option" :key="option">{{option}}</option>
          </select>
          <select v-model="selectedProgram" v-if="selectedFaculty!= ''">
            <option value=""></option>

            <option v-for="option in Object.keys(faculties[selectedFaculty])" :value="option" :key="option">{{option}}</option>
          </select>
          <select v-if="selectedType === 'undergrad' && selectedProgram != ''" v-model="selectedConcentration">
            <option value=""></option>

            <option v-for="option in faculties[selectedFaculty][selectedProgram]" :value="option" :key="option">{{option}}</option>
          </select>
          <select v-if="selectedType === 'undergrad' && selectedProgram != ''" v-model="selectedMinor">
            <option value=""></option>

            <option v-for="option in Object.keys(faculties[selectedFaculty]).filter(i => i !== selectedProgram)" :value="option" :key="option">{{option}}</option>
          </select>
          <div v-if="selectedConcentration !== '' &&  selectedType === 'undergrad'" @click="submit"> Submit </div>
          <div v-if="selectedProgram !== '' &&  selectedType === 'grad'" @click="submit"> Submit </div>

      </div>
      <div v-else-if="selectedType === 'award'">
          
          <select v-model="selectedAward">
            <option value=""></option>


            <option v-for="option in awardOptions" :value="option" :key="option">{{option}}</option>
          </select>
          <div v-if="selectedAward !== ''" @click="submit"> Submit </div>

      </div>
      <div v-else-if="selectedType === 'scholarship'">
          <select v-model="selectedScholarship">
            <option value=""></option>

              <option v-for="option in scholarShipOptions" :value="option" :key="option">{{option}}</option>
          </select>
          <div v-if="selectedScholarship !== ''" @click="submit"> Submit </div>
      </div>
    </div>
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
      faculties: {
          "engineering" :{
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
            'bio' : [
              'concentration1',
              'concentration2'
            ]
          },
          "arts":{
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