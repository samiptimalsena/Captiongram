import React,{useContext} from 'react'
import {BrowserRouter,Route,Redirect} from 'react-router-dom'
import Login from './login'
import Register from './register'
import {AuthContext} from '../../auth/auth'

export default ()=>{
    const {currentUser}=useContext(AuthContext)
    if (currentUser){
        return <Redirect to="/"/>
    }
    return(
        <BrowserRouter>
        <Route exact path="/">
            <Login/>
        </Route>
        <Route path="/register">
            <Register/>
        </Route>
        </BrowserRouter>
    )
}