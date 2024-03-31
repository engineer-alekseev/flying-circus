import { createRouter, createWebHistory } from 'vue-router'
import SignInPage from '@/components/SignInPage.vue'
import SignUpPage from '@/components/SignUpPage.vue'
import HomePage from '@/components/pages/HomePage.vue'
import MapPage from '@/components/pages/MapPage.vue'
import Calendar from '@/components/pages/Calendar.vue'

const router = createRouter({
    history: createWebHistory('/'),
    routes: [
        {
            path: '/',
            redirect: '/signin'
        },
        {
            name: 'SignIn',
            path: '/signin',
            component: SignInPage,
        },
        {
            name: 'SignUp',
            path: '/signup',
            component: SignUpPage,
        },
        {
            name: 'Home',
            path: '/home',
            component: HomePage,
        },
        {
            name: 'Calendar',
            path: '/calendar',
            component: Calendar,
        },

        {
            name: 'Map',
            path: '/map',
            component: MapPage,
        },
    ]
})

// const tgId = computed(() => store.state.user.telegram_id);
// router.beforeEach((to, _from, next) => {
//     const isAuthenticated = localStorage.getItem("token");
//     if (to.name !== 'SignIn' && !isAuthenticated) {
//       next({ name: 'SignIn' });
//     } else {
//       next();
//     }
//   })

export default router;
