<template>
    <div class = "sub-component">
        This should be a preview of your sched know what I'm sayin
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
        }
    }
</script>