<!-- src/views/Login.vue -->
<script setup>
import { ref } from 'vue'
import { useUserStore } from '@/stores'
import { useRouter } from 'vue-router'

const userStore = useUserStore()
const router = useRouter()

const email = ref('')
const password = ref('')
const errorMessage = ref('')

function login() {
  if (email.value === '1' && password.value === '1') {
    userStore.setUser({ name: 'Mustermann', email: email.value })
    router.push('/dashboard')
  } else {
    errorMessage.value = 'Ungültige Anmeldedaten'
  }
}
</script>

<template>
  <v-container>
    <v-card class="ma-5 pa-5">
      <v-card-title class="text-h5">Login</v-card-title>
      <v-card-text>
        <v-form @submit.prevent="login">
          <v-text-field
            v-model="email"
            label="Email"
            type="email"
            required
          ></v-text-field>
          <v-text-field
            v-model="password"
            label="Passwort"
            type="password"
            required
          ></v-text-field>
          <v-alert v-if="errorMessage" type="error">{{ errorMessage }}</v-alert>
          <v-btn type="submit" color="primary">Anmelden</v-btn>
        </v-form>
      </v-card-text>
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