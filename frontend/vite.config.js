import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// During development (`npm run dev`), Vite runs on port 5173 and the
// FastAPI backend runs separately on port 8000. This proxy means the React
// code can always just call fetch('/api/...') — Vite forwards it to
// FastAPI under the hood, so there's no CORS setup to think about and no
// "which URL am I on" branching in the frontend code. In production, the
// built app is served directly by FastAPI, so '/api/...' is already
// same-origin and this proxy simply isn't used.
export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
      },
    },
  },
})
