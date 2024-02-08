<template>
    <div class = "component">
        This is the navbar
        <router-link to = "/dashboard" class = "btn"> Go to dashboard </router-link>
        <router-link to = "/academics"  class = "btn"> Go to academics </router-link>
        <router-link to = "/misc" class = "btn" > Go to misc </router-link>

    </div>

</template>

<script>
export default {
  name: 'AppNavbar'
}
</script>
