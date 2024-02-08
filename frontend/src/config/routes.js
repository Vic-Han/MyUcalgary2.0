import {createRouter, createWebHistory} from 'vue-router'

// import all components that will be used as routes
import AcademicReport from '../views/AcademicReport.vue'
import DashBoard from '../views/DashBoard.vue'
import FinanceBreakdown from '../views/FinanceBreakdown.vue'
import GradeBreakdown from '../views/GradeBreakdown.vue'
import LoginScreen from '../views/LoginScreen.vue'
import MiscLinks from '../views/MiscLinks.vue'
import ProfileInfo from '../views/ProfileInfo.vue'
import RegisterScreen from '../views/RegisterScreen.vue'
import SchedBuilder from '../views/SchedBuilder.vue'

// map routes to components imported above
const routes =  [
    { path: '/', component: LoginScreen },
    { path: '/dashboard', component: DashBoard },
    { path: '/finances', component: FinanceBreakdown },
    { path: '/grades', component: GradeBreakdown },
    { path: '/misc', component: MiscLinks },
    { path: '/profile', component: ProfileInfo },
    { path: '/register', component: RegisterScreen },
    { path: '/schedule', component: SchedBuilder },
    { path: '/academics', component: AcademicReport},
]

// create the router instance and export it
const router = createRouter({
    history: createWebHistory(),
    routes,
})
export default router