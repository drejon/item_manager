/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly GOOGLE_ID: string;
  readonly VITE_GITHUB_CLIENT_ID?: string;
  // add any other env vars here
}

interface ImportMeta {
  readonly env: ImportMetaEnv;
}