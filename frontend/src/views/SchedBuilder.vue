<!-- This is the SchedBuilder component that toggles when the route is set to schedule -->
<template>
    <AdvancedSearch v-if="advancedSearchOpen" @close="advancedSearchOpen = false"></AdvancedSearch>
    <div class = "flex flex-row">
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
                <div class = "flex flex-col px-10 w-full">
                    <div v-for="(course,index) in selectedCourses" :key="index">
                        <SelectedCourse :course="course" :number="index"></SelectedCourse>
    
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
                workers:[],
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
            this.workers.push(new Worker('ScheduleWorker.js'))
            
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
            addCourseToCart(index){
                this.selectedCourses.push(this.courseSearchResults[index])
                const newArr = this.courseSearchResults.filter((item) => {
                    return item != this.courseSearchResults[index]
                })
                this.courseSearchResults = newArr
            },
            computeSchedules(){
                
            }
        }
    }
</script>

<!-- 
    The backend should give us the courses in the following manner:

    {
        Course info: blah blah,
        Availible sessions:
        [
            ["L1", "T1"],
            ["L2", "T1"],
            ["L1", "T2"],
            ["L2", "T2"],
        ],
        "lectures": {
                "L1":{
                    "days": "TTH",
                    "start": 14,
                    "end": 15.25,
                    "Prof": "Shah",
                    "totalSeats": 100,
                    "seatsFilled": 50,
                    "totalWaitlist": 10,
                    "waitlistFilled": 0,
                    "roomno": "ST 132"
                },
                "L2":{ 
                    "days": "MF",
                    "start": 14,
                    "end": 15.25,
                    "Prof": "Krishnamurthy",
                    "totalSeats": 100,
                    "seatsFilled": 50,
                    "totalWaitlist": 10,
                    "waitlistFilled": 0,
                    "roomno": "ST 132"
                }
            },
            "tutorials": {
                "T1":{
                    "days": "W",
                    "start": 14,
                    "end": 16,
                    "TA": "Lets not implement this :)",
                    "totalSeats": 100,
                    "seatsFilled": 50,
                    "totalWaitlist": 10,
                    "waitlistFilled": 0,
                    "roomno": "ENG 201"
                },
                "T2":{
                    "days": "M",
                    "start": 16,
                    "end": 18,
                    "TA": "Lets not implement this :)",
                    "totalSeats": 100,
                    "seatsFilled": 50,
                    "totalWaitlist": 10,
                    "waitlistFilled": 0,
                    "roomno": "KNB 132"
                }
            }
    }





-->