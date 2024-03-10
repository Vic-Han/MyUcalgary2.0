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
    </div>
</template>

<script>
    export default {
        name: 'SchedPreview',
        props: {
            schedule: {
                type: Object,
                required: true
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