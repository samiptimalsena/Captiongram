import React,{useContext} from 'react'
import {handleLogout} from '../../utils/firebase_login'
import {AuthContext} from '../../auth/auth'

export default ()=>{
    const {currentUser}=useContext(AuthContext)
    return(
        <div style={{"textAlign":"center","margin":"auto","display":"flex","flexDirection":"column",width:"500px","marginTop":"75px"}}>
            <h1>Welcome, {currentUser.displayName}</h1>
            <img src={currentUser.photoURL}/>
            <button style={{"width":"100px","margin":"auto","marginTop":"20px"}} onClick={handleLogout}>LogOut</button>
        </div>
    )
}