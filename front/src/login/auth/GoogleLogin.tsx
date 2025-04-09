import React from 'react';
import { GoogleLogin, CredentialResponse } from '@react-oauth/google';
import axios from 'axios';


export const GoogleLoginButton: React.FC = () => {
  const handleLogin = async (credentialResponse: CredentialResponse) => {
    if (!credentialResponse.credential) return;
    
    try {
      const res = await axios.post("http://localhost:9000/v1/auth/", {
        access_token: credentialResponse.credential,
        withCredentials: true
      });
      
      // handle JWT or user info
      console.log("Login successful:", res.data);
      // e.g., store token in localStorage or context
    } catch (error) {
      console.log(error.toJSON());
    }
  };

  return (
    <GoogleLogin onSuccess={handleLogin} onError={() => console.log("Google Login Failed")} />
  );
};