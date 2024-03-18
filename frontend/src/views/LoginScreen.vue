<template>
  <img src = "../assets/login.png" class = "fixed w-full h-screen z-10"/>
  <div class="flex flex-col absolute -translate-y-2/4 -translate-x-2/4 left-1/2 top-1/2 bg-white-100 rounded-xl w-2/6 h-5/12 z-20 shadow-xl">
    <img src = "../assets/unilogo.png" class = "w-64 ml-5 mb-14 mt-5"/> 
    <input type = "text" placeholder = "Username" v-on:keyup.enter="$refs.password.focus()" ref="username" class = "w-8/12 h-7 mb-2 p-2 border border-grey-200 rounded-md relative -translate-x-2/4 left-1/2 outline-red shadow-md" v-model="username"/>
    <input type = "password" placeholder = "Password" v-on:keyup.enter="loginAttempt" ref="password" class = "w-8/12 h-7 p-2 mb-2 border border-grey-200 rounded-md relative -translate-x-2/4 left-1/2 outline-red shadow-md" v-model="password"/>
    <div class = "w-8/12 relative -translate-x-2/4 left-1/2 mb-6 mt-4">
      <div class="w-32 border-2 border-red-100 rounded-md text-red-100 
      relative left-full -translate-x-full transition hover:bg-red-100 hover hover:text-white-100 drop-shadow-sm" @click="loginAttempt()">
        Login
      </div>
      <div v-if="error"> Incorrect username or password</div>
    </div>
    <div class = "flex flex-row mb-6 relative -translate-x-2/4 left-1/2 justify-center p-3">
      <a class = "text-sm hover:underline" href ="https://acctman.ucalgary.ca/register" target ="eid"> Create an eID </a>
      <div class = "mx-3">  •  </div>
      <a class = "text-sm hover:underline" href = "https://password.ucalgary.ca/recover" target = "password-recover">Forgot Password </a>
      <div class = "mx-3">  •  </div>
      <a class = "text-sm hover:underline" href = "https://ucalgary.service-now.com/it?id=kb_article&sys_id=e86c4d3913b93ec06f3afbb2e144b03d" target = "faq"> Account FAQs </a> 
      <div class = "mx-3">  •  </div>
      <a class = "text-sm hover:underline" href = "https://ucalgary.service-now.com/it?id=contact_and_help" target = "IT">Contact IT Support </a>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoginScreen',
  emits : ['logout-possible', 'logout-not-possible', 'hide-navbar'],
  data: () => {
    return {
      username: "",
      password: "",
      error: false
    }
  },
  methods: {
    loginCorrect() {
      this.$emit('logout-possible')
      if(this.$cookies.get('lastPage')) {
        this.$router.push(this.$cookies.get('lastPage'))
      } else {
        this.$router.push('/dashboard')
      }
    },
    loginIncorrect() {
      this.error = true
      this.$refs.username.focus()
      setTimeout(() => {
        this.error = false
      }, 3000)
    },
    loginAttempt() {
      // the hard coded server location defined globally
      const serverPath = this.$store.state.serverPath
      // the endpoint specific to the login
      const apiPath = "/auth/"


      // creates a json that can be sent in the body of the request
      // compatible with the library(axios) used
      const body = new FormData()
      body.append('username', this.username)
      body.append('password', this.password)
      // {
      //   username: this.username,
      //   password: this.password
      // }
    
      // the headers that are sent with the request
      const headers=  {
        'Content-Type': 'application/json',
      }
      // this.$http is equivalent to axios
      // this.$http.post creates a post request to the server
      // the first argument is the url of the server
      // the second argument is the body of the request
      // the third argument is the headers of the request
      this.$http.post(`${serverPath}${apiPath}`, body, {headers}).then(response => {
        // response the the response from the server, includes status code, data, and headers
        // response.data is the data sent from the server
        this.$cookies.set('auth-token', response.data.token)
        this.loginCorrect()
      }).catch(error => {
        // error is the error from the server, includes status code, data, and headers
        this.loginIncorrect()
        console.log(error)
      })
    }
  },
  created(){
    if(this.$cookies.get('auth-token') != null){
      this.loginCorrect()
    }
    this.$emit('logout-not-possible')
    this.$emit('hide-navbar')
  },
  mounted(){
    this.$refs.username.focus()
  }
}
</script>
        
 