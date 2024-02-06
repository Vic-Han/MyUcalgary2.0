<template>
    <AppNavbar/>

    <div class = "component">
        This is the GradeBreakdown Component
        <router-link to ="/dashboard" class = "btn">
            This is boring go look at the dashboard
        </router-link>
    </div>
</template>

<script>
import AppNavbar from '../components/AppNavbar'
    export default{
        name : 'GradeBreakdown',
        components:{
            AppNavbar
        },
    }
</script>