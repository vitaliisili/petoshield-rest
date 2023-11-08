import React from 'react';
import {Navigate} from "react-router-dom";
import {getCookie} from "./cookiesUtils";

const PrivateRoute = ({children}) => {
    let auth = getCookie('accessToken')
    return auth ? children : <Navigate to="/login" />;
}

export default PrivateRoute