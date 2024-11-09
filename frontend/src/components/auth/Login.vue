<!-- src/views/Login.vue -->
<script setup>
import { ref } from 'vue';
import { useUserStore } from '@/stores';
import { useRouter } from 'vue-router';
import { ApiClient } from '@/services/apiClient.js';

const userStore = useUserStore();
const router = useRouter();
const apiClient = new ApiClient();

const email = ref('');
const password = ref('');
const errorMessage = ref('');

async function login() {
  try {
    const response = await apiClient.post('/auth/login', {
      username: email.value,
      password: password.value,
    });

    const { access_token } = response.data;

    // Speichern des Tokens im User Store
    userStore.setToken(access_token);

    // Benutzerinformationen vom Backend abrufen
    const userResponse = await apiClient.get('/user/me', {
      headers: {
        Authorization: `Bearer ${access_token}`,
      },
    });

    userStore.setUser(userResponse.data)
    // Nach erfolgreichem Login
    localStorage.setItem('access_token', access_token)


    // Weiterleitung nach erfolgreicher Anmeldung
    router.push('/dashboard');
  } catch (error) {
    errorMessage.value = 'Ungültige Anmeldedaten';
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
