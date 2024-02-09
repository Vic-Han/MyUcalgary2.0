<template>
    <div class = "component">
        This is the misc Component
    </div>
</template>

<script>
    export default{
        name : 'MiscLinks',
        components:{
            
        },
        created(){
            this.$emit('show-navbar')
            this.$emit('show-search')
            this.$emit('show-profile')
        }
    }
</script>