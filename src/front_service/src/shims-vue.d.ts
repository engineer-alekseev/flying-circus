/* eslint-disable */
declare module '*.vue' {
  import type { DefineComponent } from 'vue'
  // import { store } from '@/store';
  const component: DefineComponent<{}, {}, any>
  export default component
}
