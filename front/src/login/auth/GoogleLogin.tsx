import React from 'react';
import { GoogleLogin, CredentialResponse } from '@react-oauth/google';
import axios from 'axios';

export const GoogleLoginButton: React.FC = () => {
  const handleLogin = async (credentialResponse: CredentialResponse) => {
    if (!credentialResponse.credential) return;

    try {
      const res = await axios.post("http://localhost:9000/auth/google/", {
        access_token: credentialResponse.credential
      });

      // handle JWT or user info
      console.log("Login successful:", res.data);
      // e.g., store token in localStorage or context
    } catch (error) {
      console.error("Login failed:", error);
    }
  };

  return (
    <GoogleLogin onSuccess={handleLogin} onError={() => console.log("Google Login Failed")} />
  );
};