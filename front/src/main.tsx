import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { GoogleOAuthProvider } from '@react-oauth/google';

import App from './App.tsx'

import './index.css'

const GOOGLE_ID = import.meta.env.GOOGLE_ID

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <GoogleOAuthProvider clientId={GOOGLE_ID}>
      <App />
    </GoogleOAuthProvider>
  </StrictMode>,
)