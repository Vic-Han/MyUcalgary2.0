<!-- This is the Profile Info component that toggles when the route is set to profile -->
<template>
    <div class="bg-gray-400">
        <div class="grid grid-rows-10 grid-cols-12  w-full gap-2 pt-2 pb-2 px-2 shadow-inner">
            <div class="row-span-3 col-span-5 bg-white-100 w-full  h-full rounded-lg shadow-xl">
                <h2 class="relative w-fit mx-4 pt-2 border-b-4 border-yellow-400 font-bold">Personal Info</h2>
                <div class="flex flex-row flex-wrap  w-full">
                    <p class="w-fit font-semibold">First:</p>
                    <p class="w-2/3">John</p>
                    <p class="w-fit font-semibold">Last:</p>
                    <p class="w-2/3">Doe</p>
                    <p class="w-fit font-semibold">UCID:</p>
                    <p class="w-2/3">31234567</p>
                    <p class="w-fit font-semibold">DOB:</p>
                    <p class="w-2/3">2000-01-01</p>
                </div>
            </div>
            <div class="row-span-3 col-start-6 col-span-3 bg-white-100 w-full h-full rounded-lg shadow-xl">
                <h2 class="relative w-fit mx-4 pt-2 border-b-4 border-yellow-400 font-bold">Citizenship</h2>
            </div>
            <div class="row-span-7 col-start-9  col-span-4 bg-white-100 h-full w-full rounded-lg shadow-xl">
                <h2 class="relative w-fit mx-4 pt-2 border-b-4 border-yellow-400 font-bold">Address</h2>
            </div>
            <div class="row-start-4 row-span-4 col-span-4 bg-white-100 w-full h-full rounded-lg shadow-xl">
                <h2 class="relative w-fit mx-4 pt-2 border-b-4 border-yellow-400 font-bold">Phone</h2>
            </div>
            <div class="row-start-4 row-span-4 col-start-5 col-span-4 bg-white-100 h-full  w-full rounded-lg shadow-xl">
                <h2 class="relative w-fit mx-4 pt-2 border-b-4 border-yellow-400 font-bold">Email</h2>
            </div>
            <div class="row-start-8 row-span-3  col-span-12 bg-white-100 h-40 rounded-lg shadow-xl">
                <h2 class="relative w-fit mx-4 pt-2 border-b-4 border-yellow-400 font-bold">Emergency Contacts</h2>
            </div>
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