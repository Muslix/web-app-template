// src/router/modules/dashboardRoutes.js
import Dashboard from '@views/Dashboard.vue'

export default [
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
    meta: { requiresAuth: true }, // Meta für Authentifizierung
  },
  // Weitere Dashboard-bezogene Routen
]
