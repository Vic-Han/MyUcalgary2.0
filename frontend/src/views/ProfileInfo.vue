<!-- This is the Profile Info component that toggles when the route is set to profile -->
<template>
    <div class = "component">
        This is the Profile component
        <div @click = "back" class = "btn">
            Let's go back to the screen we came from
        </div>
    </div>
</template>

<script>
    export default{
        name : 'ProfileInfo',
        components:{
            
        },
        created(){
            this.$emit('show-navbar')
            this.$emit('toggle-selected', 'profile')
        }, 
        methods:{
            back(){
                this.$router.go(-1)
            }
        },
    }
</script>