<template>
    <div class = "component">
        This is the Settings Component
        <div class = "btn" @click="logout">
            OMG I made it so that when you click this it logs out! Use @click="logout" in case you can't read
        </div>
        <div class = "sub-component">
            Thanks for fixing this callum. I have no idea whats supposed to go here
        </div>
        <div class ="sub-component">
            <div class = "btn"> 
                <div class = "component">
                Best Regards, Victor
                </div>
            </div>
            
        </div>
    </div>
</template>

<script>
    export default{
        name : 'PersonalSettings',
        methods:{
            logout(){
                this.$cookies.remove('auth-token')
                this.$router.push('/')
            }
        },
        created(){
            this.$emit('show-navbar')
        }
    }
</script>