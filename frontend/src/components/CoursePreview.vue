<template>
    <div>
        {{ course.name }}
    </div>
</template>  

<script>
    export default{
        name : 'CoursePreview',
        props: {
            course: {
                type: Object,
                requuired: true
            }
        }
        
    }
</script>