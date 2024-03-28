<template>
    <router-link to="/profile" class="flex items-center no-underline text-black font-bold">
        <div class="flex items-center justify-center w-12 h-12 rounded-full bg-white-100 mr-2 text-rubine-100 border border-rubine-100 hover:text-white-100 hover:bg-rubine-100 ">
            {{initials}}
        </div>
    </router-link>
</template>  

<script>


    export default{
        name : 'ProfilePreview',
        data: ()=>{
            return {
                initials: ""
            }
        },
        created(){
            this.initials = this.$cookies.get('initials').toUpperCase()
        }
    }
   
</script>