<!-- src/views/Home.vue -->
<script setup>
import { globalHelpers } from '@/composables/globalHelpers'
import { useUserStore } from '@/stores'

const { computed, useRouter } = globalHelpers
const userStore = useUserStore()

const router = useRouter()
const isAuthenticated = computed(() => userStore.isAuthenticated)

function goToLogin() {
  router.push('/login')
}
function goToDashboard() {
  router.push('/dashboard')
}
</script>

<template>
  <v-container>
    <v-card class="ma-5 pa-5">
      <v-card-title class="text-h5">
        Willkommen zur Investment-Tracker App!
      </v-card-title>
      <v-card-text>
        Hier kannst du deine Finanzen und Investitionen verfolgen. Melde dich
        an, um das Dashboard zu nutzen.
      </v-card-text>
      <v-card-actions >
        <v-btn v-if="!isAuthenticated" color="primary" @click="goToLogin"> Zum Login </v-btn>
        <v-btn v-else color="primary" @click="goToDashboard"> Zum Dashboard </v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<style scoped>
.v-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
</style>