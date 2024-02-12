<template>
    <div class="flex flex-col w-1/5">
        <div class = "text-green-500 text-3xl"> Hi guys, I styled the navabr with Tailwind!!</div>
        <router-link to = "/dashboard" class = "btn"> Go to dashboard </router-link>
        <router-link to = "/academics"  class = "btn"> Go to academics </router-link>
        <router-link to = "/misc" class = "btn" > Go to misc </router-link>
        <router-link to = "/application" class = "btn"> Go to Application </router-link>
    </div>

</template>

<script>
export default {
  name: 'AppNavbar'
}
</script>
