// src/router/modules/dashboardRoutes.js
import Login from '@/views/Login.vue'

export default [
  {
    path: '/login',
    name: 'Login',
    component: Login,
    meta: { requiresAuth: false }, // Meta für Authentifizierung
  },
  // Weitere Dashboard-bezogene Routen
]
