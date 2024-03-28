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
            <div class="w-12 text-grey-200 text-right pr-1 h-10">{{ time }}</div>
        </div>
        
        <div class = "absolute w-sched" v-for="(section,index) in schedule" :key="index">
            <div v-for="(day,dayNo) in section.Lecture.days" 
            :key="dayNo" :class="classStyles(day,section.Lecture.start,section.Lecture.end,index)">
            {{ section.courseCode + ' ' + section.Lecture.LectureNO  }}
            </div>
            <div class = "absolute w-sched" v-if="section.Tutorial">
                <div v-for="(day,dayNo) in section.Tutorial.days" :key ="dayNo" 
                :class="classStyles(day,section.Tutorial.start,section.Tutorial.end,index)" >
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
    8: 'top-800',
    9: 'top-900',
    9.5: 'top-950',
    10: 'top-1000',
    10.5 : 'top-1050',
    11: 'top-1100',
    11.5: 'top-1150',
    12: 'top-1200',
    12.5: 'top-1250',
    13: 'top-1300',
    13.5: 'top-1350',
    14: 'top-1400',
    14.5: 'top-1450',
    15: 'top-1500',
    15.5 : 'top-1550',
    16: 'top-1600',
    16.5: 'top-1650',
    17: 'top-1700',
    17.5: 'top-1750',
    18: 'top-1800',
    18.5: 'top-1850',
    19: 'top-1900'
}
const height = {
    0.83: 'height-50',
    1.25: 'height-115',
    1.83: 'height-150',
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
            //console.log(this.schedule)
        },
        methods: {
            classStyles(day,starttime,endtime,classno){
                let style = 'absolute ';
                style += leftPos[day] + ' ';
                style += 'w-36 box-content p-2 rounded-sm opacity-80 z-30 '
                style += topPos[starttime] + ' '
                const time = endtime-starttime;
                style += height[Number(time.toFixed(2))] + ' '
                style += classColor[classno%10] + ' '

                // // Hi Callum I was so closeee to figuring this out but whatever. Comment out the 3 lines below
                // style += ' hover:after:bg-white-100 hover:after:text-black-100 hover:after:rounded-lg hover:after:shadow-lg' 
                // + ' hover:after:p-4 hover:after:absolute hover:after:translate-x-5 hover:after:-translate-y-6 '
                // style += ` after:content-['${roomno}'] after:hidden hover:after:block`
                return style;
            },
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
                ],
                courses : []
            }
        },
    }
</script>

<style>
    .w-sched{
        width: 55.75rem;
    }
    .left-monday{
        left: 3.18rem;
    }
    .left-tuesday{
        left: 13.71rem;
    }
    .left-wednesday{
        left: 24.26rem;
    }
    .left-thursday{
        left: 34.8rem;
    }
    .left-friday{
        left: 45.4rem;
    }
    .top-800{
        top: 1.5rem;
    }
    .top-900{
        top: 4.06rem;
    }
    .top-950{
        top: 5.4rem;
    }
    .top-1000{
        top: 6.72rem;
    }
    .top-1100{
        top: 9.98rem;
    }
    .top-1200{
        top: 11.76rem;
    }
    .top-1250{
        top: 13.3rem;
    }
    .top-1300{
        top: 14.6rem;
    }
    .top-1350{
        top: 15.9rem;
    }
    .top-1400{
        top: 16.95rem;
    }
    .top-1450{
        top: 18.1rem;
    }
    .top-1500{
        top: 19.3rem;
    }
    .top-1550{
        top: 20.8rem;
    }
    .top-1600{
        top: 22.05rem;
    }
    .top-1650{
        top: 23.3rem;
    }
    .top-1700{
        top: 24.2rem;
    }
    .top-1750{
        top: 25.2rem;
    }
    .top-1800{
        top: 26.1rem;
    }
    .top-1850{
        top: 27.1rem;
    }
    .top-1900{
        top: 28rem;
    }
    .height-50{
        height: 1.15rem;
    }
    .height-115{
        height: 2.25rem;
    }
    .height-150{
        height: 3.6rem;
    }
</style>