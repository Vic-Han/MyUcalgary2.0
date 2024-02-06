
<template>
    <AppNavbar/>

    <div class = "component">
        This is the FinanceBreakdown Component
        <router-link to ="/dashboard" class = "btn">
            You're broke anyways so go back to the dashboard
        </router-link>
    </div>
</template>

<script>
import AppNavbar from '../components/AppNavbar'
    export default{
        name : 'FinanceBreakdown',
        components:{
            AppNavbar
        },
    }
</script>