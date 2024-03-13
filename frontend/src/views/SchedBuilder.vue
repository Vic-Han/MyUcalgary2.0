<!-- This is the SchedBuilder component that toggles when the route is set to schedule -->
<template>
    <AdvancedSearch v-if="advancedSearchOpen" @close="advancedSearchOpen = false"></AdvancedSearch>
    <AcademicSchedulePopup v-if="academicRequirementsPopup" :requirements="degreeRequirements" @close="academicRequirementsPopup = false"></AcademicSchedulePopup>
    <div class = "flex flex-row">
        <div class = "w-96 flex flex-col h-screen">
            <img src = "@/assets/unilogo.png " class = "w-10/12">
            <div class = "flex flex-row w-10/12 relative left-5">
                <input type = "text" v-model="courseSearchTerm" class = "w-40 border border-black-100">
                <div class = "mx-3" @click = "searchResults"> Search</div>
                <div @click = "advancedSearchOpen = true"> Advanced </div>
            </div>
            <div class = "h-4/6 overflow-y-auto">
                    <div v-for = "(course,index) in courseSearchResults" :key="index">
                    <CoursePreview :course="course" :number="index" 
                    @addcourse="addCourseToCart"
                    @removecourse="removeCourseFromSelected"
                    ></CoursePreview>
                    </div>
                
            </div>
            <div @click="academicRequirementsPopup=true"> Academic Requirements</div>
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
                <div class = "flex flex-col px-10 w-full">
                    <div v-for="(course,index) in currentSched" :key="index">
                        <SelectedCourse :course="course" :number="index" :selected="0"></SelectedCourse>
                    </div>
                    <div v-for="(course,index) in selectedCourses" :key="index">
                        <div v-if="!courseInSched(course.name)">
                            <SelectedCourse :course="course" :number="index" :selected="0"></SelectedCourse>

                        </div>
    
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
import AcademicSchedulePopup from '@/components/AcademicSchedulePopup.vue'
import data from './SB.json'
import SampleSchedule from './SampleSched.json'

    export default{
        name : 'SchedBuilder',
        components: {
            SchedPreview,
            CoursePreview,
            SelectedCourse,
            AdvancedSearch,
            AcademicSchedulePopup
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
                workers:[],
                advancedFilters: {
                },
                academicRequirementsPopup: false
                
            }
        },
        created(){
            this.$emit('hide-navbar')
            const backendPayload = data
            this.allInfo = backendPayload
            this.courses = this.allInfo['allCourses']
            this.degreeRequirements = this.allInfo['academic Requirements']
            this.worker = new Worker('./ScheduleWorker.js')
            
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
                        if(this.courseInSelected(item.name) || this.courseInSched(item.name)){
                            item.included = true;
                        }
                        else{
                            item.included = false;
                        }
                        
                        console.log(item)
                        this.courseSearchResults.push(item)
                    }
                })
            },
            addCourseToCart(courseName){
                const index = this.courseSearchResults.findIndex((item) => {
                    return item.name == courseName
                })
                console.log(this.courseSearchResults[index])
                console.log("this.courseSearchResults[index].included")
                this.courseSearchResults[index].included = true;
                this.courseSearchResults[index].selected = 0;
                this.selectedCourses.push(this.courseSearchResults[index])
            },
            removeCourseFromSelected(courseName){
                this.selectedCourses = this.selectedCourses.filter((item) => {
                    return item.name != courseName
                })
                this.courseSearchResults.forEach((item) => {
                    if(item.name == courseName){
                        item.included = false;
                    }
                })
                for(let i = 0; i < this.currentSched.length; i++){
                    if(this.currentSched[i].name == courseName){
                        this.currentSched.splice(i, 1)
                        this.computeSchedules()
                    }
                }
                return courseName
            },
            computeSchedules(){
                
            },
            courseInSched(courseName){
                for(let i = 0; i < this.currentSched.length; i++){
                    if(this.currentSched[i].name == courseName){
                        return true;
                    }
                }
                return false;
            },
            courseInSelected(courseName){
               for(let i = 0; i < this.selectedCourses.length; i++){
                   if(this.selectedCourses[i].name == courseName){
                       return true;
                   }
                }
                return false;
            },
            addCourseToSched(courseName){
                const index = this.selectedCourses.findIndex((item) => {
                    return item.name == courseName
                })
                this.currentSched.push(this.selectedCourses[index])
                this.selectedCourses.splice(index, 1)
                this.computeSchedules()
            },
        },
        computed:{
            
        }
    }
</script>

