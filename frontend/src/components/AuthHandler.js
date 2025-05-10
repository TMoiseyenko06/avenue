import { useAuth0 } from "@auth0/auth0-react";
import { useEffect, useState } from "react";
import axios from "axios";

const AuthHandler = () => {
  const {getAccessTokenSilently, isAuthenticated} = useAuth0()

  useEffect(()=>{
    const fetchToken = async () => {
      if (isAuthenticated) {
        try{
          const token = await getAccessTokenSilently({
            authorizationParams: {
              audience: "https://dev-vwmcthm72y47461e.us.auth0.com/api/v2/",
              prompt: 'consent',
              scopes: ['openid','email','profile']
            }
          })
          console.log(token)
          const response = await axios.post('http://localhost:5000/api/auth',{},{
            headers: {
              Authorization: `Bearer ${token}`,
            }
          })
        } catch(err){
          console.log(err)
        }
      }
    }
    fetchToken()
  },[isAuthenticated, getAccessTokenSilently])
};

export default AuthHandler;
