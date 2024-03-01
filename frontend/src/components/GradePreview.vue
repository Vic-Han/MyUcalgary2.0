<template>
    <div class="flex flex-row justify-between">
        <div class="flex flex-col items-center mx-10">
            <div class = "text-2xl font-bold mb-4">Semester GPA</div>
            <div class="rounded-full w-52 h-52 flex items-center justify-center flex-col border-8" :class ="[circleBorder(letter),circleColor(letter)]" >
                <span class="text-4xl font-bold" :class = "[letterColor(letter)]">{{ average }}</span>
                <span class="text-4xl font-bold" :class = "[letterColor(letter)]">{{ letter  }}</span>
            </div>
        </div>
        <div class = "flex flex-col mx-2 justify-between">
            <div v-for="course in courses" :key="course.name"  class="flex flex-row py-1 justify-between">
                <div class = "mx-3 text-lg w-28 text-left"> {{ course.name }}</div>
                <div class = "w-96 mx-0">
                    <div class = "h-8 rounded-lg" :class = "[barColor(course.letter),barWidth(course.letter)]"></div>
                </div>
                
                <div class = " mx-6 pr-2 text-lg w-12 text-center">{{ course.letter }}</div>
            </div> 
        </div>
    </div>
   <div class = "p-2 text-left text-sm">
        <div>{{ term }}</div>
        <div> Level: {{ year }}</div>
        <div> Units Enrolled: {{ unitsEnrolled }}</div>
        <div> Plan: {{ plan }}</div>
        <div> Program: {{ program }}</div>
   </div>
</template>

<script>
    export default{
        name : 'GradePreview',
        props : {
            average :{
                type: Number,
                required: true
            },
            letter:{
                type: String,
                required: true
            },
            courses:{
                type: Array,
                required: true
            },
            term:{
                type: String,
                required: true
            },
            year:{
                type: Number,
                required: true
            },
            unitsEnrolled:{
                type: Number,
                required: true
            },
            plan:{
                type: String,
                required: true
            },
            program:{
                type: String,
                required: true
            }

        },
        methods:{
            barColor(grade){
                if(grade[0] === 'A'){
                    return 'bg-green-500'
                }
                if(grade[0] === 'B'){
                    return 'bg-blue-500'
                }
                if(grade[0] === 'C'){
                    return 'bg-yellow-500'
                }
                if(grade[0] === 'D'){
                    return 'bg-red-500'
                }

            },
            barWidth(grade) {
                if(grade[0] === 'A'){
                    return 'w-96'
                }
                if(grade[0] === 'B'){
                    return 'w-80'
                }
                if(grade[0] === 'C'){
                    return 'w-68'
                }
                if(grade[0] === 'D'){
                    return 'w-60'
                }

            },
            circleColor(letter){
                if(letter[0] === 'A'){
                    return 'bg-green-500'
                }
                if(letter[0] === 'B'){
                    return 'bg-blue-500'
                }
                if(letter[0] === 'C'){
                    return 'bg-yellow-500'
                }
                if(letter[0] === 'D'){
                    return 'bg-red-500'
                }
            },
            circleBorder(letter){
                if(letter[0] === 'A'){
                    return 'border-green-200'
                }
                if(letter[0] === 'B'){
                    return 'border-blue-200'
                }
                if(letter[0] === 'C'){
                    return 'border-yellow-200'
                }
                if(letter[0] === 'D'){
                    return 'border-red-200'
                }
            },
            letterColor(letter){
                if(letter[0] === 'A'){
                    return 'text-green-200'
                }
                if(letter[0] === 'B'){
                    return 'text-blue-200'
                }
                if(letter[0] === 'C'){
                    return 'text-yellow-200'
                }
                if(letter[0] === 'D'){
                    return 'text-red-200'
                }
            }
        },
        created(){
            console.log(this.courses)
        }

}
</script>