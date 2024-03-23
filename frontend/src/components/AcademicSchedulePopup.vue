<template>
    <div class="bg-black-100 fixed opacity-50 w-screen h-screen z-30"></div>
    <div class="fixed w-1/3 h-auto max-h-3/4 overflow-y-auto px-4 pb-4 bg-white-100 rounded-xl left-1/2 transform -translate-x-1/2 top-1/2 -translate-y-1/2 shadow-lg z-40">
         <div class="flex flex-col">
            <div @click="closePopup" class="absolute right-0 p-2 cursor-pointer">
                <svg xmlns="http://www.w3.org/2000/svg" class="w-10 h-10 fill-grey-200 hover:fill-red-100" viewBox="0 -960 960 960">
                    <path d="m256-200-56-56 224-224-224-224 56-56 224 224 224-224 56 56-224 224 224 224-56 56-224-224-224 224Z"/>
                </svg>
            </div>
            <div class="text-2xl font-bold m-2 pt-8">Course Requirements</div>
            <div class="text-2xl font-bold m-2">Click on a course to add it to cart!</div>
             <div v-for=" (value,key) in requirements" :key="key" class="my-1">
                <div class="font-semibold text-lg">{{key}} :</div>
                <div class="flex flex-row flex-wrap">
                    <div v-if="value.length == 0" class="p-2 m-2 bg-gray-200 rounded-lg">No courses available</div>
                    <div v-else-if=" /^[a-zA-Z]$/.test(value[0])" class="cursor-pointer p-2 m-2 bg-gray-200 rounded-lg hover:bg-gray-300" @click="selectCourse(value)"> {{ value }}</div>
                    <div v-else class="flex flex-row flex-wrap">
                        <div v-for="course in value" :key="course" @click="selectCourse(course)" class="cursor-pointer p-2 m-2 bg-gray-200 rounded-lg hover:bg-gray-300">{{course}}</div>
                    </div>
                </div>
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
        
    }
</script>