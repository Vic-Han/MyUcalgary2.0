import { createApp } from 'vue'
import VueCookies from 'vue-cookies'
//import VueWorker from 'vue-worker'
import App from './App.vue'
// import the router and store instances
import router from './config/routes.js'
import store from './config/store.js'
import axios from 'axios'
// import the global css file and tailwind utilities
import './index.css'
import './tailwind.css'
//import axios from 'axios'

const app = createApp(App)
//app.use(VueWorker)
app.use(VueCookies, { expires: '1800s'})
app.use(router)
app.use(store)
app.config.globalProperties.$http = axios
app.mount('#app')
