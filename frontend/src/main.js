import { createApp } from 'vue'
import App from './App.vue'
// import the router and store instances
import router from './config/routes.js'
import store from './config/store.js'
// import the global css file and tailwind utilities
import './index.css'
import './tailwind.css'

// create the app instance using the router and store then mount it to the DOM
createApp(App).use(router).use(store).mount('#app')
