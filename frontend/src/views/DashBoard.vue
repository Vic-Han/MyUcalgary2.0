<!-- This is the primary dashboard component that is active when the route is dashboard -->
<template>
    <div class = "component">
        This is the dashboard heehe
        <SchedPreview/>        
        <CalendarPreview/>
        <router-link to = "grades"> 
            <GradePreview :term="GradePreview.term" :average = "GradePreview.TermGPA" :letter = "GradePreview.TermLetterGrade"
          :courses = "GradePreview.courses" :year = "GradePreview.Level" :unitsEnrolled = "GradePreview.UnitsEnrolled"
          :plan = "GradePreview.Plan" :program ="GradePreview.Program"></GradePreview>
        </router-link>
        <router-link to ="/finances">
            <FinancePieChart/>
        </router-link>
    </div>
</template>


<script>
import CalendarPreview from '../components/CalendarPreview'
import GradePreview from '../components/GradePreview'
import FinancePieChart from '../components/FinancePieChart'
import SchedPreview from '../components/SchedPreview'
    export default{
        name: 'DashBoard',
        components: {
            CalendarPreview,
            GradePreview,
            FinancePieChart,
            SchedPreview
        },
        data: () =>{
            return{
                GradePreview : {
                    term: "Fall 2023",
                    
                      UnitsEnrolled: 15,
                      Program: "Schulich Sch of EN Bachelor",
                      Level: 4,
                      Plan: "Bachelor of Science, Internship Program, Software Engineering",
                      TermGPA: 3.6,
                      TermLetterGrade: "A-",
                      courses : [
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
                              "letter": "B"
                          },
                          {
                              "name" : "ECON 341",
                              "letter": "B+"
                          }
                      ]
                  },
                
            }
        },
        created(){
            this.$emit('show-navbar')
            this.$emit('show-search')
            this.$emit('show-profile')
        }
    }
</script>