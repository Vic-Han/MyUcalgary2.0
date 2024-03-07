<!-- This is the SchedBuilder component that toggles when the route is set to schedule -->
<template>
    <div class = "flex flex-row w-96">
        <div class = "w-96 flex flex-col">
            <img src = "@/assets/unilogo.png " class = "w-10/12">
            <div class = "flex flex-row w-10/12 relative left-5">
                <input type = "text" v-model="courseSearchTerm" class = "w-40 border border-black-100">
                <div @click = "searchResults"> Search</div>
            </div>
            <div>
                <div v-for = "(course,index) in courseSearchResults" :key="index">
                <CoursePreview :course="course" :number="index"></CoursePreview>
                </div>
            </div>
        </div>
        <div>
            <div class = "flex flex-row">
                <div> Back </div> 
                <div>Fall 2024</div>
                <div> Forward</div>
                
            </div>
            <div class = "flex flex-row">
                <div>  Back </div>
                <div> {{selectedSched}} </div>
                <div> Forward</div>
            </div>
        
            <div class = "flex flex-row">
                <div class = "flex flex-col w-60">
                    <div v-for="(course,index) in selectedCourses" :key="index">
                        <SelectedCourse></SelectedCourse>
                        {{course}}
                    </div>
                </div>
                <div class = "flex flex-col">
                    <SchedPreview :sched="schedules.length > 0 ? schedules[selectedSched] : null"> </SchedPreview>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import SchedPreview from '@/components/SchedPreview.vue'
import CoursePreview from '@components/CoursePreview.vue'
import SelectedCourse from '@components/SelectedCourse.vue'
import data from './SB.json'
    export default{
        name : 'SchedBuilder',
        components: {
            SchedPreview,
            CoursePreview,
            SelectedCourse
        },
        data : () => {
            return {
                allInfo: {
                },
                selectedTerm: '',
                courses: [],
                courseSearchResults: [],
                courseSearchTerm: '',
                selectedCourses: [],
                selectedSched: 0,
                schedules: [],
                degreeRequirements: [],

                schedsLoading: false,
                advancedFilters: {

                },
                
            }
        },
        created(){
            this.$emit('hide-navbar')
            const backendPayload = data
            this.allInfo = backendPayload
            this.courses = this.allInfo['allCourses']
            this.degreeRequirements = this.allInfo['academic Requirements']

            
        },
        methods:{
            searchResults(){
                const term = this.courseSearchTerm.toLowerCase()
                this.courses.forEach((item) => {
                    if(item.name.toLowerCase().includes(term)){
                        console.log(item.name)
                        this.courseSearchResults.push(item)
                    }
                    else if(item.desc.toLowerCase().includes(term)){
                        this.courseSearchResults.push(item)
                    }
                })
            },
            addCourseToOptions(course){
                this.selectedCourses.push(course)
            }
        }
    }
</script>