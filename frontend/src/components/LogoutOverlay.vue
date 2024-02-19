<template>
    <div class = "fixed w-screen h-screen z-30 bg-black-100 inset-0 opacity-40">
       
    </div>
    <div class = "fixed w-1/2 h-1/3 -translate-y-2/4 -translate-x-2/4 left-1/2 top-1/2 bg-white-100 z-50 opacity-100 rounded-2xl">
        <div class = "mb-20"> You were inactive for too long!!!!!!!!!!! Please log back in</div>
            <router-link to = "/login">Close</router-link>
    </div>
</template>

<script>
    export default{
        name : 'LogoutOverlay'
    }
</script>