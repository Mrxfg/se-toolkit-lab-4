import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    host: true,
    proxy: {
      '/items': {
        target: 'http://10.93.25.213:42002',
        changeOrigin: true,
      },
    },
  },
})
