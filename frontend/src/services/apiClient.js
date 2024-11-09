// src/services/apiClient.js
import axios from 'axios';
import { useUserStore } from '@/stores';

export class ApiClient {
  constructor(baseURL = 'http://localhost:5000') {
    this.client = axios.create({
      baseURL,
      headers: {
        'Content-Type': 'application/json',
      },
    });

    // Interceptor zum Hinzufügen des Tokens
    this.client.interceptors.request.use((config) => {
      const userStore = useUserStore();
      if (userStore.token) {
        config.headers.Authorization = `Bearer ${userStore.token}`;
      }
      return config;
    });
  }

  get(url, params) {
    return this.client.get(url, { params });
  }

  post(url, data) {
    return this.client.post(url, data);
  }

  put(url, data) {
    return this.client.put(url, data);
  }

  delete(url) {
    return this.client.delete(url);
  }
}

export default ApiClient;
