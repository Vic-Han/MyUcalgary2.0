<!-- This is the SchedBuilder component that toggles when the route is set to schedule -->
<template>
    <div class = "flex flex-row w-96">
        <div class = "w-96 flex flex-col">
            <img src = "@/assets/unilogo.png " class = "w-10/12">
            <div class = "flex flex-row w-10/12 relative left-5">
                <input type = "text" v-model="courseSearchTerm" class = "w-40 border border-black-100">
                <div @click = "searchResults"> Search</div>
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
import SchedPreview from '@/components/SchedPreview.vue';
    export default{
        name : 'SchedBuilder',
        components: {
            SchedPreview,
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
            const backendPayload = {
                
                    "allCourses" : [
                        {
                            "name": "SENG 401",
                            "title": "Software Architecture",
                            "desc" : "Software architectures and design for non-functional software properties. Introduction to program comprehension skills including analysis of existing architectures.",
                            "prereq": ["SENG 300"],
                            "prereqfilled" : true,
                            "lectures": [
                                {
                                    "name": "L1",
                                    "days": "TTH",
                                    "start": 8,
                                    "end": 9.25,
                                    "Prof": "Ronnie",
                                    "totalSeats": 100,
                                    "seatsFilled": 50,
                                    "totalWaitlist": 10,
                                    "waitlistFilled": 0,
                                    "roomno": "SA 104"
                                },
                                {
                                    "name": "L2",
                                    "days": "TTH",
                                    "start": 9.5,
                                    "end": 10.75,
                                    "Prof": "Ronnie",
                                    "totalSeats": 100,
                                    "seatsFilled": 50,
                                    "totalWaitlist": 10,
                                    "waitlistFilled": 0,
                                    "roomno": "SA 104"
                                }
                            ],
                            "tutorials": [
                                {
                                    "name": "T1",
                                    "days": "W",
                                    "start": 8,
                                    "end": 10,
                                    "TA": "Lets not implement this :)",
                                    "totalSeats": 100,
                                    "seatsFilled": 50,
                                    "totalWaitlist": 10,
                                    "waitlistFilled": 0,
                                    "roomno": "ENA 301"
                                },
                                {
                                    "name": "T2",
                                    "days": "W",
                                    "start": 16,
                                    "end": 18,
                                    "TA": "Lets not implement this :)",
                                    "totalSeats": 100,
                                    "seatsFilled": 50,
                                    "totalWaitlist": 10,
                                    "waitlistFilled": 0,
                                    "roomno": "ENA 301"
                                }
                            ]
                        },
                        {
                            "name": "SENG 550",
                            "title": "Big Data",
                            "desc" : "Big Data, Machine Learnin, and more buzz words",
                            "prereq": ["SENG 300, CPSC 331"],
                            "prereqfilled" : "false- note that the student might be enrolled CPSC 331 in previous semester which would make them eligible for this course",
                            "lectures": [
                                {
                                    "name": "L1",
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
                                {
                                    "name": "L2",
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
                            ],
                            "tutorials": [
                                {
                                    "name": "T1",
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
                                {
                                    "name": "T2",
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
                            ]
                        }
                    ],
                    "current Sched including the shopping cart":{
                        "SENG 401":{
                            "Lecture" : {
                                "days" : "MWF",
                                "start" : 14,
                                "end" : 15,
                                "roomno": "KNB 132",
                                "LectureNO" : 1
                            },
                            "Tutorial":{
                                "days" : "TTH",
                                "start" : 14,
                                "end" : 16,
                                "roomno": "KNB 132",
                                "TutorialNO" : 1
                            }
                        },
                        "CPSC 559":{
                            "Lecture" : {
                                "days" : "MWF",
                                "start" : 14,
                                "end" : 15.25,
                                "roomno": "ENA 101",
                                "LectureNO" : 2
                            },
                            "Tutorial":{
                                "days" : "TTH",
                                "start" : 14,
                                "end" : 15,
                                "roomno": "KNB 132",
                                "TutorialNO" : 1
                            }
                        },
                        "ECON 373":{
                            "Lecture" : {
                                "days" : "MWF",
                                "start" : 14,
                                "end" : 15,
                                "roomno": "KNB 132",
                                "LecNO" : 1
                            },
                            "Tutorial":{
                                "days" : "TTH",
                                "start" : 14,
                                "end" : 15,
                                "roomno": "KNB 132",
                                "LecNO" : 1
                            }

                        }
                    },
                    "academic Requirements":{
                        "CPSC at the 500 level or above": [
                            "CPSC 559"
                        ],
                        "CPSC at the 400 level or above": [
                            "CPSC 457",
                            "CPSC 471",
                            "CPSC 559"
                        ],
                        "CPSC at the 300 level or above": [
                            "CPSC 331",
                            "CPSC 313",
                            "CPSC 355",
                            "CPSC 359",
                            "CPSC 371",
                            "CPSC 379",
                            "CPSC 457",
                            "CPSC 471",
                            "CPSC 481",
                            "CPSC 559"
                        ],
                        "CSPC 413": "CPSC 413"

                    }
                

            }
            this.allInfo = backendPayload
            this.courses = this.allInfo['allCourses']
            this.degreeRequirements = this.allInfo['academic Requirements']

            
        },
        methods:{
            searchResults(){

            },
            addCourseToOptions(course){
                this.selectedCourses.push(course)
            }
        }
    }
</script>