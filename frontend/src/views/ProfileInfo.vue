<!-- This is the Profile Info component that toggles when the route is set to profile -->
<template>
    <div class="bg-gray-400">
        <div class="grid grid-rows-10 grid-cols-12  w-full gap-2 pt-2 pb-2 px-2 shadow-inner">
            <div class="row-span-3 col-span-5 bg-white-100 w-full  h-full rounded-lg shadow-xl">
                <h2 class="relative w-fit mx-4 pt-2 border-b-4 border-yellow-400 font-bold">Personal Info</h2>
                <div class="grid grid-rows-4 grid-cols-4 gap-1 pt-2">
                    <p class="font-semibold text-right">First:</p>
                    <p class="col-span-3 text-left">John</p>
                    <p class="font-semibold text-right">Last:</p>
                    <p class="col-span-3 text-left">Doe</p>
                    <p class="font-semibold text-right">UCID:</p>
                    <p class="col-span-3 text-left">31234567</p>
                    <p class="font-semibold text-right">DOB:</p>
                    <p class="col-span-3 text-left">01-01-2000</p>
                </div>
            </div>
            <div class="row-span-3 col-start-6 col-span-3 bg-white-100 w-full h-full rounded-lg shadow-xl">
                <h2 class="relative w-fit mx-4 pt-2 border-b-4 border-yellow-400 font-bold">Citizenship</h2>
                <div class="grid grid-cols-1 divide-y divide-black-100 px-2 pt-2">
                    <div class="pb-2">
                        <div class="flex flex-row text-sm">
                            <div class="w-fit font-semibold pr-1">Country:</div>
                            <div class="">Canada</div>
                        </div>
                        <div class="flex flex-row text-sm">
                            <div class="w-fit font-semibold pr-1">Status:</div>
                            <div class="">Permanent Resident</div>
                        </div>
                    </div>
                    <div class="pt-2">
                        <div class="flex flex-row text-sm">
                            <div class="w-fit font-semibold pr-1">Residency:</div>
                            <div class="">Student Visa</div>
                        </div>
                        <div class="flex flex-row text-sm">
                            <div class="w-fit font-semibold pr-1">Expires:</div>
                            <div class="">2024-06-01</div>
                        </div>
                    </div>
                </div>
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