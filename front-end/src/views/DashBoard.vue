<!-- This is the primary dashboard component that is active when the route is dashboard -->
<template>
    <AppNavbar/>
    <div class = "component">
        This is the dashboard heehe
        <SchedPreview/>        
        <CalendarPreview/>
        <router-link to = "grades" class = "btn"> 
            <GradePreview/>
        </router-link>
        <router-link to ="/finances">
            <FinancePieChart/>
        </router-link>
    </div>
</template>


<script>
import AppNavbar from '../components/AppNavbar'
import CalendarPreview from '../components/CalendarPreview'
import GradePreview from '../components/GradePreview'
import FinancePieChart from '../components/FinancePieChart'
import SchedPreview from '../components/SchedPreview'
    export default{
        name: 'DashBoard',
        components: {
            AppNavbar,
            CalendarPreview,
            GradePreview,
            FinancePieChart,
            SchedPreview
        }
    }
</script>