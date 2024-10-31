// src/main.js
import { createApp, watch } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'
// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import { useUserStore } from '@/stores'


const app = createApp(App)

const vuetify = createVuetify({
    components,
    directives,
  })

app.use(router)
app.use(createPinia())
app.use(vuetify)

const userStore = useUserStore()

// Globaler Watcher für Authentifizierungsstatus
watch(
  () => userStore.isAuthenticated,
  (isAuthenticated) => {
    if (!isAuthenticated) {
      router.push('/')
    }
  }
)

app.mount('#app')
