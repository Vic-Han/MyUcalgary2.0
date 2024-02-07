
<template>

    <div class = "component">
        This is the FinanceBreakdown Component
        <router-link to ="/dashboard" class = "btn">
            You're broke anyways so go back to the dashboard
        </router-link>
    </div>
</template>

<script>
    export default{
        name : 'FinanceBreakdown',
        components:{
            
        },
        created(){
            this.$emit('show-navbar')
            this.$emit('show-search')
            this.$emit('show-profile')
        }
    }
</script>