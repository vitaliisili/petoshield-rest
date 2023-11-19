import React, {useEffect} from 'react';
import NavBar from "../components/NavBar";
import HelpModal from "../components/HelpModal";
import {useNavigate} from "react-router-dom";
import Footer from "../components/Footer";
import axios from "axios";
import {API_USER_URL} from "../utils/apiUrls";
import {ToastContainer} from "react-toastify";
import boyBike from  "../static/images/boy-and-bike.svg"
import Clouds from "../components/Clouds";


const EmailVerification = () => {

    const queryParams = new URLSearchParams(window.location.search);
    const token = queryParams.get('token');
    const navigate = useNavigate()

    useEffect(() => {
        axios.post(`${API_USER_URL}verify_email/`, {
            token
        }).then(response => {
            if (response.status === 200){
                console.log('Email verified success')
            }
        }).catch(error => {
            console.log(error)
        })
    }, [])

    return (
        <div className='text-black flex flex-col h-screen'>
            <ToastContainer/>
            <NavBar/>
            <HelpModal/>

            <main className='flex flex-grow flex-col pt-28 bg-black-haze items-center font-lato'>
                    <div className='flex flex-col justify-center items-center w-full h-full '>
                        <div className='text-[60px] font-dancing flex justify-center items-center text-rose text-center'>Thanks for verification</div>
                        <button onClick={() => navigate('/account')} className='mt-16 rounded-md bg-rose hover:bg-rose-dark font-bold transition-all duration-300 shadow-[rgba(255,0,131,0.5)_0px_10px_40px_-10px] w-80 p-3.5 text-white'>Go To Account</button>
                    </div>
                    <img src={boyBike} alt="boy"/>
            </main>

            <footer>
                <Footer/>
            </footer>
        </div>
    );
};

export default EmailVerification;