<template>
  <div class="flex flex-row w-full bg-grey-100">
    <div>
      <div class="flex flex-col justify-center items-center rounded-lg shadow-xl py-12 px-8 text-center bg-white-100 m-5">
        <div class="text-3xl font-bold mb-9">
          Cumulative GPA
        </div>
        <div class="rounded-full w-80 h-80 flex items-center justify-center my-7 mx-8 flex-col relative border-8" :class="gpaColours(overallLetterGrade)" >
          <span class="text-8xl font-bold my-4" :class="gpaText(overallLetterGrade)" >{{overallGPA.toFixed(2)}}</span>
          <span class="text-5xl font-bold" :class="gpaText(overallLetterGrade)">{{overallLetterGrade}}</span>
        </div>
       
      </div>
      <div class="flex flex-col rounded-xl shadow-xl py-12 px-8 text-center bg-white-100 m-5">
        <div class="font-bold my-4 text-base leading-relaxed">Level: {{currentStudentInfo.level}}</div>
        <div class="text-base text-grey-200 leading-normal my-3 ">Plan: {{ currentStudentInfo.plan }}</div>
        <div class="text-grey-200 my-3"> Program: {{ currentStudentInfo.program }} </div>
        <div class="text-grey-200 my-3"> Keep This here until you find a way to make the height identical </div>
      </div>
    </div>
    <div class="bg-white-100 rounded-xl shadow-2xl h-fit mx-1 my-5 px-4 py-1 flex flex-col">
      <select v-model="selectedOption" class=" relative left-2/3 w-64 mr-40 rounded-lg border-2 border-grey-200 focus:border-blue-500 py-2 px-4 m-3">
        <option class="selected:bg-red-100" v-for="(value, key) in termViews" :key="key">{{ key }}</option>
      </select>
      <div v-for="(value, key) in termViews[selectedOption]" :key="key" class="my-5">
        <GradePreview :term="key" :average="value.TermGPA.toFixed(2)" :letter="value.TermLetterGrade"
          :courses="value.courses" :year="value.Level" :unitsEnrolled="value.UnitsEnrolled"
          :plan="value.Plan" :program="value.Program"></GradePreview>
      </div>
      <div>

      </div>
    </div>
  </div>
  </template>
  
<script>
import GradePreview from '@/components/GradePreview.vue';
  export default {
    name: 'GradeBreakdown',
    emits: ['show-navbar', 'toggle-selected'],
    components: {
        GradePreview
    },
    data() {
        return {
            overallGPA: 0,
            overallLetterGrade: '',
            selectedOption: '',
            termViews: {

            },
            currentStudentInfo:{

            }
        };
    },
    computed: {
        selectedCourses() {
            return this.courses[this.selectedSemester] || [];
        },
        semesterGPA() {
            return '3.32'; // This should be computed based on actual courses and grades.
        },
    },
    methods: {
        calculateBarWidth(grade) {
            const maxGrade = Math.max(...this.selectedCourses.map(course => course.grade));
            const maxWidth = 200; // Maximum width
            const width = (grade / maxGrade) * maxWidth;
            return `${width}px`;
        },
        updateSelectedSemester(event) {
            this.selectedSemester = event.target.value;
            // You may need to add additional logic to update the courses and GPA based on the selected year.
        },
        termToYear(termName){
            const arr = termName.split(" ")
            const year = arr[1]
            const term = arr[0]
            if(term === "Fall"){
              return "Academic Year " + year + "-" + (parseInt(year)  + 1)
            }
            else if (term === "Winter"){
              return "Academic Year " + (parseInt(year) - 1) + "-" + year
            }
            else if (term === "Summer" || term === "Spring"){
              return "Spring/Summer " + year
            }
        },
        gpaColours(letterGrade) {
          if(letterGrade[0] == 'A') {
            return "border-grade-A bg-grade-A-background"
          }
          if(letterGrade[0] == 'B') {
            return "border-grade-B bg-grade-B-background"
          }
          if(letterGrade[0] == 'C') {
            return "border-grade-C bg-grade-C-background"
          }
          else {
            return "border-grade-D bg-grade-D-background"
          }
        },
        gpaText(letterGrade) {
          if(letterGrade[0] == 'A') {
            return "text-grade-A"
          }
          if(letterGrade[0] == 'B') {
            return "text-grade-B"
          }
          if(letterGrade[0] == 'C') {
            return "text-grade-C"
          }
          else {
            return "text-grade-D"
          }
        }
    },
    created(){
      this.$emit('show-navbar')
      this.$emit('toggle-selected', 'grades');
     
      
      const serverpath = this.$store.state.serverPath
      const apiPath = "/api/student-grades"
      const headers = {
          'Content-Type': 'application/json',
          'Authorization' :`Token ${this.$cookies.get("auth-token")}`
      }


      this.$http.get(`${serverpath}${apiPath}`,{headers}).then(response => {
        const data = response.data
        console.log(data)
        this.overallGPA = data.overallGPA
        this.overallLetterGrade = data.letterGrade
        for(const [key, value] of Object.entries(data.activity)){
          if (!this.termViews[this.termToYear(key)]) {
            this.termViews[this.termToYear(key)] = {};
          }
          this.termViews[this.termToYear(key)][key] = value
        }
        this.selectedOption = Object.keys(this.termViews)[0]
        this.currentStudentInfo = data.currentStudentInfo


      }).catch(error => {
        console.log(error)
      } )

    }
};
</script>
