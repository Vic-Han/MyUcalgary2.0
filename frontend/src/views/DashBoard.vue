<!-- This is the primary dashboard component that is active when the route is dashboard -->
<template>
    <div class="px-4 py-4 w-full h-fit gap-4 bg-grey-100 grid grid-cols-3 grid-rows-5 shadow-inner">
        <router-link to="schedule" class=" flex items-center justify-items-center col-span-2 px-2 py-4 row-span-3 bg-white-100 rounded-xl shadow-lg"> 
            <SchedPreview :schedule="Schedule"/> 
        </router-link>
        <div class="col-start-3 row-span-3 bg-white-100 rounded-xl shadow-lg"><CalendarPreview/></div>
        <router-link to="finances" class="row-start-4 row-span-2 bg-white-100 rounded-xl h-80 shadow-lg">
            <FinancePieChart :term="FinancePreview.term" :amount="FinancePreview.amount" :status="FinancePreview.status" :due="FinancePreview.due"/>
        </router-link>
        <router-link to="grades" class="relative pt-8 row-start-4 col-start-2 col-span-2 row-span-2 h-80 bg-white-100 rounded-xl shadow-lg">
            <GradePreview :term="GradePreview.term" :average="GradePreview.TermGPA" :letter="GradePreview.TermLetterGrade"
                :courses="GradePreview.courses" :year="GradePreview.Level" :unitsEnrolled="GradePreview.UnitsEnrolled"
                :plan="GradePreview.Plan" :program="GradePreview.Program" :dashboardView="true">
            </GradePreview>
        </router-link>
    </div>

</template>
  

<script>
import CalendarPreview from '../components/CalendarPreview'
import GradePreview from '../components/GradePreview'
import FinancePieChart from '../components/FinancePieChart'
import SchedPreview from '../components/SchedPreview'
import Data from './SampleSched.json'
    export default{
        name: 'DashBoard',
        components: {
            CalendarPreview,
            GradePreview,
            FinancePieChart,
            SchedPreview
        },
        emits: ['show-navbar', 'toggle-selected'],
        data: () =>{
            return{
                Schedule: Data,
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
                          },
                      ]
                },
                FinancePreview: {
                    term: "Winter 2024",
                    amount: "3,125.03",
                    status: "Paid",
                    due: "February 25, 2024"
                }
                
            }
        },
        methods: {
            fetchData(){
                const serverpath = this.$store.state.serverPath
                const apiPath = '/api/dashboard'
               
                const headers = {
                    'Content-Type': 'application/json',
                    'Authorization' :`Token ${this.$cookies.get("auth-token")}`
                }

                this.$http.get(`${serverpath}${apiPath}`,{headers}).then(response => {
                    const data = response.data
                    console.log(data)
                    for(const [key,value] of Object.entries(data.grades)){
                        this.GradePreview.term = key
                        this.GradePreview.TermGPA = value.TermGPA
                        this.GradePreview.TermLetterGrade = value.TermLetterGrade
                        this.GradePreview.courses = value.courses
                    }
                    for(const [key,value] of Object.entries(data.finances)){
                        this.FinancePreview.term = key
                        this.FinancePreview.amount = value.net_balance
                        this.FinancePreview.status = value.debits > 0 ? "Unpaid" : "Paid"
                        this.FinancePreview.due = value.due
                    }
                    this.Schedule = data.schedule

                }).catch(error => {
                    console.log(error)
                } )
            }
        },
        created(){
            this.$emit('show-navbar')
            this.$emit('toggle-selected', 'dashboard')
            this.fetchData()
    }
}
</script>