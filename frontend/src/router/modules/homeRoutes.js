// src/router/modules/dashboardRoutes.js
import Home from '@/views/Home.vue'

export default [
  {
    path: '/',
    name: 'Home',
    component: Home,
    meta: { requiresAuth: false }, // Meta für Authentifizierung
  },
  // Weitere Dashboard-bezogene Routen
]
