// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import homeRoutes from './modules/homeRoutes'
import dashboardRoutes from './modules/dashboardRoutes'
import authRoutes from './modules/authRoutes'
import { useUserStore } from '@/stores'

const routes = [...homeRoutes, ...dashboardRoutes, ...authRoutes]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

// Navigation Guard
router.beforeEach(async (to, from, next) => {
  const userStore = useUserStore()
  const isAuthenticated = userStore.isAuthenticated
  if (!userStore.isAuthenticated) {
    await userStore.fetchUser(); // Versuchen, Benutzerinformationen zu laden
  }
  if (to.meta.requiresAuth && !isAuthenticated) {
    next({ name: 'Login' })
  } else {
    next()
  }
})

export default router
