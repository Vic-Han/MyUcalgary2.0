<!-- This is the SchedBuilder component that toggles when the route is set to schedule -->
<template>
    <AdvancedSearch v-if="advancedSearchOpen" @close="advancedSearchOpen = false"></AdvancedSearch>
    <AcademicSchedulePopup v-if="academicRequirementsPopup" :requirements="degreeRequirements" @close="academicRequirementsPopup = false" @selectcourse="addCourseFromRequirements"></AcademicSchedulePopup>
    <div class="flex flex-row">
        <div class=" px-2 flex flex-col h-screen box-content bg-white-100 shadow-xl">
            <a href="https://www.ucalgary.ca/" target="_blank">
                <img  src="@/assets/unilogo.png" alt="University Logo" class="w-96 self-center">
            </a>
            <router-link to="/dashboard" class="flex flex-row py-6 items-center" @mouseenter="backHover = true" @mouseleave="backHover = false">
                <div class="w-1/3 relative">
                    <svg xmlns="http://www.w3.org/2000/svg" class="absolute rotate-90 h-16 w-16 fill-grey-200 -translate-y-8 right-1" v-bind:class="{'fill-red-100' : backHover}" viewBox="0 -960 960 960">
                        <path d="M480-345 240-585l56-56 184 184 184-184 56 56-240 240Z"/>
                    </svg>
                </div>
                <div class="font-semibold text-grey-200 text-2xl" v-bind:class="{'text-red-100' : backHover}">Back to Home</div>
            </router-link>
            <div class="flex flex-row items-center w-full relative left-5">
                <input type="text" placeholder="search" @keydown="searchResults" v-model="courseSearchTerm" class="w-2/3 text-xl pl-2 h-9 border border-black-100 rounded-md outline-red-100 ">
                <div class="text-lg w-fit px-3 cursor-pointer text-left text-grey-200 hover:text-red-100" @click="advancedSearchOpen = true"> Advanced Search</div>
            </div>
            <div class="h-4/6 overflow-y-auto w-96">
                <div v-for="(course,index) in searchedCourses" :key="index">
                    <CoursePreview :course="course" :number="computeColor(course.name)" 
                    @addcourse="searchedToSched"
                    @removecourse="removeCourse"
                    ></CoursePreview>
                </div>
            </div>
            <div @click="academicRequirementsPopup=true" class="relative left-1/2 -translate-x-1/2 border-4 border-red-100 rounded-lg text-red-100 font-semibold cursor-pointer w-fit text-center p-3 hover:bg-red-100 hover:text-white-100"> Academic Requirements</div>
        </div>
        <div class="flex flex-col w-full">
            <div class="bg-white-100 rounded-xl shadow-xl m-4">
                <div class="flex flex-row relative left-1/2 -translate-x-1/2 w-fit my-5">
                    <div class="text-5xl mx-5">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-20 w-20 rotate-90 fill-grey-200 hover:fill-red-100" viewBox="0 -960 960 960">
                            <path d="M480-345 240-585l56-56 184 184 184-184 56 56-240 240Z"/>
                        </svg>
                    </div> 
                    <div class="text-5xl pt-4 mx-40 text-grey-200">Fall 2024</div>
                    <div class="text-5xl mx-5">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-20 w-20 -rotate-90 fill-grey-200 hover:fill-red-100" viewBox="0 -960 960 960">
                            <path d="M480-345 240-585l56-56 184 184 184-184 56 56-240 240Z"/>
                        </svg>
                    </div>
                    
                </div>
                <div class="flex flex-row relative left-1/2 -translate-x-1/2 w-fit mb-5">
                    <div class="text-3xl mx-4 mt-4" @click="resetSelectedToZero">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-14 w-14 fill-grey-200 hover:fill-red-100" viewBox="0 -960 960 960">
                            <path d="M240-240v-480h80v480h-80Zm440 0L440-480l240-240 56 56-184 184 184 184-56 56Z"/>
                        </svg>
                    </div>
                    <div class="text-3xl mx-4 mt-4" @click="decrementSchedIndex">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-14 w-14 rotate-90 fill-grey-200 hover:fill-red-100" viewBox="0 -960 960 960">
                            <path d="M480-345 240-585l56-56 184 184 184-184 56 56-240 240Z"/>
                        </svg>
                    </div>
                    <div class="flex flex-col p-2 mx-8">
                        <div class="text-3xl text-grey-200"> Result </div>
                        <div class="text-3xl text-grey-200"> {{ schedules.length > 0 ?  (schedIndex + 1)+ ' of ' + schedules.length : '0 of 0'}} </div>
                    </div>
                    <div class="text-3xl mx-4 mt-4" @click="incrementSchedIndex">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-14 w-14 -rotate-90 fill-grey-200 hover:fill-red-100" viewBox="0 -960 960 960">
                            <path d="M480-345 240-585l56-56 184 184 184-184 56 56-240 240Z"/>
                        </svg>
                    </div>
                    <div class="text-3xl mx-4 mt-4" @click="setSelectedToLast">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-14 w-14 rotate-180 fill-grey-200 hover:fill-red-100" viewBox="0 -960 960 960">
                            <path d="M240-240v-480h80v480h-80Zm440 0L440-480l240-240 56 56-184 184 184 184-56 56Z"/>
                        </svg>
                    </div>
                </div>
            </div>
            <div class="grid grid-cols-11 h-200">
                <div class="col-span-4 flex flex-col px-10 h-full bg-white-100 rounded-xl shadow-xl mb-4 mx-4 p-4">
                    <div v-if="schedCourses.length+cartCourses.length == 0" class="text-grey-200 text-2xl font-semibold pt-20"> Add Courses to Your Schedule by Searching for a Course </div>
                    <div v-for="(course,index) in schedCourses" :key="index">
                        <SelectedCourse 
                        :course="course" :number="index"
                        @unselect="schedToCart"
                        @removecourse="removeCourseFromSched"
                        @addsection="addSection"
                        @removesection="removeSection"
                        @selectall="reselectall"
                        @selectset="updateset"
                        ></SelectedCourse>
                    </div>
                    <div v-for="(course,index) in cartCourses" :key="index">
                        <SelectedCourse 
                        :course="course" :number="index + schedCourses.length"
                        @select="cartToSched"
                        @removecourse="removeCourseFromCart"
                        @addsection="addSection"
                        @removesection="removeSection"
                        @selectall="reselectall"
                        @selectset="updateset"
                        ></SelectedCourse>
                    </div>
                </div>
                <div class="flex flex-col items-center col-span-7 h-full bg-white-100 rounded-xl shadow-xl mb-4 mr-4 p-4">
                    <!-- <SchedPreview :sched="schedules.length > 0 ? schedules[selectedSched] : null"> </SchedPreview> -->
                    <SchedPreview :schedule="courseListToSched()"></SchedPreview>
                    <div class="border-4 font-semibold border-red-100 mt-4 w-fit relative left-1/3 translate-x-2 p-3 text-xl rounded-xl text-red-100 hover:bg-red-100 hover:text-white-100"
                    @click="getSchedule">Get Schedule</div>
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
                backHover: false,
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
            addCourseFromRequirements(course){
                this.searchedCourses = []
                for(let i = 0; i < allCourses.length; i++){
                    if(allCourses[i].name == course){
                        allCourses[i].included = 'sched';
                        allCourses[i].selected = 0;
                        allCourses[i].selectedIndices = Array(allCourses[i].combinations.length).fill(true)
                        const newSched = [...this.schedCourses, allCourses[i]]
                        this.schedCourses = newSched
                        break;
                    }
                }
                this.academicRequirementsPopup = false
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
            },
            reselectall(courseName){
                console.log('reselecting all')
                for(let i = 0; i < this.schedCourses.length; i++){
                    if(this.schedCourses[i].name === courseName){
                        const newSched = [...this.schedCourses]
                        newSched[i].selectedIndices = Array(newSched[i].combinations.length).fill(true)
                        this.schedCourses = newSched
                        this.computeSchedules()
                        return
                    }
                }
                for(let i = 0; i < this.cartCourses.length; i++){
                    if(this.cartCourses[i].name === courseName){
                        this.cartCourses[i].selectedIndices = Array(this.cartCourses[i].combinations.length).fill(true)
                        return
                    } 
                }
            },
            updateset(courseName, newList){
                for(let i = 0; i < this.schedCourses.length; i++){
                    if(this.schedCourses[i].name === courseName){
                        const newSched = [...this.schedCourses]
                        newSched[i].selectedIndices = [...newList]
                        this.schedCourses = newSched
                        this.computeSchedules()

                        return
                    }
                }
                for(let i = 0; i < this.cartCourses.length; i++){
                    if(this.cartCourses[i].name === courseName){
                        this.cartCourses[i].selectedIndices = [...newList]
                        return
                    }
                }
            },
            applyAdvancedFilters(filters){
                this.advancedSearchOpen = false
                console.log(filters)
            },
            getSchedule(){
                console.log('getting schedule')
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

