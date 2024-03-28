<!-- This is the Profile Info component that toggles when the route is set to profile -->
<template>
    <div class="bg-grey-100 shadow-inner h-fit">
        <div class="grid grid-rows-10 grid-cols-12  w-full gap-4 pt-2 pb-2 px-2">
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
                <div class="grid grid-cols-1 px-4 pt-4 text-lg">
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
                        <div v-if="editingID == 'Address'" class="absolute pt-4 mx-4 w-fit right-0">
                            <svg xmlns="http://www.w3.org/2000/svg" @click="setView()"  class="h-10 w-10 fill-grey-200 hover:fill-red-100" viewBox="0 -960 960 960">
                                <path d="M382-240 154-468l57-57 171 171 367-367 57 57-424 424Z"/>
                            </svg>
                        </div>
                        <div v-else-if="editingID != null" class="absolute pt-4 mx-4 w-fit right-0">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 fill-grey-200" viewBox="0 -960 960 960">
                                <path d="M120-120v-170l528-527q12-11 26.5-17t30.5-6q16 0 31 6t26 18l55 56q12 11 17.5 26t5.5 30q0 16-5.5 30.5T817-647L290-120H120Zm584-528 56-56-56-56-56 56 56 56Z"/>
                            </svg>
                        </div>
                        <div v-else class="absolute pt-4 mx-4 w-fit right-0">
                            <svg xmlns="http://www.w3.org/2000/svg" @click="setEditing('Address')" class="h-8 w-8 fill-grey-200 hover:fill-red-100" viewBox="0 -960 960 960">
                                <path d="M120-120v-170l528-527q12-11 26.5-17t30.5-6q16 0 31 6t26 18l55 56q12 11 17.5 26t5.5 30q0 16-5.5 30.5T817-647L290-120H120Zm584-528 56-56-56-56-56 56 56 56Z"/>
                            </svg>
                        </div>
                    </div>
                </div>
                <div v-if="this.editingID == 'Address'" class="px-4 pt-4 text-left text-lg">
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
                        <div v-if="editingID == 'Phone'" class="absolute pt-4 mx-4 w-fit right-0">
                            <svg xmlns="http://www.w3.org/2000/svg" @click="setView()"  class="h-10 w-10 fill-grey-200 hover:fill-red-100" viewBox="0 -960 960 960">
                                <path d="M382-240 154-468l57-57 171 171 367-367 57 57-424 424Z"/>
                            </svg>
                        </div>
                        <div v-else-if="editingID != null" class="absolute pt-4 mx-4 w-fit right-0">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 fill-grey-200" viewBox="0 -960 960 960">
                                <path d="M120-120v-170l528-527q12-11 26.5-17t30.5-6q16 0 31 6t26 18l55 56q12 11 17.5 26t5.5 30q0 16-5.5 30.5T817-647L290-120H120Zm584-528 56-56-56-56-56 56 56 56Z"/>
                            </svg>
                        </div>
                        <div v-else class="absolute pt-4 mx-4 w-fit right-0">
                            <svg xmlns="http://www.w3.org/2000/svg" @click="setEditing('Phone')" class="h-8 w-8 fill-grey-200 hover:fill-red-100" viewBox="0 -960 960 960">
                                <path d="M120-120v-170l528-527q12-11 26.5-17t30.5-6q16 0 31 6t26 18l55 56q12 11 17.5 26t5.5 30q0 16-5.5 30.5T817-647L290-120H120Zm584-528 56-56-56-56-56 56 56 56Z"/>
                            </svg>
                        </div>
                    </div>
                </div>
                <div v-if="this.editingID == 'Phone'" class="px-4 pt-4 text-left text-lg">
                    <div class="flex flex-row">
                        <div class="font-semibold pb-2 w-5/12 mr-6">Home: *</div>
                        <span  class="flex items-center italic text-grey-200 text-xs">Preferred</span>
                    </div>
                    <div class="flex flex-row pb-2">
                        <div class="">
                            <input type="text" placeholder="Required" v-model="Phone.Home" class="w-10/12 border-2 rounded-md text-md border-grey-100 outline-red-100 pl-2">
                        </div>
                        <div class="flex items-center">
                            <input type="radio" name="Phone" value="Home" v-model="Phone.Preferred" class="w-4 h-4 accent-red-100">
                        </div>
                    </div>
                    <div class="font-semibold pb-2">Mobile: *</div>
                    <div class="flex flex-row pb-2">
                        <div class="">
                            <input type="text" placeholder="Required" v-model="Phone.Mobile" class="w-10/12 border-2 rounded-md text-md border-grey-100 outline-red-100 pl-2">
                        </div>
                        <div class="flex items-center">
                            <input type="radio" name="Phone" value="Mobile" v-model="Phone.Preferred" class="w-4 h-4 accent-red-100">
                        </div>
                    </div>
                    <div>
                        <div class="font-semibold pb-2">Other:</div>
                        <div class="flex flex-row pb-2">
                            <div class="">
                                <input type="text" placeholder="Optional" v-model="Phone.Other" class="w-10/12 border-2 rounded-md text-md border-grey-100 outline-red-100 pl-2">
                            </div>
                            <div v-if="Phone.Other" class="flex items-center">
                                <input type="radio" name="Phone" value="Other" v-model="Phone.Preferred" class="w-4 h-4 accent-red-100">
                            </div>
                        </div>
                    </div>
                </div>
                <div v-else class="px-4 pt-4 text-left text-lg">
                    <div class="font-semibold pb-2">Home:</div>
                    <div class="flex flex-row pb-4">
                        <div class="pr-4">{{ Phone.Home }}</div>
                        <span v-if="Phone.Preferred == 'Home'" class="flex items-center italic text-grey-200 text-xs">Preferred</span> 
                    </div>
                    <div class="font-semibold pb-2">Mobile:</div>
                    <div class="flex flex-row pb-4">
                        <div class="pr-4">{{ Phone.Mobile }}</div>
                        <span v-if="Phone.Preferred == 'Mobile'" class="flex items-center italic text-grey-200 text-xs">Preferred</span> 
                    </div>
                    <div v-if="Phone.Other">
                        <div class="font-semibold pb-2">Other:</div>
                        <div class="flex flex-row pb-4">
                            <div class="pr-4">{{ Phone.Other }}</div>
                            <span v-if="Phone.Preferred == 'Other'" class="flex items-center italic text-grey-200 text-xs">Preferred</span> 
                        </div>
                    </div>
                </div>
            </div>
            <div class="relative row-start-4 row-span-4 col-start-5 col-span-4 bg-white-100 h-full  w-full rounded-lg shadow-xl">
                <div class="flex flex-row w-full">
                    <h2 class="w-fit mx-4 pt-4 border-b-4 border-yellow-400 font-bold text-xl">Email</h2>
                    <div class="w-full">
                        <div v-if="editingID == 'Email'" class="absolute pt-4 mx-4 w-fit right-0">
                            <svg xmlns="http://www.w3.org/2000/svg" @click="setView()"  class="h-10 w-10 fill-grey-200 hover:fill-red-100" viewBox="0 -960 960 960">
                                <path d="M382-240 154-468l57-57 171 171 367-367 57 57-424 424Z"/>
                            </svg>
                        </div>
                        <div v-else-if="editingID != null" class="absolute pt-4 mx-4 w-fit right-0">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 fill-grey-200" viewBox="0 -960 960 960">
                                <path d="M120-120v-170l528-527q12-11 26.5-17t30.5-6q16 0 31 6t26 18l55 56q12 11 17.5 26t5.5 30q0 16-5.5 30.5T817-647L290-120H120Zm584-528 56-56-56-56-56 56 56 56Z"/>
                            </svg>
                        </div>
                        <div v-else class="absolute pt-4 mx-4 w-fit right-0">
                            <svg xmlns="http://www.w3.org/2000/svg" @click="setEditing('Email')" class="h-8 w-8 fill-grey-200 hover:fill-red-100" viewBox="0 -960 960 960">
                                <path d="M120-120v-170l528-527q12-11 26.5-17t30.5-6q16 0 31 6t26 18l55 56q12 11 17.5 26t5.5 30q0 16-5.5 30.5T817-647L290-120H120Zm584-528 56-56-56-56-56 56 56 56Z"/>
                            </svg>
                        </div>
                    </div>
                </div>
                <div v-if="this.editingID == 'Email'" class="px-4 pt-4 text-left text-lg">
                    <div class="flex flex-row">
                        <div class="font-semibold pb-2 w-3/4 mr-5">School: *</div>
                        <span  class="flex items-center italic text-grey-200 text-xs">Preferred</span>
                    </div>
                    <div class="flex flex-row pb-4">
                        <div class="pr-4 w-10/12">{{ Email.School }}</div>
                        <div class="flex items-center">
                            <input type="radio" name="Email" value="School" v-model="Email.Preferred" class="w-4 h-4 accent-red-100">
                        </div>
                    </div>
                    <div class="font-semibold pb-2">Personal: *</div>
                    <div class="flex flex-row pb-4">
                        <div class="w-10/12">
                            <input type="text" placeholder="Required" v-model="Email.Personal" class="w-10/12 border-2 rounded-md text-md border-grey-100 outline-red-100 pl-2">
                        </div>
                        <div class="flex items-center">
                            <input type="radio" name="Email" value="Personal" v-model="Email.Preferred" class="w-4 h-4 accent-red-100">
                        </div>
                    </div>
                </div>
                <div v-else class="px-4 pt-4 text-left text-lg">
                    <div class="font-semibold pb-2">School:</div>
                    <div class="flex flex-row pb-4">
                        <div class="pr-4">{{ Email.School }}</div>
                        <span v-if="Email.Preferred == 'School'" class="flex items-center italic text-grey-200 text-xs">Preferred</span> 
                    </div>
                    <div class="font-semibold pb-2">Personal:</div>
                    <div class="flex flex-row pb-4">
                        <div class="pr-4">{{ Email.Personal }}</div>
                        <span v-if="Email.Preferred == 'Personal'" class="flex items-center italic text-grey-200 text-xs">Preferred</span> 
                    </div>
                </div>
            </div>
            <div class="relative row-start-8 row-span-3  col-span-12 bg-white-100 h-56 rounded-lg shadow-xl">
                <div class="flex flex-row w-full">
                    <h2 class="w-60 mx-4 pt-4 border-b-4 border-yellow-400 font-bold text-xl">Emergency Contacts</h2>
                    <div class="w-full">
                        <div v-if="EmergencyContacts.length < 3" @click="addContact()" class="absolute pt-4 mx-4 w-fit right-0">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 fill-grey-200 hover:fill-red-100" viewBox="0 -960 960 960">
                                <path d="M440-440H200v-80h240v-240h80v240h240v80H520v240h-80v-240Z"/>
                            </svg>
                        </div>
                    </div>
                </div>
                <div class="grid grid-cols-3 w-full h-full pt-4 px-4 gap-6">
                    <div v-for="(Contact,index) in EmergencyContacts" :key="index">
                        <div v-if="this.editingID == index" class="relative bg-white-100 w-full h-2/3 border border-grey-100 drop-shadow-lg rounded-lg">
                            <div class="flex flex-row">
                                <div class="w-full">
                                    <div class="font-semibold text-left pt-4 pl-4">Name: *</div>
                                    <input type="text" placeholder="Required" v-model="Contact.Name" class="relative left-0 w-full border-2 rounded-md text-md mx-4 border-grey-100 outline-red-100 pl-2">
                                </div>
                                <div class="w-full">
                                    <div class="absolute right-0 flex flex-row pr-4">
                                        <div v-if="Contact.Primary" class="italic text-green-100 text-xs pt-5">Primary</div>
                                        <div v-if="Contact.Primary" class="pl-2 pt-4">
                                            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 fill-green-100" viewBox="0 -960 960 960">
                                                <path d="m344-60-76-128-144-32 14-148-98-112 98-112-14-148 144-32 76-128 136 58 136-58 76 128 144 32-14 148 98 112-98 112 14 148-144 32-76 128-136-58-136 58Zm94-278 226-226-56-58-170 170-86-84-56 56 142 142Z"/>
                                            </svg>
                                        </div>
                                        <div class="pl-4 pt-2">
                                            <svg xmlns="http://www.w3.org/2000/svg" @click="setView()" class="h-10 w-10 fill-grey-200 hover:fill-red-100" viewBox="0 -960 960 960">
                                                <path d="M382-240 154-468l57-57 171 171 367-367 57 57-424 424Z"/>
                                            </svg>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="flex flex-row pt-2">
                                <div class="w-full mx-4">
                                    <div class="text-left font-semibold">Relationship: *</div>
                                    <input type="text" placeholder="Required" v-model="Contact.Relationship" class="relative left-0 w-full mr-2 border-2 rounded-md text-md border-grey-100 outline-red-100 pl-2">
                                </div>
                                <div class="w-full mr-4">
                                    <div class="text-left font-semibold">Phone: *</div>
                                    <input type="text" placeholder="Required" v-model="Contact.Phone" class="relative left-0 w-full border-2 rounded-md text-md border-grey-100 outline-red-100 pl-2">
                                </div>
                            </div>
                        </div>
                        <div v-else class="relative bg-white-100 w-full h-2/3 border border-grey-100 drop-shadow-lg rounded-lg">
                            <div id="contact-dropdown" v-if="dropdownVisible == index" class="absolute py-1 right-4 top-8 z-20 bg-white-100 rounded-md border border-grey-100 drop-shadow-lg w-40 h-28 flex flex-col">
                                <div @click="editContact(index)" class="flex flex-row items-center h-full pt-1 pb-1 fill-grey-200 text-grey-200 hover:bg-red-100 hover:fill-white-100 hover:text-white-100">
                                    <div class="w-1/3 ml-4">
                                        <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" viewBox="0 -960 960 960">
                                            <path d="M120-120v-170l528-527q12-11 26.5-17t30.5-6q16 0 31 6t26 18l55 56q12 11 17.5 26t5.5 30q0 16-5.5 30.5T817-647L290-120H120Zm584-528 56-56-56-56-56 56 56 56Z"/>
                                        </svg>
                                    </div>
                                    <div class="w-full text-left">
                                        Edit
                                    </div>
                                </div>
                                <div @click="togglePrimary(index)" class="flex flex-row items-center h-full pt-1 pb-1 fill-grey-200 text-grey-200 hover:bg-red-100 hover:fill-white-100 hover:text-white-100">
                                    <div v-if="Contact.Primary" class="w-1/3 ml-4">
                                        <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" viewBox="0 -960 960 960">
                                            <path d="m305-704 112-145q12-16 28.5-23.5T480-880q18 0 34.5 7.5T543-849l112 145 170 57q26 8 41 29.5t15 47.5q0 12-3.5 24T866-523L756-367l4 164q1 35-23 59t-56 24q-2 0-22-3l-179-50-179 50q-5 2-11 2.5t-11 .5q-32 0-56-24t-23-59l4-165L95-523q-8-11-11.5-23T80-570q0-25 14.5-46.5T135-647l170-57Z"/>
                                        </svg>
                                    </div>
                                    <div v-else class="w-1/3 ml-4">
                                        <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6"  viewBox="0 -960 960 960">
                                            <path d="m305-704 112-145q12-16 28.5-23.5T480-880q18 0 34.5 7.5T543-849l112 145 170 57q26 8 41 29.5t15 47.5q0 12-3.5 24T866-523L756-367l4 164q1 35-23 59t-56 24q-2 0-22-3l-179-50-179 50q-5 2-11 2.5t-11 .5q-32 0-56-24t-23-59l4-165L95-523q-8-11-11.5-23T80-570q0-25 14.5-46.5T135-647l170-57Zm49 69-194 64 124 179-4 191 200-55 200 56-4-192 124-177-194-66-126-165-126 165Zm126 135Z"/>
                                        </svg>
                                    </div>
                                    <div class="w-full text-left">
                                        Primary
                                    </div>
                                </div>
                                <div @click="removeContact(index)" class="flex flex-row items-center h-full pt-1 pb-1 fill-grey-200 text-grey-200 hover:bg-red-100 hover:fill-white-100 hover:text-white-100">
                                    <div class="w-1/3 ml-4">
                                        <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" viewBox="0 -960 960 960">
                                            <path d="M280-120q-33 0-56.5-23.5T200-200v-520h-40v-80h200v-40h240v40h200v80h-40v520q0 33-23.5 56.5T680-120H280Zm80-160h80v-360h-80v360Zm160 0h80v-360h-80v360Z"/>
                                        </svg>
                                    </div>
                                    <div class="w-full text-left">
                                        Delete
                                    </div>
                                </div>
                            </div>
                            <div class="flex flex-row">
                                <div class="w-full">
                                    <div class="font-semibold text-left pt-4 pl-4">Name:</div>
                                    <div class="text-left pl-4">{{ Contact.Name }}</div>
                                </div>
                                <div class="w-full">
                                    <div class="absolute right-0 flex flex-row pr-4">
                                        <div v-if="Contact.Primary" class="italic text-green-100 text-xs pt-5">Primary</div>
                                        <div v-if="Contact.Primary" class="pl-2 pt-4">
                                            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 fill-green-100" viewBox="0 -960 960 960">
                                                <path d="m344-60-76-128-144-32 14-148-98-112 98-112-14-148 144-32 76-128 136 58 136-58 76 128 144 32-14 148 98 112-98 112 14 148-144 32-76 128-136-58-136 58Zm94-278 226-226-56-58-170 170-86-84-56 56 142 142Z"/>
                                            </svg>
                                        </div>
                                        <div v-if="this.editingID != null || this.dropdownVisible!=null" class="pl-4 pt-2">
                                            <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 fill-grey-200" viewBox="0 -960 960 960">
                                                <path d="M240-400q-33 0-56.5-23.5T160-480q0-33 23.5-56.5T240-560q33 0 56.5 23.5T320-480q0 33-23.5 56.5T240-400Zm240 0q-33 0-56.5-23.5T400-480q0-33 23.5-56.5T480-560q33 0 56.5 23.5T560-480q0 33-23.5 56.5T480-400Zm240 0q-33 0-56.5-23.5T640-480q0-33 23.5-56.5T720-560q33 0 56.5 23.5T800-480q0 33-23.5 56.5T720-400Z"/>
                                            </svg>
                                        </div>
                                        <div v-else @click="openDropdown(index)" class="pl-4 pt-2">
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
                                    <div class="text-left">{{ Contact.Relationship }}</div>
                                </div>
                                <div class="w-full pr-4">
                                    <div class="text-left font-semibold">Phone:</div>
                                    <div class="text-left">{{ Contact.Phone }}</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div> 
            </div>
        </div>
    </div>
