<!-- This is the Profile Info component that toggles when the route is set to profile -->
<template>
    <div class="bg-grey-100 shadow-inner h-fit">
        <div class="grid grid-rows-10 grid-cols-12  w-full gap-4 pt-5 pb-4 px-4">
            <div class="row-span-3 col-span-5 bg-white-100 w-full  h-56 rounded-lg shadow-xl">
                <h2 class="relative w-fit mx-4 pt-4 border-b-4 border-yellow-400 font-bold text-xl">Personal Info</h2>
                <div class="pt-4 pb-2 px-4 text-lg">
                    <div class="flex flex-row pb-3">
                        <div class="w-fit font-semibold pr-1">First:</div>
                        <div class="text-lg">John</div>
                    </div>
                    <div class="flex flex-row pb-3">
                        <div class="w-fit font-semibold pr-1">Last:</div>
                        <div class="text-lg">Doe</div>
                    </div>
                    <div class="flex flex-row pb-3">
                        <div class="w-fit font-semibold pr-1">UCID:</div>
                        <div class="text-lg">31234567</div>
                    </div>
                    <div class="flex flex-row pb-3">
                        <div class="w-fit font-semibold pr-1">DOB:</div>
                        <div class="text-lg">01-01-2000</div>
                    </div>
                </div>
            </div>
            <div class="row-span-3 col-start-6 col-span-3 bg-white-100 w-full h-56 rounded-lg shadow-xl">
                <h2 class="relative w-fit mx-4 pt-4 border-b-4 border-yellow-400 font-bold text-xl">Citizenship</h2>
                <div class="grid grid-cols-1 divide-y divide-grey-200 px-4 pt-4 text-lg">
                    <div class="pb-4">
                        <div class="flex flex-row">
                            <div class="w-fit font-semibold pr-1">Country:</div>
                            <div class="">Canada</div>
                        </div>
                        <div class="flex flex-row">
                            <div class="w-fit font-semibold pr-1">Status:</div>
                            <div class="">Permanent Resident</div>
                        </div>
                    </div>
                    <div class="pt-4">
                        <div class="flex flex-row">
                            <div class="w-fit font-semibold pr-1">Residency:</div>
                            <div class="">Student Visa</div>
                        </div>
                        <div class="flex flex-row">
                            <div class="w-fit font-semibold pr-1">Expires:</div>
                            <div class="">2024-06-01</div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="relative row-span-7 col-start-9  col-span-4 bg-white-100 h-full w-full rounded-lg shadow-xl">
                <div class="flex flex-row w-full">
                    <h2 class="w-fit mx-4 pt-4 border-b-4 border-yellow-400 font-bold text-xl">Address</h2>
                    <div class="w-full">
                        <div class="absolute pt-4 mx-4 w-fit right-0">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 fill-grey-200 hover:fill-red-100" viewBox="0 -960 960 960">
                                <path d="M120-120v-170l528-527q12-11 26.5-17t30.5-6q16 0 31 6t26 18l55 56q12 11 17.5 26t5.5 30q0 16-5.5 30.5T817-647L290-120H120Zm584-528 56-56-56-56-56 56 56 56Z"/>
                            </svg>
                        </div>
                    </div>
                </div>
                <div class="px-4 pt-4 text-left text-lg">
                    <div class="font-semibold pb-2">Street Address:</div>
                    <div class="pb-4">2500 University Dr NW</div>
                    <div class="font-semibold pb-2">City:</div>
                    <div class="pb-4">Calgary</div>
                    <div class="font-semibold pb-2">Province:</div>
                    <div class="pb-4">Alberta</div>
                    <div class="font-semibold pb-2">Country:</div>
                    <div class="pb-4">Canada</div>
                    <div class="font-semibold pb-2">Postal Code:</div>
                    <div class="pb-4">T2N 1N4</div>
                    <div class="font-semibold pb-2">Apt/Suite:</div>
                    <div class="pb-4">ENC 101</div>
                </div>
            </div>
            <div class="relative row-start-4 row-span-4 col-span-4 bg-white-100 w-full h-full rounded-lg shadow-xl">
                <div class="flex flex-row w-full">
                    <h2 class="w-fit mx-4 pt-4 border-b-4 border-yellow-400 font-bold text-xl">Phone</h2>
                    <div class="w-full">
                        <div class="absolute pt-4 mx-4 w-fit right-0">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 fill-grey-200 hover:fill-red-100" viewBox="0 -960 960 960">
                                <path d="M120-120v-170l528-527q12-11 26.5-17t30.5-6q16 0 31 6t26 18l55 56q12 11 17.5 26t5.5 30q0 16-5.5 30.5T817-647L290-120H120Zm584-528 56-56-56-56-56 56 56 56Z"/>
                            </svg>
                        </div>
                    </div>
                </div>
                <div class="px-4 pt-4 text-left text-lg">
                    <div class="font-semibold pb-2">Home:</div>
                    <div class="flex flex-row pb-4">
                        <div class="pr-4">(403)-220-5110</div>
                        <span class="flex items-center italic text-grey-200 text-xs">Preferred</span> 
                    </div>
                    <div class="font-semibold pb-2">Mobile:</div>
                    <div class="flex flex-row pb-4">
                        <div class="pr-4">(403)-220-5738</div>
                        <span class="flex items-center italic text-grey-200 text-xs">Preferred</span> 
                    </div>
                    <div class="font-semibold pb-2">Other:</div>
                    <div class="flex flex-row pb-4">
                        <div class="pr-4">(403)-220-8600</div>
                        <span class="flex items-center italic text-grey-200 text-xs">Preferred</span> 
                    </div>
                </div>
            </div>
            <div class="relative row-start-4 row-span-4 col-start-5 col-span-4 bg-white-100 h-full  w-full rounded-lg shadow-xl">
                <div class="flex flex-row w-full">
                    <h2 class="w-fit mx-4 pt-4 border-b-4 border-yellow-400 font-bold text-xl">Email</h2>
                    <div class="w-full">
                        <div class="absolute pt-4 mx-4 w-fit right-0">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 fill-grey-200 hover:fill-red-100" viewBox="0 -960 960 960">
                                <path d="M120-120v-170l528-527q12-11 26.5-17t30.5-6q16 0 31 6t26 18l55 56q12 11 17.5 26t5.5 30q0 16-5.5 30.5T817-647L290-120H120Zm584-528 56-56-56-56-56 56 56 56Z"/>
                            </svg>
                        </div>
                    </div>
                </div>
                <div class="px-4 pt-4 text-left text-lg">
                    <div class="font-semibold pb-2">School:</div>
                    <div class="flex flex-row pb-4">
                        <div class="pr-4">no-reply@ucalgary.ca</div>
                        <span class="flex items-center italic text-grey-200 text-xs">Preferred</span> 
                    </div>
                    <div class="font-semibold pb-2">Personal:</div>
                    <div class="flex flex-row pb-4">
                        <div class="pr-4">no-reply@gmail.com</div>
                        <span class="flex items-center italic text-grey-200 text-xs">Preferred</span> 
                    </div>
                </div>
            </div>
            <div class="relative row-start-8 row-span-3  col-span-12 bg-white-100 h-56 rounded-lg shadow-xl">
                <div class="flex flex-row w-full">
                    <h2 class="w-60 mx-4 pt-4 border-b-4 border-yellow-400 font-bold text-xl">Emergency Contacts</h2>
                    <div class="w-full">
                        <div class="absolute pt-4 mx-4 w-fit right-0">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 fill-grey-200 hover:fill-red-100" viewBox="0 -960 960 960">
                                <path d="M440-440H200v-80h240v-240h80v240h240v80H520v240h-80v-240Z"/>
                            </svg>
                        </div>
                    </div>
                </div>
                <div class="grid grid-cols-3 w-full h-full pt-4 px-4 gap-6">
                    <div class="relative bg-white-100 w-full h-2/3 border border-grey-100 drop-shadow-lg rounded-lg">
                        <div class="flex flex-row">
                            <div class="w-full">
                                <div class="font-semibold text-left pt-4 pl-4">Name:</div>
                                <div class="text-left pl-4">John Doe</div>
                            </div>
                            <div class="w-full">
                                <div class="absolute right-0 flex flex-row pr-4">
                                    <div class="italic text-green-100 text-xs pt-5">Primary</div>
                                    <div class="pl-2 pt-4">
                                        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 fill-green-100" viewBox="0 -960 960 960">
                                            <path d="m344-60-76-128-144-32 14-148-98-112 98-112-14-148 144-32 76-128 136 58 136-58 76 128 144 32-14 148 98 112-98 112 14 148-144 32-76 128-136-58-136 58Zm94-278 226-226-56-58-170 170-86-84-56 56 142 142Z"/>
                                        </svg>
                                    </div>
                                    <div class="pl-4 pt-2">
                                        <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 fill-grey-200 hover:fill-red-100" viewBox="0 -960 960 960">
                                            <path d="M240-400q-33 0-56.5-23.5T160-480q0-33 23.5-56.5T240-560q33 0 56.5 23.5T320-480q0 33-23.5 56.5T240-400Zm240 0q-33 0-56.5-23.5T400-480q0-33 23.5-56.5T480-560q33 0 56.5 23.5T560-480q0 33-23.5 56.5T480-400Zm240 0q-33 0-56.5-23.5T640-480q0-33 23.5-56.5T720-560q33 0 56.5 23.5T800-480q0 33-23.5 56.5T720-400Z"/>
                                        </svg>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="flex flex-row pt-4">
                            <div class="w-full pl-4">
                                <div class="text-left font-semibold">Relationship:</div>
                                <div class="text-left">Father</div>
                            </div>
                            <div class="w-full pr-4">
                                <div class="text-left font-semibold">Phone:</div>
                                <div class="text-left">(403)-220-5110</div>
                            </div>
                        </div>
                    </div>
                    <div class="relative bg-white-100 w-full h-2/3 border border-grey-100 drop-shadow-lg rounded-lg">
                        <div class="flex flex-row">
                            <div class="w-full">
                                <div class="font-semibold text-left pt-4 pl-4">Name:</div>
                                <div class="text-left pl-4">John Doe</div>
                            </div>
                            <div class="w-full">
                                <div class="absolute right-0 flex flex-row pr-4">
                                    <div class="italic text-green-100 text-xs pt-5">Primary</div>
                                    <div class="pl-2 pt-4">
                                        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 fill-green-100" viewBox="0 -960 960 960">
                                            <path d="m344-60-76-128-144-32 14-148-98-112 98-112-14-148 144-32 76-128 136 58 136-58 76 128 144 32-14 148 98 112-98 112 14 148-144 32-76 128-136-58-136 58Zm94-278 226-226-56-58-170 170-86-84-56 56 142 142Z"/>
                                        </svg>
                                    </div>
                                    <div class="pl-4 pt-2">
                                        <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 fill-grey-200 hover:fill-red-100" viewBox="0 -960 960 960">
                                            <path d="M240-400q-33 0-56.5-23.5T160-480q0-33 23.5-56.5T240-560q33 0 56.5 23.5T320-480q0 33-23.5 56.5T240-400Zm240 0q-33 0-56.5-23.5T400-480q0-33 23.5-56.5T480-560q33 0 56.5 23.5T560-480q0 33-23.5 56.5T480-400Zm240 0q-33 0-56.5-23.5T640-480q0-33 23.5-56.5T720-560q33 0 56.5 23.5T800-480q0 33-23.5 56.5T720-400Z"/>
                                        </svg>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="flex flex-row pt-4">
                            <div class="w-full pl-4">
                                <div class="text-left font-semibold">Relationship:</div>
                                <div class="text-left">Father</div>
                            </div>
                            <div class="w-full pr-4">
                                <div class="text-left font-semibold">Phone:</div>
                                <div class="text-left">(403)-220-5110</div>
                            </div>
                        </div>
                    </div>
                    <div class="relative bg-white-100 w-full h-2/3 border border-grey-100 drop-shadow-lg rounded-lg">
                        <div class="flex flex-row">
                            <div class="w-full">
                                <div class="font-semibold text-left pt-4 pl-4">Name:</div>
                                <div class="text-left pl-4">John Doe</div>
                            </div>
                            <div class="w-full">
                                <div class="absolute right-0 flex flex-row pr-4">
                                    <div class="italic text-green-100 text-xs pt-5">Primary</div>
                                    <div class="pl-2 pt-4">
                                        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 fill-green-100" viewBox="0 -960 960 960">
                                            <path d="m344-60-76-128-144-32 14-148-98-112 98-112-14-148 144-32 76-128 136 58 136-58 76 128 144 32-14 148 98 112-98 112 14 148-144 32-76 128-136-58-136 58Zm94-278 226-226-56-58-170 170-86-84-56 56 142 142Z"/>
                                        </svg>
                                    </div>
                                    <div class="pl-4 pt-2">
                                        <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 fill-grey-200 hover:fill-red-100" viewBox="0 -960 960 960">
                                            <path d="M240-400q-33 0-56.5-23.5T160-480q0-33 23.5-56.5T240-560q33 0 56.5 23.5T320-480q0 33-23.5 56.5T240-400Zm240 0q-33 0-56.5-23.5T400-480q0-33 23.5-56.5T480-560q33 0 56.5 23.5T560-480q0 33-23.5 56.5T480-400Zm240 0q-33 0-56.5-23.5T640-480q0-33 23.5-56.5T720-560q33 0 56.5 23.5T800-480q0 33-23.5 56.5T720-400Z"/>
                                        </svg>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="flex flex-row pt-4">
                            <div class="w-full pl-4">
                                <div class="text-left font-semibold">Relationship:</div>
                                <div class="text-left">Father</div>
                            </div>
                            <div class="w-full pr-4">
                                <div class="text-left font-semibold">Phone:</div>
                                <div class="text-left">(403)-220-5110</div>
                            </div>
                        </div>
                    </div>
                </div>
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
            this.$emit('toggle-selected', 'profile')
        }, 
        methods:{
            back(){
                this.$router.go(-1)
            }
        },
    }
</script>