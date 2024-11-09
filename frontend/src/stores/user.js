// src/stores/user.js
import { defineStore } from 'pinia';
import ApiClient from '@/services/apiClient';

export const useUserStore = defineStore('user', {
  state: () => ({
    user: null,
    token: localStorage.getItem('access_token') || null, // Token aus dem Local Storage initialisieren
  }),
  actions: {
    setUser(userData) {
      this.user = userData;
    },
    setToken(token) {
      this.token = token;
      localStorage.setItem('access_token', token); // Token im Local Storage speichern
    },
    logout() {
      this.user = null;
      this.token = null;
      localStorage.removeItem('access_token'); // Token aus dem Local Storage entfernen
    },
    async fetchUser() {
      if (this.token) {
        try {
          const apiClient = new ApiClient();
          const response = await apiClient.get('/user/me', {
            headers: {
              Authorization: `Bearer ${this.token}`,
            },
          });
          this.setUser(response.data);
        } catch (error) {
          console.log(error);
          this.logout();
        }
      }
    },
  },
  getters: {
    isAuthenticated: (state) => !!state.token,
    getToken: (state) => state.token,
  },
});
