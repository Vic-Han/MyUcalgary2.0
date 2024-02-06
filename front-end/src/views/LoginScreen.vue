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
      //this.$emit('show-navbar')
      this.$router.push('/dashboard')
    },
  },
  created(){
    this.$emit('hide-navbar')
  }
}
</script>
        
 