import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'

const __dirname = path.dirname(new URL(import.meta.url).pathname)

// https://vitejs.dev/config/
export default defineConfig({
  base: '/',
  plugins: [vue()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
      '@style': path.resolve(__dirname, './src/assets/css'),
    },
  },
  css: {
    preprocessorOptions: {
      scss: {
        additionalData: `@import "@/assets/css/_variables.scss";`
      }
    }
  },
  server: {
    proxy: {
      '/auth_service': {
          target: 'http://auth_service:8000',
          changeOrigin: true,
          // rewrite: (path) => path.replace(/^\/auth_service/, '')
      },
      '/booking_service': {
        target: 'http://booking_service:8000',
        changeOrigin: true,
        // rewrite: (path) => path.replace(/^\/booking_service/, '')
      },
      '/send_one_message': {
        target: 'http://mail_service:8000',
        changeOrigin: true,
        // rewrite: (path) => path.replace(/^\/send_one_message/, '')
    }
  }
}
})
