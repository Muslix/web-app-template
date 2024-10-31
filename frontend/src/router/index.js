// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import homeRoutes from './modules/homeRoutes'
import dashboardRoutes from './modules/dashboardRoutes'
import loginRoutes from './modules/loginRoutes'
import { useUserStore } from '@/stores' // Importiere Pinia für Authentifizierung

const routes = [
  ...homeRoutes,
  ...dashboardRoutes,
  ...loginRoutes
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

// Navigation Guard
router.beforeEach((to, from, next) => {
  const userStore = useUserStore()
  const isAuthenticated = userStore.isAuthenticated // Annahme: boolean Flag für Auth-Status

  if (to.meta.requiresAuth && !isAuthenticated) {
    next({ name: 'Login' }) // Leitet zur Login-Seite weiter
  } else {
    next()
  }
})

export default router
