import * as firebase from 'firebase/app'
import 'firebase/auth'
import app from './firebase'

const handleGoogleLogin=async()=>{
    const provider=new firebase.auth.GoogleAuthProvider();
    app.auth().signInWithPopup(provider).then((result)=>{
        console.log("Google Login success")
    }).catch((err)=>{
        console.log(err)
    })
}

const handleLogout=async()=>{
    app.auth().signOut()
}

export {handleGoogleLogin,handleLogout}