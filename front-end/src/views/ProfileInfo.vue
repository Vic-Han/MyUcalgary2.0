<!-- This is the Profile Info component that toggles when the route is set to profile -->
<template>
    <AppNavbar/>
    <div class = "component">
        This is the Profile component
    </div>
</template>

<script>
import AppNavbar from '../components/AppNavbar'
    export default{
        name : 'ProfileInfo',
        components:{
            AppNavbar
        },
    }
</script>