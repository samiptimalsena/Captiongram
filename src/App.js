import React from 'react'
import LandingPage from './components/landingPage/landingPage'
import Home from './components/home/home'
import {BrowserRouter} from 'react-router-dom'
import PrivateRoutes from './routes/privateRoutes'
import { AuthProvider } from './auth/auth'

export default ()=>{
  return(
    <AuthProvider>
      <BrowserRouter>
      <PrivateRoutes path="/" component={Home}/>
    <LandingPage/>
    </BrowserRouter> 
    </AuthProvider>
  )
}