<template>
    <div class="bg-white-100 fixed w-screen h-screen z-30"></div>
    <div class="fixed w-1/3 h-3/4 z-40 bg-white rounded-xl left-1/2 transform -translate-x-1/2 top-1/3 -translate-y-1/2 shadow-lg">
         <div class="flex flex-col p-8">
             <div class="flex justify-between items-center mb-6">
                 <h2 class="text-2xl font-semibold">Degree Requirements</h2>
                 <button @click="closePopup" class="text-lg font-semibold cursor-pointer">Close</button>
             </div>
             <div class="mb-4">
                 <p><span class="font-semibold">Units:</span> 120.00 required, 114.00 taken, 6.00 needed</p>
             </div>
             <div class="mb-4">
                 <h3 class="font-semibold mb-2">Required Courses</h3>
                 <div class="flex flex-col">
                     <div>
                         <p class="font-semibold">Major Field</p>
                         <!-- Course boxes here -->
                     </div>
                     <div>
                         <p class="font-semibold">Math</p>
                         <!-- Course boxes here -->
                     </div>
                     <div>
                         <p class="font-semibold">Logic</p>
                         <!-- Course boxes here -->
                     </div>
                     <div>
                         <p class="font-semibold">Ethics</p>
                         <!-- Course boxes here -->
                     </div>
                 </div>
             </div>
             <div class="flex items-center">
                 <span class="w-4 h-4 mr-2 bg-green-500 inline-block rounded-full"></span>
                 <span class="mr-4">Open</span>
                 <span class="w-4 h-4 mr-2 bg-yellow-500 inline-block rounded-full"></span>
                 <span class="mr-4">Waitlistable</span>
                 <span class="w-4 h-4 mr-2 bg-red-500 inline-block rounded-full"></span>
                 <span>Closed</span>
             </div>
         </div>
    </div>
 </template>
 

<script>
    export default{
        name : 'AcademicSchedulePopup',
        props:{
            requirements: {
                type: Object,
                required: true
            }
        },
        emits: ['close', 'selectcourse'],
        methods: {
            closePopup() {
                this.$emit('close')
            },
            selectCourse(course){
                this.$emit('selectcourse',course)
            }
        },
        created(){
            // delete the whole "created" method afterwards
            // this is just for you to see what this object looks like!
            console.log(this.requirements)

        }
    }
</script>