</template>

<script>
let initialValue = null;
const streetValid = (street) =>{
    if(street == ''){
        return false
    }
    return true

}
const cityValid = (city) =>{
    if(city == ''){
        return false
    }
    return true
}
const provinceValid = (province) =>{
    if(province == ''){
        return false
    }
    return true
}
const countryValid = (country) =>{
    if(country == ''){
        return false
    }
    return true
}
const postalValid = (postal) =>{
    if(postal.length != 7){
        return false
    }
    if(postal[3] != ' '){
        return false
    }
    return true
}
// (403)-220-5738
const phoneValid = (phone) =>{
    // if(phone.length != 14){
    //     return false
    // }
    // if(phone[0] != '(' || phone[4] != ')' || phone[5] != '-' || phone[9] != '-'){
    //     return false
    // }
    // for(let i = 1; i < 4; i++){
    //     if(isNaN(phone[i])){
    //         return false
    //     }
    // }
    // for(let i = 6; i < 9; i++){
    //     if(isNaN(phone[i])){
    //         return false
    //     }
    // }
    // for(let i = 10; i < 14; i++){
    //     if(isNaN(phone[i])){
    //         return false
    //     }
    // }
    if(phone.length < 10){
        return false
    }
    return true
}
const emailValid = (email) =>{  
    if(email.length < 5){
        return false
    }
    if(!email.includes('@')){
        return false
    }
    if(!email.includes('.')){
        return false
    }
    return true
}

    export default{
        name : 'ProfileInfo',
        emits: ['show-navbar','toggle-selected'],
        components:{
            
        },
        data: ()=> {
            return {
                editingID: null,
                dropdownVisible: null,
                User: {
                    First: "",
                    Last: "",
                    UCID: "",
                    DOB: "",
                    Citizenship: {
                        Country: "",
                        Status: "",
                        Residency: null,
                        Expiry: null
                    }
                },
                Address: {
                    ID: null,
                    Street: "",
                    City: "",
                    Province: "",
                    Country: "",
                    Postal: "",
                    Apt: null
                },
                Email: {
                    School: "",
                    Personal: "",
                    Preferred: ""
                },
                Phone: {
                    Home: "",
                    Mobile: "",
                    Number: null,
                    Preferred: ""
                },
                EmergencyContacts: [
                    {
                        Name: "",
                        Relationship: "",
                        Phone: "",
                        Primary: true
                    },
                    {
                        Name: "",
                        Relationship: "",
                        Phone: "",
                        Primary: false
                    }
                ]
            }
        },
        created(){
            this.fetchData();
            this.$emit('show-navbar')
            this.$emit('toggle-selected', 'profile')
        }, 
        methods:{
            async fetchData() {
                const headers = {
                    'Content-Type': 'application/json',
                    'Authorization': `Token ${this.$cookies.get("auth-token")}`
                };

                try {
                    const response = await fetch('http://127.0.0.1:8000/api/personal-info/', { headers });
                    if (!response.ok) {
                        throw new Error(`HTTP error! status: ${response.status}`);
                    }
                    const data = await response.json();
                    this.User = {
                        First: data.personal_info.firstname,
                        Last: data.personal_info.lastname,
                        UCID: data.personal_info.UCID,
                        DOB: data.personal_info["date of birth"],
                        Citizenship: {
                            Country: data.citizenship.country,
                            Status: data.citizenship.status
                        }
                    };
                    this.Address = {
                        id: data.address.id,
                        Street: data.address["street address"],
                        City: data.address.city,
                        Province: data.address["province/state"],
                        Country: data.citizenship.country,
                        Postal: data.address["postal code"]
                    };

                    this.Phone = {
                        Home: data.phone_numbers.home,
                        Mobile: data.phone_numbers.mobile,
                        Other: data.phone_numbers.other,
                        Preferred: data.phone_numbers.preferred
                    };

                    this.Email = {
                        School: data.email.school,
                        Personal: data.email.personal,
                        Preferred: data.email.preferred
                    };

                    this.EmergencyContacts = [];

                    if(data.emergency_contact.id1 != null) {
                        this.EmergencyContacts.push({
                            id: data.emergency_contact.id1,
                            Name: data.emergency_contact.name1,
                            Relationship: data.emergency_contact.relation1,
                            Phone: data.emergency_contact.phone1,
                            Primary: data.emergency_contact.preferred === "1"
                        })
                    }
                    if(data.emergency_contact.id2 != null) {
                        this.EmergencyContacts.push({
                            id: data.emergency_contact.id2,
                            Name: data.emergency_contact.name2,
                            Relationship: data.emergency_contact.relation2,
                            Phone: data.emergency_contact.phone2,
                            Primary: data.emergency_contact.preferred === "2"
                        })
                    }
                    if(data.emergency_contact.id3 != null) {
                        this.EmergencyContacts.push({
                            id: data.emergency_contact.id3,
                            Name: data.emergency_contact.name3,
                            Relationship: data.emergency_contact.relation3,
                            Phone: data.emergency_contact.phone3,
                            Primary: data.emergency_contact.preferred === "3"
                        })
                    }

                } catch (error) {
                    console.error('There was a problem with the fetch operation:', error);
                }
            },
            async editInfo(){

                const studentData = {
                    student_id: this.User.UCID,
                    student_first_name: this.User.First,
                    student_last_name: this.User.Last,
                    date_of_birth: this.User.DOB,
                    citizenship_status: this.User.Citizenship.Status,
                    home_phone_number: this.Phone.Home,
                    mobile_phone_number: this.Phone.Mobile,
                    other_phone_number: this.Phone.Other,
                    preferred_phone: this.Phone.Preferred,
                    personal_email: this.Email.Personal,
                    school_email: this.Email.School,
                    preferred_email: this.Email.Preferred
                };

                try {
                    // Update student info
                    let response = await fetch(`http://127.0.0.1:8000/api/students/${this.User.UCID}/`, {
                        method: 'PUT',
                        headers: {
                            'Content-Type': 'application/json',
                            'Authorization': `Token ${this.$cookies.get("auth-token")}`
                        },
                        body: JSON.stringify(studentData)
                    });

                    if (!response.ok) {
                        throw new Error(`HTTP error! status: ${response.status}`);
                    }

                    // Update address info
                    const addressData = {
                        address_street_address: this.Address.Street,
                        address_city: this.Address.City,
                        address_province: this.Address.Province,
                        address_country: this.Address.Country,
                        address_postal_code: this.Address.Postal
                    };
                    response = await fetch(`http://127.0.0.1:8000/api/addresses/${this.Address.id}/`, {
                        method: 'PUT',
                        headers: {
                            'Content-Type': 'application/json',
                            'Authorization': `Token ${this.$cookies.get("auth-token")}`
                        },
                        body: JSON.stringify(addressData)
                    });

                    if (!response.ok) {
                        throw new Error(`HTTP error! status: ${response.status}`);
                    }

                    // Update emergency contacts
                    for (const contact of this.EmergencyContacts) {
                        const contactData = {
                            emergency_contact_name: contact.Name,
                            emergency_contact_phone: contact.Phone,
                            emergency_contact_relationship: contact.Relationship
                        };

                        response = await fetch(`http://127.0.0.1:8000/api/emergency-contacts/${contact.id}/`, {
                            method: 'PUT',
                            headers: {
                                'Content-Type': 'application/json',
                                'Authorization': `Token ${this.$cookies.get("auth-token")}`
                            },
                            body: JSON.stringify(contactData)
                        });

                        if (!response.ok) {
                            throw new Error(`HTTP error! status: ${response.status}`);
                        }
                    }

                    if(response.ok) {
                        console.log("Everything updated successfully");
                    }

                    return true;
                } catch (error) {
                    console.error('There was a problem with the PUT request:', error);
                    return false;
                }
            },

            setEditing(element) {
                this.editingID = element;
                if(element == 'Address') {
                    initialValue = {
                        Street: this.Address.Street,
                        City: this.Address.City,
                        Province: this.Address.Province,
                        Country: this.Address.Country,
                        Postal: this.Address.Postal,
                        Apt: this.Address.Apt
                    }
                }
                else if(element == 'Phone') {
                    initialValue = {
                        Home: this.Phone.Home,
                        Mobile: this.Phone.Mobile,
                        Other: this.Phone.Other,
                        Preferred: this.Phone.Preferred
                    }
                }
                else if(element == 'Email') {
                    initialValue = {
                        School: this.Email.School,
                        Personal: this.Email.Personal,
                        Preferred: this.Email.Preferred
                    }
                }
                else if(element == 'EmergencyContacts') {
                    initialValue = {
                        Name: this.EmergencyContacts[element].Name,
                        Relationship: this.EmergencyContacts[element].Relationship,
                        Phone: this.EmergencyContacts[element].Phone,
                        Primary: this.EmergencyContacts[element].Primary
                    }
                }
                else{
                    initialValue = {
                        Name: this.EmergencyContacts[element].Name,
                        Relationship: this.EmergencyContacts[element].Relationship,
                        Phone: this.EmergencyContacts[element].Phone,
                        Primary: this.EmergencyContacts[element].Primary
                    }
                    console.log(initialValue)
                }
            },
            setView() {
                if(this.editingID !== initialValue) {
                    if(this.editingID == 'Address') {
                       if(!streetValid(this.Address.Street) || !cityValid(this.Address.City)  
                       || !provinceValid(this.Address.Province) || !countryValid(this.Address.Country) 
                       || !postalValid(this.Address.Postal)) {
                            this.editingID = null;
                            this.Address = initialValue;
                            initialValue = null;
                            return
                        }
                    }
                    else if(this.editingID == 'Phone') {
                        if(!phoneValid(this.Phone.Home) || !phoneValid(this.Phone.Mobile)) {
                            this.editingID = null;
                            this.Phone = initialValue;
                            initialValue = null;
                            return
                        }
                    }
                    else if(this.editingID == 'Email') {
                        if(!emailValid(this.Email.School) || !emailValid(this.Email.Personal)) {
                            this.editingID = null;
                            this.Email = initialValue;
                            initialValue = null;
                            return
                        }
                    }
                    else if(this.editingID == 1 || this.editingID == 0 || this.editingID == 2) {
                        if(this.EmergencyContacts[this.editingID].Name == '' || this.EmergencyContacts[this.editingID].Relationship == '' || !phoneValid(this.EmergencyContacts[this.editingID].Phone)) {
                            
                            this.EmergencyContacts[this.editingID] = initialValue;
                            initialValue = null;
                            this.editingID = null;
                            return
                        }
                    }


                    this.editInfo().then(res =>{
                        if(res){
                            this.editingID = null;
                        } else {
                            this[this.editingID] = initialValue;
                            this.editingID = null;
                        }
                    })
                }
                else{
                    this.editingID = null;
                }
                
            },
            editContact(index) {
                document.removeEventListener("click",this.eventLister)
                this.closeDropdown()
                this.setEditing(index)
            },
            eventLister(e) {
                const dropdown = document.getElementById("contact-dropdown")
                if(!dropdown.contains(e.target)) {
                    this.closeDropdown()
                    document.removeEventListener("click",this.eventLister)
                }
            },
        
            closeDropdown () {
                this.dropdownVisible = null
            },
            openDropdown(index) {
                if(this.dropdownVisible == index){
                    return
                }
                this.dropdownVisible = index
                setTimeout(() => { 
                    document.addEventListener("click",this.eventLister)
                }, 20)
            },
            togglePrimary(index) {
                document.removeEventListener("click",this.eventLister)
                this.closeDropdown()
                if(this.EmergencyContacts[index].Primary) {
                    this.EmergencyContacts[index].Primary = false
                } else {
                    this.EmergencyContacts.forEach(contact => contact.Primary = false)
                    this.EmergencyContacts[index].Primary = true
                }
            },
            removeContact(i) {
                document.removeEventListener("click",this.eventLister)
                this.closeDropdown()
                const temp = this.EmergencyContacts.filter((item,index) => i !== index)
                this.EmergencyContacts = temp
            },
            addContact() {
                this.EmergencyContacts.push({
                    Name: "Name",
                    Relationship: "Relationship",
                    Phone: '123-456-7890',
                    Primary: false
                })
                this.setEditing(this.EmergencyContacts.length - 1)
            }
        },
        beforeUnmount(){
            document.removeEventListener("click",this.eventLister)
        }
    }
</script>