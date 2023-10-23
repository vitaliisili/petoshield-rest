import React, {useEffect, useState} from 'react';
import Footer from "../components/Footer";
import NavBar from "../components/NavBar";
import HelpModal from "../components/HelpModal";
import axios from "axios";
import {getCookie} from "../utils/cookiesUtils";
import {useNavigate} from "react-router-dom";

const Account = () => {

    const [profile, setProfile] = useState(null)
    const navigate = useNavigate()

    // useEffect(() => {
    //     const accessToken = getCookie('accessToken')
    //     if (accessToken) {
    //
    //     }else {
    //         navigate('/login')
    //     }
    //
    // }, []);

    return (
        <div className='text-black'>
            <NavBar/>
            <HelpModal/>

            <main>
                Account Page
            </main>

            <footer>
                <Footer/>
            </footer>
        </div>
    )
}

export default Account;