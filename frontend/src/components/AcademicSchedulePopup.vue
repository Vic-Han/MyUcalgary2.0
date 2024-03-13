<template>
   <div class = "bg-black-100 fixed w-screen h-screen opacity-40 z-30"></div>
   <div class = "fixed w-1/3 h-96 z-40 bg-white-100 rounded-xl left-1/2 -translate-x-1/2 top-1/3 -translate-y-1/2">
        <div @click="closePopup"> Close</div>
   </div>
</template>  

<script>
    export default{
        name : 'AcademicSchedulePopup',
        props:{
            requirements: {
                type: Object,
                required: true
            }
        },
        methods: {
            closePopup() {
                this.$emit('close')
            },
            selectCourse(course){
                this.$emit('selectcourse',course)
            }
        },
        created(){
            // delete the whole "created" method afterwards
            console.log(this.requirements)

        }
    }
</script>