import React from 'react';
import {BrowserRouter, Route, Routes} from "react-router-dom";
import Home from "./pages/Home";
import Price from "./pages/Price";
import Account from "./pages/Account";
import Partners from "./pages/Partners";
import Blog from "./pages/Blog";
import Team from "./pages/Team";
import FAQ from "./pages/FAQ";
import Giveback from "./pages/Giveback";
import Login from "./pages/Login";
import NotFound from "./pages/NotFound";
import Register from "./pages/Register";
import PasswordRecovery from "./pages/PasswordRecovery";
import PetRegistration from "./pages/PetRegistration";
import PetOnlyRegistration from "./pages/PetOnlyRegistration";
import PetProfile from "./pages/PetProfile";
import PrivateRoute from "./utils/PrivateRoute";
import EmailVerification from "./pages/EmailVerification";
import Quote from "./pages/Quote";
import Payment from "./pages/Payment";
import UserProfileUpdate from "./pages/UserProfileUpdate";
import PasswordRecoveryConfirm from "./pages/PasswordRecoveryConfirm";

const App = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route exact path='/' element={<Home/>}/>
                <Route path='/price' element={<Price/>}/>
                <Route path='/account' element={<PrivateRoute><Account/></PrivateRoute>}/>
                <Route path='/partners' element={<Partners/>}/>
                <Route path='/team' element={<Team/>}/>
                <Route path='/giveback' element={<Giveback/>}/>
                <Route path='/login' element={<Login/>}/>
                <Route path='/register' element={<Register/>}/>
                <Route path='/pass-recovery' element={<PasswordRecovery/>}/>
                <Route path='/pass-recovery/confirm' element={<PasswordRecoveryConfirm/>}/>
                <Route path='/pet-registration' element={<PetRegistration/>}/>
                <Route path='/confirm-email' element={<EmailVerification/>}/>
                <Route path='/new-pet' element={<PrivateRoute><PetOnlyRegistration/></PrivateRoute>}/>
                <Route path='/pet-profile/:id' element={<PrivateRoute><PetProfile/></PrivateRoute>}/>
                <Route path='/pet-quote/:id' element={<PrivateRoute><Quote/></PrivateRoute>}/>
                <Route path='/profile-update' element={<PrivateRoute><UserProfileUpdate/></PrivateRoute>}/>
                <Route path='/payment' element={<Payment/>}/>
                <Route path='*' element={<NotFound/>}/>
            </Routes>
        </BrowserRouter>
    )
}

export default App;
