import React, { useEffect, useState } from "react";
import app from "../utils/firebase";
import 'firebase/auth'

export const AuthContext = React.createContext();

export const AuthProvider = ({ children }) => {
  const [currentUser, setCurrentUser] = useState(null);

  useEffect(() => {
    app.auth().onAuthStateChanged(setCurrentUser);
  }, []);

  return (
    <AuthContext.Provider
      value={{
        currentUser
      }} 
    >
      {children}
    </AuthContext.Provider>
  );
};