<template>
  <div class="component">
    <div class="btn" @click="loginCorrect()">
      Click here to login
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoginScreen',
  data: () => {
    return {
      // Component data
    }
  },
  methods: {
    loginCorrect() {
      this.$router.push('/dashboard')
    },
  },
}
</script>
        
 