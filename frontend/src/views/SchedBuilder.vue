<!-- This is the SchedBuilder component that toggles when the route is set to schedule -->
<template>
    <AdvancedSearch v-if="advancedSearchOpen" @close="advancedSearchOpen = false"></AdvancedSearch>
    <AcademicSchedulePopup v-if="academicRequirementsPopup" :requirements="degreeRequirements" @close="academicRequirementsPopup = false"></AcademicSchedulePopup>
    <div class = "flex flex-row">
        <div class = "w-fit flex flex-col h-screen box-content">
            <img src = "@/assets/unilogo.png " class = "w-96 mx-12">
            <div class = "flex flex-row w-full relative left-5">
                <input type="text" placeholder="search" @keydown.enter="searchResults" v-model="courseSearchTerm" class="w-60 text-xl h-9 border border-black-100 rounded-md">
                <div class="text-lg" @click = "advancedSearchOpen = true"> Advanced Search</div>
            </div>
            <div class = "h-4/6 overflow-y-auto">
                <div v-for = "(course,index) in searchedCourses" :key="index">
                    <CoursePreview :course="course" :number="computeColor(course.name)" 
                    @addcourse="searchedToSched"
                    @removecourse="removeCourse"
                    ></CoursePreview>
                </div>
            </div>
            <div @click="academicRequirementsPopup=true"> Academic Requirements</div>
        </div>
        <div class="flex flex-col w-full">
            <div class = "flex flex-row relative left-1/2 -translate-x-1/2 w-fit my-5">
                <div class="text-5xl mx-5">  {{ '<' }} </div> 
                <div class="text-5xl mx-40">Fall 2024</div>
                <div class="text-5xl mx-5"> {{'>'}}</div>
                
            </div>
            <div class = "flex flex-row relative left-1/2 -translate-x-1/2 w-fit mb-5">
                <div class="text-3xl mx-4 mt-4" @click="resetSelectedToZero"> {{'|<'}} </div>
                <div class="text-3xl mx-4 mt-4" @click="decrementSchedIndex"> {{ '<' }} </div>
                <div class="flex flex-col p-2 mx-8">
                    <div class="text-3xl"> Result </div>
                    <div class="text-3xl"> {{ schedules.length > 0 ?  (schedIndex + 1)+ ' of ' + schedules.length : '0 of 0'}} </div>
                </div>
                <div class="text-3xl mx-4 mt-4" @click="incrementSchedIndex"> {{'>'}} </div>
                <div class="text-3xl mx-4 mt-4" @click="setSelectedToLast"> {{'>|'}} </div>
            </div>
        
            <div class = "grid grid-cols-11">
                <div class = "col-span-4 flex flex-col px-10 -translate-y-10">
                    <div v-for="(course,index) in schedCourses" :key="index">
                        <SelectedCourse 
                        :course="course" :number="index"
                        @unselect="schedToCart"
                        @removecourse="removeCourseFromSched"
                        @addsection="addSection"
                        @removesection="removeSection"
                        ></SelectedCourse>
                    </div>
                    <div v-for="(course,index) in cartCourses" :key="index">
                        <SelectedCourse 
                        :course="course" :number="index + schedCourses.length"
                        @select="cartToSched"
                        @removecourse="removeCourseFromCart"
                        @addsection="addSection"
                        @removesection="removeSection"
                        ></SelectedCourse>
                    </div>
                </div>
                <div class = "flex flex-col col-span-7">
                    <!-- <SchedPreview :sched="schedules.length > 0 ? schedules[selectedSched] : null"> </SchedPreview> -->
                    <SchedPreview :schedule="courseListToSched()"></SchedPreview>
                    <div class="border border-grey-200 mt-4 w-fit relative left-1/2 -translate-x-1/2 p-10 text-xl rounded-xl"> Get Schedule!</div>
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
                item.included = 'sched';
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
                        if(this.courseInSched(item.name)){
                            item.included = 'sched';
                        }
                        else if(this.courseInCart(item.name) ){
                            item.included = 'cart';
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
                course.included = 'sched';
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
                course.included = 'cart';
                const newCart = [...this.cartCourses, course]
                this.cartCourses = newCart
                const newSched = this.schedCourses.filter((item) => {
                    return item.name != courseName
                })
                this.schedCourses = newSched
            },
            removeCourseFromCart(courseName){
                const newCart = this.cartCourses.filter((item) => {
                    return item.name != courseName
                })
                this.cartCourses = newCart
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
                course.included = 'sched';
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
            },
            computeColor(courseName){
                for(let i = 0; i < this.schedCourses.length; i++){
                    if(this.schedCourses[i].name === courseName){
                        return i
                    }
                }
                for(let i = 0; i < this.cartCourses.length; i++){
                    if(this.cartCourses[i].name === courseName){
                        return i + this.schedCourses.length
                    }
                }
                return this.schedCourses.length + this.cartCourses.length
            },
            addSection(courseName,sectionIndex){
                for(let i = 0; i < this.schedCourses.length; i++){
                    if(this.schedCourses[i].name === courseName){
                        const newSched = [...this.schedCourses]
                        newSched[i].selectedIndices[sectionIndex] = true
                        this.schedCourses = newSched
                        this.computeSchedules()
                        return
                    }
                }
                for(let i = 0; i < this.cartCourses.length; i++){
                    if(this.cartCourses[i].name === courseName){
                        this.cartCourses[i].selectedIndices[sectionIndex] = true
                        return
                    }
                }
            },
            removeSection(courseName, sectionIndex){
                for(let i = 0; i < this.schedCourses.length; i++){
                    if(this.schedCourses[i].name === courseName){
                        const newSched = [...this.schedCourses]
                        newSched[i].selectedIndices[sectionIndex] = false
                        this.schedCourses = newSched
                        this.computeSchedules()
                        return
                    }
                }
                for(let i = 0; i < this.cartCourses.length; i++){
                    if(this.cartCourses[i].name === courseName){
                        this.cartCourses[i].selectedIndices[sectionIndex] = false
                        return
                    }
                }
            }

        },
        computed:{
            
        },
        watch:{
            schedCourses:{
                handler(newList, oldList) {
                    
                    if (newList.length !== oldList.length) {
                        this.computeSchedules()
                        return
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

