<template>
    <div class = "bg-white-100 w-96 rounded-t-xl mt-5 flex flex-row py-4" :class="roundedBottom()" @click="toggleDropdown">
        <div class = "flex flex-col w-20 h-16 px-3 py-2 text-base" v-bind:class="courseColor()"> {{ course.name }}</div>
        <div class = "flex flex-col w-52 h-16 align-middle text-lg text-left px-2">
            <div>{{ course.title }}</div>
            <div> {{  }} </div> 
            
        </div>
        <div class = "flex flex-col w-8">
            <div v-if="course.included" @click="removeCourseFromCart"> - </div>
            <div v-else @click="addCourseToCart"> + </div>
        </div>
    </div>
    <div class = "bg-white-200 w-96 rounded-b-lg" v-if="dropDownVisible" :class="animation()">
        <div class="text-xs text-left" > Description: {{ course.desc }}</div>
        <div class = "text-xs text-left" > Prerequisites: {{ course.prereq }}</div>
        <div class = "text-xs text-left"> AntiRequisites: {{ course.antireq }}:)</div>
        <div class = "text-sm text-left"> Course attributes: {{ course.attributes }} :)</div>
    </div>

</template>  

<script>
const animationTime = 300
    export default{
        name : 'CoursePreview',
        props: {
            course: {
                type: Object,
                requuired: true
            },
            number:{
                type: Number,
                required: true
            }
        },
        emits: ['addcourse', 'removecourse'],
        data:() =>{
            return {
                dropDownOpen: true,
                dropDownVisible: false,
                dropDownFadeDown: false,
                dropDownFadeUp: false
            }
        },
        methods: {
            addCourseToCart(e){
                this.$emit('addcourse', this.course.name)
                e.stopPropagation()
            },
            removeCourseFromCart(e){
                this.$emit('removecourse', this.course.name)
                e.stopPropagation()
            },
            roundedBottom(){
                if(!this.dropDownVisible){
                    return ' rounded-b-xl'
                }
                else{
                    return ''
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
           
            animation(){
                if(this.dropDownFadeDown){
                    return ' fade-down'
                }
                else if(this.dropDownFadeUp){
                    return ' fade-up'
                }
                else{
                    return ' h-40'
                }
            }
        },
        computed: {
            
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
    height: 160px;
  }
}
@keyframes fade-up{
    0% {
    height: 160px;
  }
  100% {
    height: 0;
  }
}
</style>