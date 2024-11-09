
  
  <script setup>
  import { ref } from 'vue';
  import { useRouter } from 'vue-router';
  import { ApiClient } from '@/services/apiClient.js';
  
  const router = useRouter();
  const username = ref('');
  const email = ref('');
  const password = ref('');
  const confirmPassword = ref('');
  const errorMessage = ref('');
  const apiClient = new ApiClient();

  async function register() {
    if (password.value !== confirmPassword.value) {
      errorMessage.value = 'Die Passwörter stimmen nicht überein.';
      return;
    }
  
    try {
      const response = await apiClient.post('/auth/register', {
        username: username.value,
        email: email.value,
        password: password.value,
      });
  
      if (response.status === 201) {
        router.push('/login');
      } else {
        errorMessage.value = response.data.message || 'Registrierung fehlgeschlagen.';
      }
    } catch (error) {
        console.log("error", error)
      errorMessage.value = error.response?.data?.message || 'Registrierung fehlgeschlagen.';
    }
  }
  </script>
  <template>
    <v-container>
      <v-card class="ma-5 pa-5">
        <v-card-title class="text-h5">Registrierung</v-card-title>
        <v-card-text>
          <v-form @submit.prevent="register">
            <v-text-field v-model="username" label="Benutzername" required></v-text-field>
            <v-text-field v-model="email" label="E-Mail" type="email" required></v-text-field>
            <v-text-field v-model="password" label="Passwort" type="password" required></v-text-field>
            <v-text-field v-model="confirmPassword" label="Passwort bestätigen" type="password" required></v-text-field>
            <v-alert v-if="errorMessage" type="error">{{ errorMessage }}</v-alert>
            <v-btn type="submit" color="primary">Registrieren</v-btn>
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
  