<template>

    <div class = "component">
        This is the GradeBreakdown Component
        <router-link to ="/dashboard" class = "btn">
            This is boring go look at the dashboard
        </router-link>
    </div>
</template>

<script>
    export default{
        name : 'GradeBreakdown',
        components:{
            
        },
        data : () =>{

        },
        created() {
            this.$emit('show-navbar')
            this.$emit('show-search')
            this.$emit('show-profile')
        }
    }
</script>