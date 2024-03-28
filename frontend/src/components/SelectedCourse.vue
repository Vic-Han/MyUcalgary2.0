<template>
    
    <div class="w-full rounded-t-xl mt-5 flex flex-col py-2 z-10" v-bind:class="courseColor() + roundedBottom()" @click="toggleDropdown" >
        <div class="flex flex-row px-3 py-2 text-base" > 
            <div class="w-1/4 mx-2 font-semibold text-xl">{{ course.name }}</div>
            <div class="w-3/5 mx-2 font-semibold text-left"> {{ course.title }}</div>
            <div class="flex flex-row">
                <div class="pr-1" @click="toggleOn" v-if="course.included != 'sched' ">
                    <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 fill-grey-200 hover:fill-red-100" viewBox="0 -960 960 960">
                        <path d="M792-56 624-222q-35 11-70.5 16.5T480-200q-151 0-269-83.5T40-500q21-53 53-98.5t73-81.5L56-792l56-56 736 736-56 56ZM480-320q11 0 20.5-1t20.5-4L305-541q-3 11-4 20.5t-1 20.5q0 75 52.5 127.5T480-320Zm292 18L645-428q7-17 11-34.5t4-37.5q0-75-52.5-127.5T480-680q-20 0-37.5 4T408-664L306-766q41-17 84-25.5t90-8.5q151 0 269 83.5T920-500q-23 59-60.5 109.5T772-302ZM587-486 467-606q28-5 51.5 4.5T559-574q17 18 24.5 41.5T587-486Z"/>
                    </svg>
                </div>
                <div class="pr-1" @click="toggleOff" v-else-if="!course.enrolled">
                    <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 fill-grey-200 hover:fill-red-100" viewBox="0 -960 960 960">
                        <path d="M480-320q75 0 127.5-52.5T660-500q0-75-52.5-127.5T480-680q-75 0-127.5 52.5T300-500q0 75 52.5 127.5T480-320Zm0-72q-45 0-76.5-31.5T372-500q0-45 31.5-76.5T480-608q45 0 76.5 31.5T588-500q0 45-31.5 76.5T480-392Zm0 192q-146 0-266-81.5T40-500q54-137 174-218.5T480-800q146 0 266 81.5T920-500q-54 137-174 218.5T480-200Z"/>
                    </svg>
                </div>
                <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 fill-grey-200 hover:fill-red-100" viewBox="0 -960 960 960" @click="removeCourse">
                    <path d="M280-120q-33 0-56.5-23.5T200-200v-520h-40v-80h200v-40h240v40h200v80h-40v520q0 33-23.5 56.5T680-120H280Zm80-160h80v-360h-80v360Zm160 0h80v-360h-80v360Z"/>
                </svg>       
            </div>
        </div>
       <div class="flex flex-row pl-2">
            <div class="mx-1"> {{ lecture.name }} </div>
            <div class="mx-1"> {{ convertLectureTime()}} </div>
            <div class="mx-1">{{lecture.roomno}}</div>
            <div class="ml-2 h-5 w-16 border-2 border-white-100 text-xs text-white-100 bg-blue-500 rounded-xl drop-shadow-lg" v-if="course.enrolled">Enrolled</div>
       </div>
        <div class="flex flex-row pl-2" v-if="tut">
            <div class="mx-1">{{tut.name}}</div>
            <div class="mx-1"> {{convertTutorialTime()  }}</div>
            <div class="mx-1"> {{ tut.roomno }}</div>
        </div>
        <div class="flex flex-row pl-2">
            <div class="mx-1">Session</div>
            <div class="mx-1"> Regular Academic </div>
            <div class="mx-1"> {{lecture.Prof}}</div>
        </div>

    </div>
    <div class="bg-white-200 flex flex-col z-0 w-full rounded-b-xl shadow-md" v-if="dropDownVisible" :class="animation()"> 
        <div class="flex flex-row pl-2">
            <div> Try all classes </div>
            <input type="checkbox" class="mx-1 accent-red-100" v-model="allClasses">    
        </div>
        <div v-if="!allClasses" class="flex flex-row flex-wrap w-80 pl-2 divide-x-2 divide-dashed divide-grey-100"> 
            <div v-for="(section,index) in sections" :key="index" class="mx-1">
                <div class="flex flex-row pl-1">
                    <input type="checkbox" v-if="course.selectedIndices[index]" class="accent-red-100" @click="removeSection(index)" checked>
                    <input type="checkbox" v-else @click="addSection(index)">
                    <div class="pl-1">{{section[0] + (tut ? " - " + section[1] : '')}}</div>
                </div>
            </div>
        </div>
        <div class="flex flex-col pl-2">
            <div class="flex flex-row">
                <div class="mx-1"> {{lecture.name}}</div>
                <div class="mx-1"> University of Calgary</div>
            </div>
            <div class="flex flex-row">
                <div class="mx-1"> Seats</div>
                <div class="mx-1"> {{ lecture.seatsFilled + '/' + lecture.totalSeats}} Seats</div>
            </div>
            <div class="flex flex-row">
                <div class="mx-1"> Waitlist</div>
                <div class="mx-1"> {{lecture.waitlistFilled + '/' + lecture.totalWaitlist}} Waitlist</div>
            </div>
        </div>
        <div v-if="tut" class="flex flex-col pl-2">
            <div class="flex flex-row">
                <div class="mx-1"> {{tut.name}}</div>
                <div class="mx-1"> University of Calgary</div>
            </div>
            <div class="flex flex-row">
                <div class="mx-1"> Seats</div>
                <div class="mx-1"> {{ tut.seatsFilled + '/' + tut.totalSeats}} Seats</div>
            </div>
            <div class="flex flex-row">
                <div class="mx-1"> Waitlist</div>
                <div class="mx-1"> {{ tut.waitlistFilled + '/' + tut.totalWaitlist}} Waitlist</div>
            </div>
        </div>

    </div>
