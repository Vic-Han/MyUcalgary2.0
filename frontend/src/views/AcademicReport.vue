<!-- This is the  academics component that is active when the route is academics -->

<template>

    <div class = "component">
        This is the AcademicReport Component
    </div>
</template>

<script>

    export default{
        name : 'AcademicReport',
        components:{
            
        },
        created(){
            this.$emit('show-navbar')
            this.$emit('show-search')
            this.$emit('show-profile')
            this.$emit('set-title','Academic Report')
        }
    }
</script>