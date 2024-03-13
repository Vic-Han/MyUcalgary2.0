<template>
    <div class="bg-primary">
        <div class="text-secondary-100">This is the Application Homepage Component</div>
        <div class="text-secondary-100">I setup some custom colors I defined in tailwind config.js</div>
        <!-- Button added below -->
        <button @click="goToNewPage" class="bg-blue-500 text-white font-bold py-2 px-4 rounded hover:bg-blue-700">
            Click Me
          </button>
          
    </div>
</template>

<script>
export default {
  name: 'ApplicationHomepage',
  methods: {
    goToNewPage() {
      this.$router.push({ name: 'NewPage' });
    }
  },
  created() {
    this.$emit('show-navbar');
    this.$emit('toggle-selected', 'application');
  }
}
</script>

