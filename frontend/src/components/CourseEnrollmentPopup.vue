<template>
    <div class="bg-black-100 fixed opacity-50 w-screen h-screen z-40"></div>
    <div class="fixed w-1/3 h-auto px-4 pb-4 bg-white-100 rounded-xl left-1/2 transform -translate-x-1/2 top-1/2 -translate-y-1/2 shadow-lg z-50">
         <div class="flex flex-col">
            <div class="text-2xl font-semibold text-left p-2">
                Enrollment Summary
            </div>
            <div @click="closePopup" class="absolute right-0 p-2 cursor-pointer">
                <svg xmlns="http://www.w3.org/2000/svg" class="w-10 h-10 fill-grey-200 hover:fill-red-100" viewBox="0 -960 960 960">
                    <path d="m256-200-56-56 224-224-224-224 56-56 224 224 224-224 56 56-224 224 224 224-56 56-224-224-224 224Z"/>
                </svg>
            </div>
         </div>
         <div class="max-h-3/4 overflow-y-auto ">
            <div v-if="enrolled">
                <div v-for=" (course,index) in enrolledInfo " :key="index">
                    <div v-for="[key,value] of Object.entries(course)" :key="key">
                        <div>{{key}}</div>
                        <div>{{value}}</div>
                    </div>
                </div>
            </div>
            <div v-else class="flex flex-col divide-y divide-grey-200 divide-dashed">
                <div v-for="(course,index) in schedCourses" :key="index" class="pb-2">
                    <div class="text-left font-semibold text-lg pl-2 pb-1">{{ course.name }}:</div>
                    <div v-for="(lec,i) in course.combinations[course.selected]" :key="i">
                        <div v-if="lec[0] == 'L'" class="text-left pl-4">Lecture: {{ lec }}</div>
                        <div v-else-if="lec[0] == 'T'" class="text-left pl-4">Tutorial: {{ lec }}</div>
                        <div v-else-if="lec[0] == 'B'" class="text-left pl-4">Lab: {{ lec }}</div>
                        <div v-else class="text-left pl-4">Section: {{ lec }}</div>
                    </div>
                </div>
            </div>
        </div>
        <div class="h-12"></div>
        <div @click="enrollInCourses" class="absolute right-0 bottom-4 pt-0.5 px-2 bg-white-100 border-2 border-red-100 text-red-100 mx-10 h-10 text-2xl rounded-lg cursor-pointer hover:bg-red-100 hover:text-white-100">Enroll</div>
    </div>
 </template>
 

<script>
    export default{
        name : 'CourseEnrollmentPopup',
        props:{
            courses: {
                type: Array,
                required: true
            },
            term: {
                type: String,
                required: true
            }
        },
        data(){
            return {
                schedCourses: [],
                enrolledInfo: [],
                enrolled: false
            }
        },
        emits: ['close', 'selectcourse'],
        methods: {
            closePopup() {
                this.$emit('close')
                if(this.enrolled){
                    this.$emit('enroll')
                }
            },
            enrollInCourses(){
                const serverPath  = this.$store.state.serverPath
                const apiPath = '/api/schedule-builder/'
                const headers = {
                    'Content-Type': 'application/json',
                    'Authorization' : `Token ${this.$cookies.get("auth-token")}`
                }
                const body = new FormData()
                body.append('term', this.term)
                const courses = []
                for(let i = 0; i < this.schedCourses.length; i++){
                    courses.push(({
                        course: this.schedCourses[i].name,
                        lecture: this.schedCourses[i].combinations[this.schedCourses[i].selected][0],
                        tutorial: this.schedCourses[i].combinations[this.schedCourses[i].selected][1] ? this.schedCourses[i].combinations[this.schedCourses[i].selected][1] : false,
                    }))
                }
                body.append('courses', JSON.stringify(courses))
                this.$http.post(`${serverPath}${apiPath}`, body, {headers: headers}).then(res => {
                    console.log(res.data)
                    this.enrolledInfo = res.data
                    this.enrolled = true
                }).catch(err => {
                    console.log(err)
                })
            }
        },
        created()   {
            this.schedCourses =  this.courses

        }
        
    }
</script>