<!-- This is the Profile Info component that toggles when the route is set to profile -->
<template>
    <div class="bg-grey-100 shadow-inner h-fit">
        <div class="grid grid-rows-10 grid-cols-12  w-full gap-4 pt-5 pb-4 px-4">
            <div class="row-span-3 col-span-5 bg-white-100 w-full  h-56 rounded-lg shadow-xl">
                <h2 class="relative w-fit mx-4 pt-4 border-b-4 border-yellow-400 font-bold text-xl">Personal Info</h2>
                <div class="pt-4 pb-2 px-4 text-lg">
                    <div class="flex flex-row pb-3">
                        <div class="w-fit font-semibold pr-1">First:</div>
                        <div class="text-lg">{{ User.First }}</div>
                    </div>
                    <div class="flex flex-row pb-3">
                        <div class="w-fit font-semibold pr-1">Last:</div>
                        <div class="text-lg">{{ User.Last }}</div>
                    </div>
                    <div class="flex flex-row pb-3">
                        <div class="w-fit font-semibold pr-1">UCID:</div>
                        <div class="text-lg">{{ User.UCID }}</div>
                    </div>
                    <div class="flex flex-row pb-3">
                        <div class="w-fit font-semibold pr-1">DOB:</div>
                        <div class="text-lg">{{ User.DOB }}</div>
                    </div>
                </div>
            </div>
            <div class="row-span-3 col-start-6 col-span-3 bg-white-100 w-full h-56 rounded-lg shadow-xl">
                <h2 class="relative w-fit mx-4 pt-4 border-b-4 border-yellow-400 font-bold text-xl">Citizenship</h2>
                <div class="grid grid-cols-1 divide-y divide-grey-200 px-4 pt-4 text-lg">
                    <div class="pb-4">
                        <div class="flex flex-row">
                            <div class="w-fit font-semibold pr-1">Country:</div>
                            <div class="">{{ User.Citizenship.Country }}</div>
                        </div>
                        <div class="flex flex-row">
                            <div class="w-fit font-semibold pr-1">Status:</div>
                            <div class="">{{ User.Citizenship.Status }}</div>
                        </div>
                    </div>
                    <div v-if="User.Citizenship.Residency" class="pt-4">
                        <div  class="flex flex-row">
                            <div class="w-fit font-semibold pr-1">Residency:</div>
                            <div class="">{{ User.Citizenship.Residency }}</div>
                        </div>
                        <div class="flex flex-row">
                            <div class="w-fit font-semibold pr-1">Expires:</div>
                            <div class="">{{ User.Citizenship.Expiry }}</div>
                        </div>
                    </div>
                    <div v-else class="pt-4"></div>
                </div>
            </div>
            <div class="relative row-span-7 col-start-9  col-span-4 bg-white-100 h-full w-full rounded-lg shadow-xl">
                <div class="flex flex-row w-full">
                    <h2 class="w-fit mx-4 pt-4 border-b-4 border-yellow-400 font-bold text-xl">Address</h2>
                    <div class="w-full">
                        <div v-if="editingID == Address" class="absolute pt-4 mx-4 w-fit right-0">
                            <svg xmlns="http://www.w3.org/2000/svg" @click="setView()"  class="h-10 w-10 fill-grey-200 hover:fill-red-100" viewBox="0 -960 960 960">
                                <path d="M382-240 154-468l57-57 171 171 367-367 57 57-424 424Z"/>
                            </svg>
                        </div>
                        <div v-else class="absolute pt-4 mx-4 w-fit right-0">
                            <svg xmlns="http://www.w3.org/2000/svg" @click="setEditing(Address)" class="h-8 w-8 fill-grey-200 hover:fill-red-100" viewBox="0 -960 960 960">
                                <path d="M120-120v-170l528-527q12-11 26.5-17t30.5-6q16 0 31 6t26 18l55 56q12 11 17.5 26t5.5 30q0 16-5.5 30.5T817-647L290-120H120Zm584-528 56-56-56-56-56 56 56 56Z"/>
                            </svg>
                        </div>
                    </div>
                </div>
                <div v-if="this.editingID == Address" class="px-4 pt-4 text-left text-lg">
                    <div class="font-semibold pb-2">Street Address: *</div>
                    <div class="pb-2">
                        <input type="text" placeholder="Required" v-model="Address.Street" class="w-10/12 border-2 rounded-md text-md border-grey-100 outline-red-100 pl-2">
                    </div>
                    <div class="font-semibold pb-2">City: *</div>
                    <div class="pb-2">
                        <input type="text" placeholder="Required" v-model="Address.City" class="w-10/12 border-2 text-md rounded-md border-grey-100 outline-red-100 pl-2">
                    </div>
                    <div class="font-semibold pb-2">Province: *</div>
                    <div class="pb-2">
                        <input type="text" placeholder="Required" v-model="Address.Province" class="w-10/12 border-2 text-md rounded-md border-grey-100 outline-red-100 pl-2">
                    </div>
                    <div class="font-semibold pb-2">Country: *</div>
                    <div class="pb-2">
                        <input type="text" placeholder="Required" v-model="Address.Country" class="w-10/12 border-2 text-md rounded-md border-grey-100 outline-red-100 pl-2">
                    </div>
                    <div class="font-semibold pb-2">Postal Code: *</div>
                    <div class="pb-2">
                        <input type="text" placeholder="Required" v-model="Address.Postal" class="w-10/12 border-2 text-md rounded-md border-grey-100 outline-red-100 pl-2">
                    </div>
                    <div class="font-semibold pb-2">Apt/Suite:</div>
                    <div class="pb-2">
                        <input type="text" placeholder="Optional" v-model="Address.Apt" class="w-10/12 border-2 text-md rounded-md border-grey-100 outline-red-100 pl-2">
                    </div>
                </div>
                <div v-else class="px-4 pt-4 text-left text-lg">
                    <div class="font-semibold pb-2">Street Address:</div>
                    <div class="pb-4">{{ Address.Street }}</div>
                    <div class="font-semibold pb-2">City:</div>
                    <div class="pb-4">{{ Address.City }}</div>
                    <div class="font-semibold pb-2">Province:</div>
                    <div class="pb-4">{{ Address.Province }}</div>
                    <div class="font-semibold pb-2">Country:</div>
                    <div class="pb-4">{{ Address.Country }}</div>
                    <div class="font-semibold pb-2">Postal Code:</div>
                    <div class="pb-4">{{ Address.Postal }}</div>
                    <div v-if="Address.Apt" class="font-semibold pb-2">Apt/Suite:</div>
                    <div class="pb-4">{{ Address.Apt }}</div>
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
                        <div class="pr-4">{{ Phone.Home.Number }}</div>
                        <span v-if="Phone.Home.Preferred" class="flex items-center italic text-grey-200 text-xs">Preferred</span> 
                    </div>
                    <div class="font-semibold pb-2">Mobile:</div>
                    <div class="flex flex-row pb-4">
                        <div class="pr-4">{{ Phone.Mobile.Number }}</div>
                        <span v-if="Phone.Mobile.Preferred" class="flex items-center italic text-grey-200 text-xs">Preferred</span> 
                    </div>
                    <div v-if="Phone.Other.Number">
                        <div class="font-semibold pb-2">Other:</div>
                        <div class="flex flex-row pb-4">
                            <div class="pr-4">{{ Phone.Other.Number }}</div>
                            <span v-if="Phone.Other.Preferred" class="flex items-center italic text-grey-200 text-xs">Preferred</span> 
                        </div>
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
                        <div class="pr-4">{{ Email.School.Value }}</div>
                        <span v-if="Email.School.Preferred" class="flex items-center italic text-grey-200 text-xs">Preferred</span> 
                    </div>
                    <div class="font-semibold pb-2">Personal:</div>
                    <div class="flex flex-row pb-4">
                        <div class="pr-4">{{ Email.Personal.Value }}</div>
                        <span v-if="Email.Personal.Preferred" class="flex items-center italic text-grey-200 text-xs">Preferred</span> 
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
                    <div v-if="EmergencyContacts.Contact1.Name" class="relative bg-white-100 w-full h-2/3 border border-grey-100 drop-shadow-lg rounded-lg">
                        <div class="flex flex-row">
                            <div class="w-full">
                                <div class="font-semibold text-left pt-4 pl-4">Name:</div>
                                <div class="text-left pl-4">{{ EmergencyContacts.Contact1.Name }}</div>
                            </div>
                            <div class="w-full">
                                <div class="absolute right-0 flex flex-row pr-4">
                                    <div v-if="EmergencyContacts.Contact1.Primary" class="italic text-green-100 text-xs pt-5">Primary</div>
                                    <div v-if="EmergencyContacts.Contact1.Primary" class="pl-2 pt-4">
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
                                <div class="text-left">{{ EmergencyContacts.Contact1.Relationship }}</div>
                            </div>
                            <div class="w-full pr-4">
                                <div class="text-left font-semibold">Phone:</div>
                                <div class="text-left">{{ EmergencyContacts.Contact1.Phone }}</div>
                            </div>
                        </div>
                    </div>
                    <div v-if="EmergencyContacts.Contact2.Name" class="relative bg-white-100 w-full h-2/3 border border-grey-100 drop-shadow-lg rounded-lg">
                        <div class="flex flex-row">
                            <div class="w-full">
                                <div class="font-semibold text-left pt-4 pl-4">Name:</div>
                                <div class="text-left pl-4">{{ EmergencyContacts.Contact2.Name }}</div>
                            </div>
                            <div class="w-full">
                                <div class="absolute right-0 flex flex-row pr-4">
                                    <div v-if="EmergencyContacts.Contact2.Primary" class="italic text-green-100 text-xs pt-5">Primary</div>
                                    <div v-if="EmergencyContacts.Contact2.Primary" class="pl-2 pt-4">
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
                                <div class="text-left">{{ EmergencyContacts.Contact2.Relationship }}</div>
                            </div>
                            <div class="w-full pr-4">
                                <div class="text-left font-semibold">Phone:</div>
                                <div class="text-left">{{ EmergencyContacts.Contact2.Phone }}</div>
                            </div>
                        </div>
                    </div>
                    <div v-if="EmergencyContacts.Contact3.Name" class="relative bg-white-100 w-full h-2/3 border border-grey-100 drop-shadow-lg rounded-lg">
                        <div class="flex flex-row">
                            <div class="w-full">
                                <div class="font-semibold text-left pt-4 pl-4">Name:</div>
                                <div class="text-left pl-4">{{ EmergencyContacts.Contact3.Name }}</div>
                            </div>
                            <div class="w-full">
                                <div class="absolute right-0 flex flex-row pr-4">
                                    <div v-if="EmergencyContacts.Contact3.Primary" class="italic text-green-100 text-xs pt-5">Primary</div>
                                    <div v-if="EmergencyContacts.Contact3.Primary" class="pl-2 pt-4">
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
                                <div class="text-left">{{ EmergencyContacts.Contact3.Relationship }}</div>
                            </div>
                            <div class="w-full pr-4">
                                <div class="text-left font-semibold">Phone:</div>
                                <div class="text-left">{{ EmergencyContacts.Contact3.Phone }}</div>
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
        data: ()=> {
            return {
                editingID: null,
                User: {
                    First: "John",
                    Last: "Doe",
                    UCID: "31234567",
                    DOB: "2000-01-01",
                    Citizenship: {
                        Country: "Canada",
                        Status: "Permanent Resident",
                        Residency: null,
                        Expiry: null
                    }
                },
                Address: {
                    Street: "2500 University Dr NW",
                    City: "Calgary",
                    Province: "Alberta",
                    Country: "Canada",
                    Postal: "T2N 1N4",
                    Apt: null
                },
                Email: {
                    School: {
                        Value: "noreply@ucalgary.ca",
                        Preferred: true
                    },
                    Personal: {
                        Value: "noreply@gmail.com",
                        Preferred: false
                    }
                },
                Phone: {
                    Home: {
                        Number: "(403)-220-5110",
                        Preferred: false
                    },
                    Mobile: {
                        Number: "(403)-220-5738",
                        Preferred: true
                    },
                    Other: {
                        Number: null,
                        Preferred: false
                    }
                },
                EmergencyContacts: {
                    Contact1: {
                        Name: "Jane Doe",
                        Relationship: "Mother",
                        Phone: "(403)-220-8600",
                        Primary: true
                    },
                    Contact2: {
                        Name: "Josh Doe",
                        Relationship: "Father",
                        Phone: "(403)-220-8601",
                        Primary: false
                    },
                    Contact3: {
                        Name: null,
                        Relationship: null,
                        Phone: null,
                        Primary: false
                    }
                }
            }
        },
        created(){
            this.$emit('show-navbar')
            this.$emit('toggle-selected', 'profile')
        }, 
        methods:{
            back(){
                this.$router.go(-1)
            },
            setEditing(element) {
                this.editingID = element;
            },
            setView() {
                this.editingID = null;
            }
        },
    }
</script>