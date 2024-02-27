<!-- This is the Profile Info component that toggles when the route is set to profile -->
<template>
    <div class="bg-gray-400">
        <div class="grid grid-rows-3 grid-flow-col gap-4">
            <div class="bg-white-100 w-1/3">Personal Info</div>
            <div class="col-start-2 bg-white-100 w-1/3">Citizenship</div>
            <div class="col-start-3 row-span-2 bg-white-100 w-1/3">Address</div>
            <div class="bg-white-100 w-1/3">Phone</div>
            <div class="row-start-2 col-start-2 bg-white-100 w-1/3">Email</div>
            <div class="col-span-3 bg-white-100 w-full">Emergency Contacts</div>
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
            this.$emit('show-search')
            this.$emit('show-profile')
        }, 
        methods:{
            back(){
                this.$router.go(-1)
            }
        },
    }
</script>