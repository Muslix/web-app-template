// src/stores/index.js
import { createPinia } from 'pinia';
import { createORM } from 'pinia-orm';
// src/stores/index.js
import { useUserStore } from './user'

export {
  useUserStore,
}

const pinia = createPinia();
const orm = createORM();

pinia.use(orm.install);

export default pinia;
