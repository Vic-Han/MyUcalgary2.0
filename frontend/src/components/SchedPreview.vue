<template>
    <div class="flex flex-col">
        <div class="flex flex-row">
            <div class="w-12"></div>
            <div class="w-40 px-1 box-content bg-grey-200 text-white-100  rounded-tl-xl">Monday</div>
            <div class="w-40 px-1 box-content border-x bg-grey-200 text-white-100 ">Tuesday</div>
            <div class="w-40 px-1 box-content bg-grey-200 text-white-100 ">Wednesday</div>
            <div class="w-40 px-1 box-content border-x bg-grey-200 text-white-100 ">Thursday</div>
            <div class="w-40 px-1 box-content bg-grey-200 text-white-100  rounded-tr-xl">Friday</div>
        </div>
        <div v-for="time in times" class="flex flex-row" :key="time">
            <div class="w-12 text-grey-200 text-right pr-1 h-10">{{ time }}</div>
            <div class="flex flex-col">
                <div class="h-5 w-40 px-1 box-content bg-white-200 border-b border-grey-100"></div>
                <div v-if="time == '7pm'" class="h-5 w-40 px-1 box-content bg-white-200 rounded-bl-xl"></div>
                <div v-else class="h-5 w-40 px-1 box-content bg-white-200 border-b border-grey-200"></div>
            </div>
            <div class="flex flex-col border-x border-grey-200">
                <div class="h-5 w-40 px-1 box-content bg-white-200 border-b border-grey-100"></div>
                <div v-if="time == '7pm'" class="h-5 w-40 px-1 box-content bg-white-200"></div>
                <div v-else class="h-5 w-40 px-1 box-content bg-white-200 border-b border-grey-200"></div>
            </div>
            <div class="flex flex-col">
                <div class="h-5 w-40 px-1 box-content bg-white-200 border-b border-grey-100"></div>
                <div v-if="time == '7pm'" class="h-5 w-40 px-1 box-content bg-white-200"></div>
                <div v-else class="h-5 w-40 px-1 box-content bg-white-200 border-b border-grey-200"></div>
            </div>
            <div class="flex flex-col border-x border-grey-200">
                <div class="h-5 w-40 px-1 box-content bg-white-200 border-b border-grey-100"></div>
                <div v-if="time == '7pm'" class="h-5 w-40 px-1 box-content bg-white-200"></div>
                <div v-else class="h-5 w-40 px-1 box-content bg-white-200 border-b border-grey-200"></div>
            </div>
            <div class="flex flex-col">
                <div class="h-5 w-40 px-1 box-content bg-white-200 border-b border-grey-100"></div>
                <div v-if="time == '7pm'" class="h-5 w-40 px-1 box-content bg-white-200 rounded-br-xl"></div>
                <div v-else class="h-5 w-40 px-1 box-content bg-white-200 border-b border-grey-200"></div>
            </div>
        </div>
        
        <div class = "absolute w-sched" v-for="(section,index) in schedule" :key="index">
            <div v-for="(day,dayNo) in section.Lecture.days" 
            :key="dayNo" :class="classStyles(day,section.Lecture.start,section.Lecture.end,index)">
            {{ section.courseCode + ' ' + section.Lecture.LectureNO }}
            </div>
            <div class = "absolute w-sched" v-if="section.Tutorial">
                <div v-for="(day,dayNo) in section.Tutorial.days" :key ="dayNo" 
                :class="classStyles(day,section.Tutorial.start,section.Tutorial.end,index)">
                    {{ section.courseCode + ' ' + section.Tutorial.TutorialNO }}
                </div>
        </div>
        
        </div>
        
        
    </div>
</template>

<script>
const leftPos = {
    'M': 'left-monday',
    'T': 'left-tuesday',
    'W': 'left-wednesday',
    'R': 'left-thursday',
    'F': 'left-friday'
}
const topPos = {
    8: 'top-0',
    8.25: 'top-10',
    9: 'top-10',
    10: 'top-20',
    11: 'top-32',
    12: 'top-40',
    13: 'top-52',
    14: 'top-60',
    15: 'top-80',
    16: 'top-80',
    17: 'top-80',
    18: 'top-96',
    19: 'top-96'
}
const height = {
    1: 'h-5',
    1.25: 'h-10',
    2: 'h-20',
}
const classColor= {
    0: 'bg-course-100',
    1: 'bg-course-200',
    2: 'bg-course-300',
    3: 'bg-course-400',
    4: 'bg-course-500',
    5: 'bg-course-600',
    6: 'bg-course-700',
    7: 'bg-course-800',
    8: 'bg-course-900',
    9: 'bg-course-1000'
}
    export default {
        name: 'SchedPreview',
        props: {
            schedule: {
                type: Array,
                required: true
            }
        },
        created() {
            console.log(this.schedule)
        },
        methods: {
            classStyles(day,starttime,endtime,classno){
                let style = 'absolute ';
                style += leftPos[day] + ' ';
                style += 'w-40 box-content p-2';
                style += topPos[starttime] + ' ';
                style += height[endtime-starttime] + ' ';
                console.log(classno)
                style += classColor[classno] + ' ';
                console.log(day)
                return style;
            }
        },
        data: () =>{
            return{
                times: [
                    "8am",
                    "9am",
                    "10am",
                    "11am",
                    "12pm",
                    "1pm",
                    "2pm",
                    "3pm",
                    "4pm",
                    "5pm",
                    "6pm",
                    "7pm",
                ]
            }
        }
    }
</script>
<!-- 
    Really quick hotfix should be removed later
-->
<style>
    .w-sched{
        width: 55.75rem;
    }
    .left-monday{
        left: 1rem;
    }
    .left-tuesday{
        left: 15rem;
    }
    .left-wednesday{
        left: 30rem;
    }
    .left-thursday{
        left: 45rem;
    }
    .left-friday{
        left: 60rem;
    }
    .top-800{

    }
    .top-900{

    }
    .top-1000{

    }
    .top-1100{

    }
</style>