<!-- src/views/Dashboard.vue -->
<script setup>
import { globalHelpers } from '@/composables/globalHelpers'
import { useUserStore } from '@/stores'

const { computed, useRouter } = globalHelpers

const router = useRouter()
const userStore = useUserStore()
const isAuthenticated = computed(() => userStore.isAuthenticated)
const userName = computed(() => userStore.user ? userStore.user.name : '')

function login() {
  console.log('Logging in...')
  userStore.setUser({ name: 'Mustermann', email: 'mustermann@example.com' })
}

function logout() {
  userStore.setUser(null)
}

function goToHome() {
  router.push('/')
}
</script>

<template>
  <div>
    <div class="d-flex align-center justify-center">
      <h2>Dashboard</h2>
      <v-btn class="pl-2" @click="goToHome">Zu Home</v-btn>
    </div>
    <v-container>
      <v-card class="ma-5 pa-5">
        <v-card-title class="text-h5">
          <span v-if="isAuthenticated">Willkommen, {{ userName }}!</span>
          <span v-else>Bitte melde dich an, um das Dashboard zu nutzen.</span>
        </v-card-title>
        <v-card-text>
          <p v-if="isAuthenticated">
            Hier siehst du deine Investitionen und Finanzdaten.
          </p>
          <p v-else>
            Du bist derzeit nicht eingeloggt. Klicke auf "Anmelden", um fortzufahren.
          </p>
        </v-card-text>
        <v-card-actions>
          <v-btn v-if="isAuthenticated" color="error" @click="logout">Abmelden</v-btn>
          <v-btn v-else color="primary" @click="login">Anmelden</v-btn>
        </v-card-actions>
      </v-card>
    </v-container>
  </div>
</template>

<style scoped>
.v-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
</style>
