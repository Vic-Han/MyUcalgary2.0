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
                <div class="mx-1" @click="resetSelectedToZero"> {{'|<'}} </div>
                <div class="mx-1" @click="decrementSchedIndex"> {{ '<' }} </div>
                <div class="flex flex-col p-2">
                    <div> Result </div>
                    <div> {{ schedules.length > 0 ?  (schedIndex + 1)+ ' of ' + schedules.length : '0 of 0'}} </div>
                </div>
                <div class="mx-1" @click="incrementSchedIndex"> {{'>'}} </div>
                <div class="mx-1" @click="setSelectedToLast"> {{'>|'}} </div>
            </div>
        
            <div class = "flex flex-row">
                <div class = "flex flex-col px-10 w-full">
                    <div v-for="(course,index) in schedCourses" :key="index">
                        <SelectedCourse 
                        :course="course" :number="index"
                        @unselect="schedToCart"
                        @removecourse="removeCourseFromSched"
                        ></SelectedCourse>
                    </div>
                    <div v-for="(course,index) in cartCourses" :key="index">
                        <SelectedCourse 
                        :course="course" :number="index"
                        @select="cartToSched"
                        @removecourse="removeCourseFromCart"
                        ></SelectedCourse>
                    </div>
                </div>
                <div class = "flex flex-col">
                    <!-- <SchedPreview :sched="schedules.length > 0 ? schedules[selectedSched] : null"> </SchedPreview> -->
                    <SchedPreview :schedule="courseListToSched()"></SchedPreview>
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
                const course = this.schedCourses[index]
                course.included = false;
                const newCart = [...this.cartCourses, course]
                this.cartCourses = newCart
                const newSched = this.schedCourses.filter((item) => {
                    return item.name != courseName
                })
                this.schedCourses = newSched
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
                const newSched = this.schedCourses.filter((item) => {
                    return item.name != courseName
                })
                this.schedCourses = newSched
    
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
                    //console.log(e.data.schedules)
                    this.schedules = e.data.schedules
                    this.schedsLoading = false
        
                }
                this.worker.onerror = (e) => {
                    console.log(e)
                }
                const courses = JSON.parse(JSON.stringify(this.schedCourses));
                this.worker.postMessage({
                    courses: courses
                })
                
               
                this.schedsLoading = true
    
            },
            cartToSched(courseName){
                const index = this.cartCourses.findIndex((item) => {
                    return item.name == courseName
                })
                const course = this.cartCourses[index]
                course.included = true;
                const newSched = [...this.schedCourses, course]
                this.schedCourses = newSched
                const newCart = this.cartCourses.filter((item) => {
                    return item.name != courseName
                })
                this.cartCourses = newCart
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
            courseListToSched(){
                let sched = []
                for(let i = 0; i < this.schedCourses.length; i++){
                    const course = this.schedCourses[i]
                    const selected = course.combinations[course.selected]
                    console.log(selected)
                    const schedCourse = {
                        courseCode: course.name,
                        courseTitle : course.title,
                        Lecture : null,
                        Tutorial:null
                    }
                    const lecture = {
                            days : null,
                            start : null,
                            end : null,
                            roomno: null,
                            LectureNO : null
                    }
                    for(let j = 0; j < course.lectures.length; j++){
                        console.log(course.lectures[j].name, selected[0])
                        if(course.lectures[j].name === selected[0]){
                            lecture.days = course.lectures[j].days
                            lecture.start = course.lectures[j].start
                            lecture.end = course.lectures[j].end
                            lecture.roomno = course.lectures[j].roomno
                            lecture.LectureNO = course.lectures[j].name
                            break
                        }
                    }
                    schedCourse.Lecture = lecture
                    if(selected.length > 1){
                        const tutorial = {
                            days : null,
                            start : null,
                            end : null,
                            roomno: null,
                            TutorialNO : null
                        }
                        for(let j = 0; j < course.tutorials.length; j++){
                            if(course.tutorials[j].name === selected[1]){
                                tutorial.days = course.tutorials[j].days
                                tutorial.start = course.tutorials[j].start
                                tutorial.end = course.tutorials[j].end
                                tutorial.roomno = course.tutorials[j].roomno
                                tutorial.TutorialNO = course.tutorials[j].name
                                break
                            }
                        }
                        schedCourse.Tutorial = tutorial
                    }
                    console.log(schedCourse)
                    sched.push(schedCourse)
                }
                return sched
            },
            resetSelectedToZero(){
                this.schedIndex = 0;
            },
            setSelectedToLast(){
                if(this.schedules.length > 0){
                    this.schedIndex = this.schedules.length - 1;
                }
            },
            incrementSchedIndex(){
                if(this.schedIndex < this.schedules.length - 1){
                    this.schedIndex = this.schedIndex + 1;
                }
            },
            decrementSchedIndex(){
                if(this.schedIndex > 0){
                    this.schedIndex = this.schedIndex - 1;
                }
            }

        },
        computed:{
            
        },
        watch:{
            schedCourses:{
                handler(newList, oldList) {
                    
                    if (newList.length !== oldList.length) {
                        this.computeSchedules();
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

