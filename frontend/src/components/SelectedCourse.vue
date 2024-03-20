<template>
    <div class = "w-full rounded-t-xl mt-5 flex flex-col py-4 z-10" v-bind:class="courseColor() + roundedBottom()" @click="toggleDropdown" >
        <div class = "flex flex-row px-3 py-2 text-base" > 
            <div class = "w-20 mx-2">{{ course.name }}</div>
            <div class = "w-20 mx-2"> {{ course.title }}</div>
            <div class = "bg-red-100 h-4 w-4" @click="toggleOn" v-if="course.included != 'sched' "></div>
            <div class="bg-green-100 h-4 w-4" @click="toggleOff" v-else ></div>
            <svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 -960 960 960" width="24" @click="removeCourse">
                <path d="M280-120q-33 0-56.5-23.5T200-200v-520h-40v-80h200v-40h240v40h200v80h-40v520q0 33-23.5 56.5T680-120H280Zm80-160h80v-360h-80v360Zm160 0h80v-360h-80v360Z"/>
            </svg>       

        </div>
       <div class = "flex flex-row">
            <div class="mx-1"> {{ lecture.name }} </div>
            <div class="mx-1"> {{ convertLectureTime()}} </div>
            <div class="mx-1">{{lecture.roomno}}</div>
       </div>
        <div class = "flex flex-row">
            <div class="mx-1">{{tut.name}}</div>
            <div class="mx-1"> {{convertTutorialTime()  }}</div>
            <div class="mx-1"> {{ tut.roomno }}</div>
        </div>
        <div class = "flex flex-row">
            <div class="mx-1">Session</div>
            <div class="mx-1"> Regular Academic </div>
            <div class="mx-1"> {{lecture.Prof}}</div>
        </div>

    </div>
    <div class = "bg-white-100 flex flex-col z-0 h-52 w-full rounded-b-xl " v-if="dropDownVisible" :class="animation()"> 
        <div class = "flex flex-row">
            <div> Try all classes </div>
            <input type = "checkbox" class = "mx-1" v-model="allClasses">    
        </div>
        <div v-if="!allClasses" class = "flex flex-row flex-wrap w-80"> 
            <div v-for="(section,index) in sections" :key="index" class = "mx-1">
                <div>{{section[0] + " " + section[1]}}</div>
                {{ course.selectedIndices[index] }}
                <div class="w-4 h-4 bg-green-100" v-if="course.selectedIndices[index]" @click="removeSection(index)"></div>
                <div class="w-4 h-4 bg-red-100" v-else @click="addSection(index)"></div>
            </div>
        </div>
        <div class = "flex flex-col">
            <div class = "flex flex-row">
                <div class = "mx-1"> {{lecture.name}}</div>
                <div class="mx-1"> Lecture ID</div>
                <div class="mx-1"> University of Calgary</div>
            </div>
            <div class = "flex flex-row">
                <div class = "mx-1"> Seats</div>
                <div class="mx-1"> {{ lecture.seatsFilled + '/' + lecture.totalSeats}} Seats</div>
            </div>
            <div class = "flex flex-row">
                <div class = "mx-1"> Waitlist</div>
                <div class="mx-1"> {{lecture.waitlistFilled + '/' + lecture.totalWaitlist}} Waitlist</div>
            </div>
        </div>
        <div class = "flex flex-col">
            <div class = "flex flex-row">
                <div class = "mx-1"> {{tut.name}}</div>
                <div class="mx-1"> Lab ID</div>
                <div class="mx-1"> University of Calgary</div>
            </div>
            <div class = "flex flex-row">
                <div class = "mx-1"> Seats</div>
                <div class="mx-1"> {{ tut.seatsFilled + '/' + tut.totalSeats}} Seats</div>
            </div>
            <div class = "flex flex-row">
                <div class = "mx-1"> Waitlist</div>
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
                },
                deep: true
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
                if(this.dropDownVisible){
                    return ' rounded-b-xl'
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
                else{
                    return ' '
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
                this.$emit('removesection', this.course.name, index)
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