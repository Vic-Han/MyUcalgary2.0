<template>
    <!-- <div class="bg-gray-200 min-h-screen px-5 py-3">
      <div class="container mx-auto">
        <div class="flex flex-wrap -mx-2">
          <div class="w-full lg:w-1/3 px-2 mb-4" >

            <div class="flex flex-col justify-center items-center rounded-lg shadow p-8 text-center bg-white-100">

              <div class=" bg-white-100">
                <div class = "text-3xl font-bold">Cumulative GPA</div>
                <div class="mx-auto rounded-full bg-green-200 w-60 h-60 flex items-center justify-center mb-6 mt-4 flex-col relative border-8 border-green-300">
                  <span class="text-white text-6xl font-bold" style="color: #47A67C;">{{overallGPA}}</span>
                  <span class="text-white text-3xl font-bold" style="color: #47A67C;">{{letterGrade}}</span>
                </div>
                
                </div>
              <div>
                <p class="mb-4">Request Official Transcript</p>
                <p class="mb-4">View Unofficial Transcript</p>
              </div>
            </div>
            <div class="rounded-lg shadow p-4 mt-4 text-sm text-gray-800" style="background-color: #FFFFFF; height: 200px;">
              <p class="font-bold mb-7 text-base leading-relaxed text-left">Expected Graduation Date: 2024</p>
              <p class="text-base leading-normal mb-4 text-left">Deferred Examination Request</p>
              <p class="text-base leading-normal mb-4 text-left">Confirmation of Enrollment</p>
              <p class="text-base leading-normal mb-4 text-left">View Degree Requirements</p>
            </div>
          </div>
          <div class="w-full lg:w-2/3 px-2 flex-grow" style="background-color: #FFFFFF;">
            <div class="bg-white rounded-lg shadow p-4" style="padding-top: 20px; padding-bottom: 20px;">
              <div class="text-right mb-4">
                <select v-model="selectedSemester" class="rounded border-2 border-gray-500 focus:border-indigo-500 py-2 px-4">
                  <option v-for="semester in semesters" :key="semester" :value="semester">{{ semester }}</option>
                </select>
              </div>
  
              <div class="flex flex-wrap justify-between">
                <div class="flex flex-col items-center mr-6 ml-4" style="margin-top: -3.60rem;">
                  <div style="font-weight: bold; font-size: 20px; margin-bottom: 35px; margin-top:15px;">Semester GPA</div>
                  <div class="rounded-full w-40 h-40 flex items-center justify-center flex-col" style="border: 8px solid #FFCD00; background-color: #9D8830;">
                    <span class="text-white text-4xl font-bold" style="color: #FFCD00;">{{ semesterGPA }}</span>
                    <span class="text-white text-4xl font-bold" style="color: #FFCD00;">B+</span>
                  </div>
                </div>
              </div>
              <div class="pl-56" style="margin-top: -10.00rem;">
                <div v-for="course in selectedCourses" :key="course.id" class="flex items-center py-2 justify-between">
                  <div class="flex items-center">
                    <div class="text-lg font-medium ml-8">{{ course.name }}</div>
                    <div :class="`h-6 rounded-full ${course.barColor} relative ml-8`" :style="{ width: calculateBarWidth(course.grade) }">
                      <div class="absolute top-0 left-0 w-full h-full flex items-center justify-center">
                        <div class="text-lg font-medium">{{ course.grade }}%</div>
                      </div>
                    </div>
                  </div>
                  <div class="text-left text-black w-12">
                    <span>{{ course.letter }}</span>
                  </div>
                </div>
              </div>
              <div style="font-size: 14px; margin-top: 20px;">
                <p style="text-align: left;">Winter 2024</p>
                <p style="text-align: left;">Units Enrolled: 12</p>
                <p style="text-align: left;">Program: Schulich Sch of EN Bachelor</p>
                <p style="text-align: left;">Level: Year 4</p>
                <p style="text-align: left;">Plan: Bachelor of Science, Internship Program, Software Engineering</p>
              </div>
            </div>
            <div class="bg-white rounded-lg shadow p-4" style="padding-top: 20px; padding-bottom: 20px;">
              <div class="flex flex-wrap justify-between">
                <div class="flex flex-col items-center mr-16 ml-4">
                  <div class="rounded-full w-40 h-40 flex items-center justify-center flex-col" style="border: 8px solid #FFCD00; background-color: #9D8830;">
                    <span class="text-white text-3xl font-bold" style="color: #FFCD00;">{{ semesterGPA }}</span>
                    <span class="text-white text-3xl font-bold" style="color: #FFCD00;">B+</span>
                  </div>
                </div>
              </div>
              <div class="pl-56" style="margin-top: -10.00rem;">
                <div v-for="course in selectedCourses" :key="course.id" class="flex items-center py-2 justify-between">
                  <div class="flex items-center">
                    <div class="text-lg font-medium ml-8">{{ course.name }}</div>
                    <div :class="`h-6 rounded-full ${course.barColor} relative ml-8`" :style="{ width: calculateBarWidth(course.grade) }">
                      <div class="absolute top-0 left-0 w-full h-full flex items-center justify-center">
                        <div class="text-lg font-medium">{{ course.grade }}%</div>
                      </div>
                    </div>
                  </div>
                  <div class="text-left text-black w-12">
                    <span>{{ course.letter }}</span>
                  </div>
                </div>
              </div>
              <div style="font-size: 14px; margin-top: 20px;">
                <p style="text-align: left;">Winter 2024</p>
                <p style="text-align: left;">Units Enrolled: 12</p>
                <p style="text-align: left;">Program: Schulich Sch of EN Bachelor</p>
                <p style="text-align: left;">Level: Year 4</p>
                <p style="text-align: left;">Plan: Bachelor of Science, Internship Program, Software Engineering</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div> -->
  <div class = "flex flex-row w-full bg-grey-100">
    <div>
      <div class="flex flex-col justify-center items-center rounded-lg shadow-xl py-12 px-8 text-center bg-white-100 m-5">
        <div class = "text-3xl font-bold mb-9">
          Cumulative GPA
        </div>
        <div class="rounded-full bg-green-200 w-80 h-80 flex items-center justify-center my-7 mx-8 flex-col relative border-8 border-green-300">
          <span class="text-white text-8xl font-bold my-4" style="color: #47A67C;">{{overallGPA}}</span>
          <span class="text-white text-5xl font-bold" style="color: #47A67C;">{{overallLetterGrade}}</span>
        </div>
       
      </div>
      <div class = "flex flex-col rounded-xl shadow-xl py-12 px-8 text-center bg-white-100 m-5">
        <div class="font-bold my-4 text-base leading-relaxed">Expected Graduation Date: 2024</div>
        <div class="text-base leading-normal my-3 ">Confirmation of Enrollment</div>
        <div class = "text-grey-200 my-3"> Request Official Transcript </div>
        <div class = "text-grey-200 my-3"> View Unofficial Transcript </div>
      </div>
    </div>
    <div class = " bg-white-100 rounded-xl shadow-2xl h-fit mx-1 my-5 px-4 py-1 flex flex-col">
      <select v-model="selectedOption" class=" relative w-64 left-2/3 mr-40 rounded-lg border-2 border-gray-500 focus:border-indigo-500 py-2 px-4 m-3">
        <option v-for="(value, key) in termViews" :key="key">{{ key }}</option>
      </select>
      <div v-for="(value, key) in termViews[selectedOption]" :key="key" class = "my-3">
        <GradePreview :term="key" :average = "value.TermGPA" :letter = "value.TermLetterGrade"
          :courses = "value.courses" :year = "value.Level" :unitsEnrolled = "value.UnitsEnrolled"
          :plan = "value.Plan" :program ="value.Program"></GradePreview>
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
    components: {
        GradePreview
    },
    data() {
        return {
            overallGPA: 0,
            overallLetterGrade: '',
            selectedOption: '',
            termViews: {

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
        }
    },
    created(){
      this.$emit('show-navbar')
      this.$emit('toggle-selected', 'grades');
        const backendPayload = {
          "overallGPA": 3.71,
          "letterGrade": "A-",
          "activity": {
            "Fall 2023" : {
                  "UnitsEnrolled": 15,
                  "Program": "Schulich Sch of EN Bachelor",
                  "Level": 4,
                  "Plan": "Bachelor of Science, Internship Program, Software Engineering",
                  "TermGPA": 3.6,
                  "TermLetterGrade": "A-",
                  "courses" : [
                      {
                          "name" : "SENG 550",
                          "letter": "A"
                      },
                      {
                          "name" : "SENG 513",
                          "letter" : "A"
                      },
                      {
                          "name" : "CPSC 481",
                          "letter": "A-"
                      },
                      {
                          "name" : "CPSC 411",
                          "letter" : "B"
                      },
                      {
                          "name" : "ECON 341",
                          "letter": "B+"
                      },
                      {
                          "name" : "VICT 301",
                          "letter": "A+"
                      }
                  ]
              },
              "Winter 2024" : {
                  "UnitsEnrolled": 15,
                  "Program": "Schulich Sch of EN Bachelor",
                  "Level": 4,
                  "Plan": "Bachelor of Science, Internship Program, Software Engineering",
                  "TermGPA": 3.6,
                  "TermLetterGrade": "A-",
                  "courses" : [
                      {
                          "name" : "SENG 550",
                          "letter": "A"
                      },
                      {
                          "name" : "SENG 513",
                          "letter" : "A"
                      },
                      {
                          "name" : "ECON 341",
                          "letter": "B+"
                      },
                      {
                          "name" : "CPSC 411",
                          "letter" : "B"
                      },
                      {
                          "name" : "ECON 341",
                          "letter": "B+"
                      }
                  ]
              },
              "Winter 2023" : {
                  "Units Enrolled": 12,
                  "Program": "Schulich Sch of EN Bachelor",
                  "Level": 3,
                  "Plan": "Bachelor of Science, Internship Program, Software Engineering",
                  "TermGPA": 3.15,
                  "TermLetterGrade": "A-",
                  "courses" : [
                      {
                          "name" : "CPSC 441",
                          "letter": "C-"
                      },
                      {
                          "name" : "CPSC 599",
                          "letter" : "A"
                      },
                      {
                          "name" : "CPSC 457",
                          "letter": "A"
                      },
                      {
                          "name" : "SENG 300",
                          "letter" : "B"
                      }

                  ]
              }
          }
      }
      console.log(backendPayload)
      this.overallGPA = backendPayload.overallGPA
      this.overallLetterGrade = backendPayload.letterGrade
      for(const [key, value] of Object.entries(backendPayload.activity)){
        if (!this.termViews[this.termToYear(key)]) {
          this.termViews[this.termToYear(key)] = {};
        }
        this.termViews[this.termToYear(key)][key] = value
      }
      this.selectedOption = Object.keys(this.termViews)[0]
      console.log(this.termViews)
    }
};
</script>
