import React from 'react'
import {BrowserRouter,Route} from 'react-router-dom'
import Login from './login'
import Register from './register'

export default ()=>{
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