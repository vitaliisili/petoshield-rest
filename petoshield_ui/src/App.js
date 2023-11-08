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

const App = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route exact path='/' element={<Home/>}/>
                <Route exact path='/price' element={<Price/>}/>
                <Route exact path='/account' element={<PrivateRoute><Account/></PrivateRoute>}/>
                <Route exact path='/partners' element={<Partners/>}/>
                <Route exact path='/blog' element={<Blog/>}/>
                <Route exact path='/team' element={<Team/>}/>
                <Route exact path='/question' element={<FAQ/>}/>
                <Route exact path='/giveback' element={<Giveback/>}/>
                <Route exact path='/login' element={<Login/>}/>
                <Route exact path='/register' element={<Register/>}/>
                <Route exact path='/pass-recovery' element={<PrivateRoute><PasswordRecovery/></PrivateRoute>}/>
                <Route exact path='/pet-registration' element={<PetRegistration/>}/>
                <Route exact path='/new-pet' element={<PrivateRoute><PetOnlyRegistration/></PrivateRoute>}/>
                <Route exact path='/pet-profile/:id' element={<PrivateRoute><PetProfile/></PrivateRoute>}/>
                <Route exact path='*' element={<NotFound/>}/>
            </Routes>
        </BrowserRouter>
    )
}

export default App;