</template>  

<script>
const animationTime = 300;
    export default{
        name : 'SelectedCourse',
        props: {
            course: {
                type: Object,
                requuired: true
            },
            number:{
                type: Number,
                required: true
            },
        },
        emits: ['removecourse', 'select', 'unselect', 'addsection', 'removesection'],
        data: () => {
            return {
                dropDownOpen: true,
                dropDownFadeUp: false,
                dropDownFadeDown: false,
                dropDownVisible: false,
                sections: [],
                allClasses: true,
                lecture: null,
                tut: null,
                dropCoursePopup: false
            }
        },
        created()  {
            this.sections = this.course.combinations
            const lecID = this.course.combinations[this.course.selected][0]
            for(let i = 0; i < this.course.lectures.length; i++){
                if(this.course.lectures[i].name === lecID){
                    this.lecture = this.course.lectures[i]
                    break
                }
            }
            if(this.course.combinations[this.course.selected].length > 1){
                const tutID = this.course.combinations[this.course.selected][1]
                for(let i = 0; i < this.course.tutorials.length; i++){
                    if(this.course.tutorials[i].name === tutID){
                        this.tut = this.course.tutorials[i]
                        break
                    }
                }
            }
            else
            {
                this.tut = null
            }
            if(this.course.enrolled){
                this.allClasses = false
            }
        },
        watch:{
            course:{
                handler(){
                    const lecID = this.course.combinations[this.course.selected][0]
                    for(let i = 0; i < this.course.lectures.length; i++){
                        if(this.course.lectures[i].name === lecID){
                            this.lecture = this.course.lectures[i]
                            break
                        }
                    }
                    if(this.course.combinations[this.course.selected].length > 1){
                        const tutID = this.course.combinations[this.course.selected][1]
                        for(let i = 0; i < this.course.tutorials.length; i++){
                            if(this.course.tutorials[i].name === tutID){
                                this.tut = this.course.tutorials[i]
                                break
                            }
                        }
                    }
                    else{
                        this.tut = null
                    }
                },
                deep: true
            },
            allClasses(oldVal,newVal){
                if(newVal){
                    this.$emit('selectset', this.course.name, this.course.selectedIndices)
                }
                else if(oldVal){
                    this.$emit('selectall', this.course.name)
                }
            }
        },
        methods:{
            courseColor(){
                if(this.number === 0){
                    return 'bg-course-100'
                }
                else if(this.number == 1){
                    return 'bg-course-200'
                }
                else if(this.number === 2){
                    return 'bg-course-300'
                }
                else if(this.number == 3){
                    return 'bg-course-400'
                }
                else if(this.number === 4){
                    return 'bg-course-500'
                }
                else if(this.number == 5){
                    return 'bg-course-600'
                }
                else if(this.number === 6){
                    return 'bg-course-700'
                }
                else if(this.number == 7){
                    return 'bg-course-800'
                }
                else{
                    return 'bg-course-900'
                }
            },
            roundedBottom(){
                if(!this.dropDownVisible){
                    return ' shadow-md rounded-b-xl '
                }
                else{
                    return ' '
                }
            },
            toggleDropdown(){
                
                if(!this.dropDownOpen){
                    return
                }

                this.dropDownOpen = false
                
                if(this.dropDownVisible){
                    this.dropDownFadeUp = true
                    setTimeout(() => {
                        this.dropDownVisible = false
                        this.dropDownFadeUp = false
                        this.dropDownOpen = true
                    }, animationTime)
                }
                
                else{
                    this.dropDownVisible = true
                    this.dropDownFadeDown = true
                    setTimeout(() => {
                        this.dropDownFadeDown = false
                        this.dropDownOpen = true
                    }, animationTime)
                }
            },
            removeCourse(e){
                if(this.course.included){
                    this.$emit('removecourse', this.course.name)
                }
                else{
                    this.$emit('removecourse', this.course.name)
                }
                e.stopPropagation()
            },
            
            toggleOn(e){
                this.$emit('select', this.course.name)
                e.stopPropagation()
            },
            toggleOff(e){
                this.$emit('unselect', this.course.name)
                e.stopPropagation()
            },
            animation(){
                if(this.dropDownFadeDown){
                    return 'fade-down'
                }
                else if(this.dropDownFadeUp){
                    return 'fade-up'
                }
                else if(!this.allClasses){
                    return ' h-auto'
                }
                else{
                    return ' h-52'
                }
            },
            convertLectureTime(){
                let time = ""
                if(this.lecture.days.includes('M')){
                    time += "Mon "
                }
                if(this.lecture.days.includes('T')){
                    time += "Tue "
                }
                if(this.lecture.days.includes('W')){
                    time += "Wed "
                }
                if(this.lecture.days.includes('R')){
                    time += "Thu "
                }
                if(this.lecture.days.includes('F')){
                    time += "Fri "
                }
                time += this.convertTime(this.lecture.start) + " - " + this.convertTime(this.lecture.end)
                return time
            },
            convertTutorialTime(){
                let time = ""
                if(this.tut.days.includes('M')){
                    time += "Mon "
                }
                if(this.tut.days.includes('T')){
                    time += "Tue "
                }
                if(this.tut.days.includes('W')){
                    time += "Wed "
                }
                if(this.tut.days.includes('R')){
                    time += "Thu "
                }
                if(this.tut.days.includes('F')){
                    time += "Fri "
                }
                time += this.convertTime(this.tut.start) + " - " + this.convertTime(this.tut.end)
                return time
            },
            convertTime(time){
                const hours = Math.floor(time);
                const minutes = Math.round((time - hours) * 60);
                const period = hours >= 12 ? 'pm' : 'am';
                const formattedHours = hours % 12 === 0 ? 12 : hours % 12;
                const formattedMinutes = minutes < 10 ? `0${minutes}` : minutes;
                return `${formattedHours}:${formattedMinutes}${period}`;
            },
            addSection(index){
                
                this.$emit('addsection', this.course.name, index)
            },
            removeSection(index){
                for(let i = 0; i < this.course.selectedIndices.length; i++){
                    if(this.course.selectedIndices[i] && i !== index){
                        console.log('removing' , i, index)
                        this.$emit('removesection', this.course.name, index)
                        return
                    }
                }
            }
        }
    }
</script>

<style scoped>
.fade-down{
    overflow-y: hidden;
    animation: fade-down 0.3s;
}
.fade-up{
    overflow-y: hidden;
    animation: fade-up 0.3s;
}
@keyframes fade-down{
    0% {
    height: 0;
  }
  100% {
    height: 208px;
  }
}
@keyframes fade-up{
    0% {
    height: 208px;
  }
  100% {
    height: 0;
  }
}
</style>