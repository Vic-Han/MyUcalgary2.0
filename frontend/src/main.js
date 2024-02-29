import { createApp } from 'vue'
import VueCookies from 'vue-cookies'
import App from './App.vue'
// import the router and store instances
import router from './config/routes.js'
import store from './config/store.js'
// import axios to make requests to backend
import axios from 'axios'
// import the global css file and tailwind utilities
import './index.css'
import './tailwind.css'

const app = createApp(App)
app.use(VueCookies, { expires: '30m'})
app.use(router)
app.use(store)
app.config.globalProperties.$http = axios
app.mount('#app')
