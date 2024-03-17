<template>
    <div class = "component">
        This is the ApplicationSummary Component
    </div>
    <div>
        {{ application }}
    </div>
</template>

<script>
    export default{
        name : 'ApplicationSummary',
        props: {
            application: {
                type: Object,
                required: true
            }
        }
    }
</script>