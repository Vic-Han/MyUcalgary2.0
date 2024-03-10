<template>
    <div class = "w-fit rounded-xl mt-5 flex flex-col py-4 z-10" v-bind:class="courseColor()" @click="toggleDropdown" >
        <div class = "flex flex-row px-3 py-2 text-base" > 
            <div class = "mx-2">{{ course.name }}</div>
            <div class = "mx-2"> {{ course.title }}</div>
            <div class = "bg-red-100 h-4 w-4" @click="toggleOff" v-if="included"></div>
            <div class="bg-green-100 h-4 w-4" @click="toggleOn" v-else ></div>
            <svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 -960 960 960" width="24" @click="removeCourse">
                <path d="M280-120q-33 0-56.5-23.5T200-200v-520h-40v-80h200v-40h240v40h200v80h-40v520q0 33-23.5 56.5T680-120H280Zm80-160h80v-360h-80v360Zm160 0h80v-360h-80v360Z"/>
            </svg>       

        </div>
       <div class = "flex flex-row">
            <div class="mx-1"> {{ lecture.name }} </div>
            <div class="mx-1"> Selected lecture time </div>
            <div class="mx-1">SA 104</div>
       </div>
        <div class = "flex flex-row">
            <div class="mx-1">Lab number</div>
            <div class="mx-1"> Selected lab time </div>
            <div class="mx-1"> Room of tut/lab</div>
        </div>
        <div class = "flex flex-row">
            <div class="mx-1">Session</div>
            <div class="mx-1"> Regular Academic </div>
            <div class="mx-1"> Instructor</div>
        </div>

    </div>
    <div class = "bg-white-100 flex flex-col z-0" v-if="dropDownVisible" :class="animation()"> 
        <div class = "flex flex-row">
            <div> Try all classes </div>
            <input type = "checkbox" class = "mx-1" v-model="allClasses">    
        </div>
        <div v-if="!allClasses" class = "flex flex-row flex-wrap w-80"> 
            <div v-for="(section,index) in sections" :key="index" class = "mx-1">
                <div>{{section[0] + " " + section[1]}}</div>
                <input type = "checkbox" v-model="section.selected"> 
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
                <div class="mx-1"> Current/Max Seats</div>
            </div>
            <div class = "flex flex-row">
                <div class = "mx-1"> Waitlist</div>
                <div class="mx-1"> Current/Max Waitlist</div>
            </div>
        </div>
        <div class = "flex flex-col">
            <div class = "flex flex-row">
                <div class = "mx-1"> Lab Number</div>
                <div class="mx-1"> Lab ID</div>
                <div class="mx-1"> University of Calgary</div>
            </div>
            <div class = "flex flex-row">
                <div class = "mx-1"> Seats</div>
                <div class="mx-1"> Current/Max Seats</div>
            </div>
            <div class = "flex flex-row">
                <div class = "mx-1"> Waitlist</div>
                <div class="mx-1"> Current/Max Waitlist</div>
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
            selected: {
                type: Number,
                required: true
            }
        },
        data: () => {
            return {
                dropDownOpen: true,
                dropDownFadeUp: false,
                dropDownFadeDown: false,
                dropDownVisible: false,
                included: true,
                sections: [],
                allClasses: true,
                lecture: null,
                tut: null,
            }
        },
        created()  {
            this.sections = this.course.combinations
            const lecID = this.course.combinations[this.selected][0]
            for(let i = 0; i < this.course.lectures.length; i++){
                if(this.course.lectures[i].name === lecID){
                    this.lecture = this.course.lectures[i]
                    break
                }
            }
            console.log(this.lecture)
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
            removeCourse(){
                this.$emit('removecourse', this.number)
            },
            toggleOn(e){
                this.included = true
                e.stopPropagation()
            },
            toggleOff(e){
                this.included = false
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
            }
        }
    }
</script>

<style>
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
    height: 168px;
  }
}
@keyframes fade-up{
    0% {
    height: 168px;
  }
  100% {
    height: 0;
  }
}
</style>