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
                <div v-for = "(course,index) in searchedCourses" :key="index">
                    <CoursePreview :course="course" :number="index" 
                    @addcourse="searchedToSched"
                    @removecourse="removeCourse"
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
                <div class="mx-1"> {{'|<'}} </div>
                <div class="mx-1"> {{ '<' }} </div>
                <div class="flex flex-col p-2">
                    <div> Result </div>
                    <div> {{ schedules.length > 0 ?  (schedIndex + 1)+ ' of ' + schedules.length : '0 of 0'}} </div>
                </div>
                <div class="mx-1"> {{'>'}} </div>
                <div class="mx-1"> {{'>|'}} </div>
            </div>
        
            <div class = "flex flex-row">
                <div class = "flex flex-col px-10 w-full">
                    <div v-for="(course,index) in schedCourses" :key="index">
                        <SelectedCourse 
                        :course="course" :number="index" :selected="0"
                        @unselect="schedToCart"
                        @removecourse="removeCourseFromSched"
                        ></SelectedCourse>
                    </div>
                    <div v-for="(course,index) in cartCourses" :key="index">
                        <SelectedCourse 
                        :course="course" :number="index" :selected="0"
                        @select="cartToSched"
                        @removecourse="removeCourseFromCart"
                        ></SelectedCourse>
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
let allCourses = []
//const worker = new Worker('./ScheduleWorker.js')
    export default{
        name : 'SchedBuilder',
        emits: ['hide-navbar'],
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
                courseSearchTerm: '',
                searchedCourses: [],
                
                cartCourses: [],
                
                schedCourses: [],
                schedules: [],
                schedIndex: 0,

                degreeRequirements: [],
                advancedSearchOpen: false,
                schedsLoading: false,
                advancedFilters: {
                },
                academicRequirementsPopup: false
            }
        },
        created(){
            this.$emit('hide-navbar')
            const backendPayload = data
            this.allInfo = backendPayload
            allCourses = this.allInfo['allCourses']
            this.degreeRequirements = this.allInfo['academic Requirements']
            this.schedCourses.forEach((item) => {
                item.included = true;
                item.selected = 0;
            })
            this.worker = new Worker('./ScheduleWorker.js')
           
        },
        methods:{
            searchResults(){
                this.searchedCourses = []
                const term = this.courseSearchTerm.toLowerCase()
                if(term == ""){
                    return;
                }
                allCourses.forEach((item) => {
                    if(item.name.toLowerCase().includes(term)){
                        if(this.courseInCart(item.name) || this.courseInSched(item.name)){
                            item.included = true;
                        }
                        else{
                            item.included = false;
                        }
                        this.searchedCourses.push(item)
                    }
                })
            },
            searchedToSched(courseName){
                const index = this.searchedCourses.findIndex((item) => {
                    return item.name == courseName
                })
                const course = this.searchedCourses[index]
                course.included = true;
                course.selected = 0;
                course.selectedIndices =  Array(course.combinations.length).fill(true)
                const newSched = [...this.schedCourses, course]
                this.schedCourses = newSched
            },
            schedToCart(courseName){
                const index = this.schedCourses.findIndex((item) => {
                    return item.name == courseName
                })
                this.cartCourses.push(this.schedCourses[index])
                this.schedCourses.splice(index, 1)
            },
            removeCourseFromCart(courseName){
                const index = this.cartCourses.findIndex((item) => {
                    return item.name == courseName
                })
                for(let i = 0; i < this.searchedCourses; i++){
                    if(this.searchedCourses[i].name == courseName){
                        this.searchedCourses[i].included = false;
                        this.searchedCourses[i].selected = 0;
                        break;
                    }
                }
                this.cartCourses.splice(index, 1)
                for(let i = 0; i < this.searchedCourses.length; i++){
                    if(this.searchedCourses[i].name == courseName){
                        this.searchedCourses[i].included = false;
                        this.searchedCourses[i].selected = 0;
                        break;
                    }
                }
            },
            removeCourseFromSched(courseName){
                const index = this.schedCourses.findIndex((item) => {
                    return item.name == courseName
                })
                for(let i = 0; i < this.searchedCourses; i++){
                    if(this.searchedCourses[i].name == courseName){
                        this.searchedCourses[i].included = false;
                        this.searchedCourses[i].selected = 0;
                        break;
                    }
                }
                this.schedCourses.splice(index, 1)
                for(let i = 0; i < this.searchedCourses.length; i++){
                    if(this.searchedCourses[i].name == courseName){
                        this.searchedCourses[i].included = false;
                        this.searchedCourses[i].selected = 0;
                        break;
                    }
                }
            },
            removeCourse(coursename){
                if(this.courseInCart(coursename)){
                    this.removeCourseFromCart(coursename)
                }
                else if(this.courseInSched(coursename)){
                    this.removeCourseFromSched(coursename)
                }
            },
            computeSchedules(){
           
                this.worker.onmessage = (e) => {
                    console.log(e.data.schedules)
                    this.schedules = e.data.schedules
                    this.schedsLoading = false
        
                }
                this.worker.onerror = (e) => {
                    console.log("error!!")
                    console.log(e)
                }
                const courses = JSON.parse(JSON.stringify(this.schedCourses));
                this.worker.postMessage({
                    courses: courses
                })
                
                // console.log("message posted!!")
                // this.schedsLoading = true
    
            },
            cartToSched(courseName){
                const index = this.cartCourses.findIndex((item) => {
                    return item.name == courseName
                })
                this.schedCourses.push(this.cartCourses[index])
                this.cartCourses.splice(index, 1)
            },
            courseInSched(courseName){
                for(let i = 0; i < this.schedCourses.length; i++){
                    if(this.schedCourses[i].name == courseName){
                        return true;
                    }
                }
                return false;
            },
            courseInCart(courseName){
               for(let i = 0; i < this.cartCourses.length; i++){
                   if(this.cartCourses[i].name == courseName){
                       return true;
                   }
                }
                return false;
            },
        },
        computed:{
            
        },
        watch:{
            schedCourses:{
                handler(newList, oldList) {
                    console.log('schedCourses changed:', newList, oldList);
                    if (newList.length !== oldList.length) {
                        this.computeSchedules();
                    }
                    else{
                        console.log("no change")
                    }
                },
                deep: true,
            },
            schedules:{
                handler(){
                    this.schedIndex = 0
                },
                deep: true
                
            },
            schedIndex:{
                handler(){
                    for(let i = 0; i < this.schedCourses.length; i++){
                        this.schedCourses[i].selected = this.schedules[this.schedIndex][i]
                    }
                }
            }


        }
    }
</script>

