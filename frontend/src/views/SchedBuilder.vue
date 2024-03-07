<!-- This is the SchedBuilder component that toggles when the route is set to schedule -->
<template>
    <AdvancedSearch v-if="advancedSearchOpen" @close="advancedSearchOpen = false"></AdvancedSearch>
    <div class = "flex flex-row w-96">
        <div class = "w-96 flex flex-col">
            <img src = "@/assets/unilogo.png " class = "w-10/12">
            <div class = "flex flex-row w-10/12 relative left-5">
                <input type = "text" v-model="courseSearchTerm" class = "w-40 border border-black-100">
                <div class = "mx-3" @click = "searchResults"> Search</div>
                <div @click = "advancedSearchOpen = true"> Advanced </div>
            </div>
            <div>
                <div v-for = "(course,index) in courseSearchResults" :key="index">
                <CoursePreview :course="course" :number="index" 
                @addcourse="addCourseToCart"
                ></CoursePreview>
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
                    <!-- <SchedPreview :sched="schedules.length > 0 ? schedules[selectedSched] : null"> </SchedPreview> -->
                    <SchedPreview :schedule="currentSched"></SchedPreview>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import SchedPreview from '@/components/SchedPreview.vue'
import CoursePreview from '@/components/CoursePreview.vue'
import SelectedCourse from '@/components/SelectedCourse.vue'
import AdvancedSearch from '@/components/AdvancedSearch.vue'
import data from './SB.json'
import SampleSchedule from './SampleSched.json'
    export default{
        name : 'SchedBuilder',
        components: {
            SchedPreview,
            CoursePreview,
            SelectedCourse,
            AdvancedSearch
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
                currentSched: SampleSchedule,
                schedules: [],
                degreeRequirements: [],
                advancedSearchOpen: false,
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
                this.courseSearchResults = []
                const term = this.courseSearchTerm.toLowerCase()
                if(term == ""){
                    return;
                }
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
            addCourseToCart(course){
                this.selectedCourses.push(course)
            }
        }
    }
</script>