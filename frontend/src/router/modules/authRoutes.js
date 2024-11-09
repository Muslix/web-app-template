// src/router/modules/authRoutes.js
import AuthView from '@/views/AuthView.vue'
import Login from '@/components/auth/Login.vue'
import Register from '@/components/auth/Register.vue'

export default [
  {
    path: '/auth',
    component: AuthView,
    children: [
      {
        path: 'login',
        name: 'Login',
        component: Login,
        meta: { requiresAuth: false }, // Kein Login erforderlich
      },
      {
        path: 'register',
        name: 'Register',
        component: Register,
        meta: { requiresAuth: false }, // Kein Login erforderlich
      },
    ],
  },
]
