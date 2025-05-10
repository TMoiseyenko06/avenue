import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import {Auth0Provider} from '@auth0/auth0-react'

const domain = process.env.REACT_APP_AUTH0_DOMAIN
const clientid = process.env.REACT_APP_AUTH0_CLIENT_ID


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Auth0Provider
    domain={domain}
    clientId = {clientid}
    authorizationParams={{
      redirect_uri: window.location.origin,
      scopes: ['openid','email','profile'],
      audience: "https://dev-vwmcthm72y47461e.us.auth0.com/api/v2/",
      prompt: "consent"
    }}
    >
    <App />
    </Auth0Provider>
    
  </React.StrictMode>
);

