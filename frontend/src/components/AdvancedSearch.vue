<template>
    <div class = "fixed w-screen h-screen z-30 opacity-50 bg-black-100"></div>
    <div class = "fixed w-96 h-96 z-40 bg-white-100 rounded-xl">
        <div @click="closeAdvancedSearch"> Close </div>
    </div>
</template>  

<script>
    export default{
        name : 'AdvancedSearch',
        data : () => {
            return {
            
            }
        },
        methods: {
            closeAdvancedSearch(){
                this.$emit('close')
            },
            appluAdvancedSearch(){
                this.$emit('applyadvancedsearch')
            }
        }
    }
</script>