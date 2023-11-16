import React, {useState} from 'react';
import {toast, ToastContainer} from "react-toastify";
import NavBar from "../components/NavBar";
import HelpModal from "../components/HelpModal";
import Footer from "../components/Footer";
import handClick from "../static/images/payment/click.gif"
import axios from "axios";
import {API_USER_URL} from "../utils/apiUrls";
import {RESET_PASSWORD_REDIRECT_LINK} from "../utils/config";

const PasswordRecovery = () => {

    const [email, setEmail] = useState('')

    const submitHandler = () => {
        const id = toast.loading('Please Wait...')
        if (!email) {
            toast.update(id, {render: 'Email is required', type: "error", isLoading: false, autoClose: 5000})
        }else {
            axios.post(`${API_USER_URL}reset_password/`, {
                email,
                "redirect_link": RESET_PASSWORD_REDIRECT_LINK
            }).then(response => {
                if (response.status === 200) {
                    toast.update(id, {render: 'Please check your email', type: "success", isLoading: false, autoClose: 5000})
                    setEmail('')
                }
            }).catch(error => {
                toast.update(id, {render: error.response.data.errors[0].detail, type: "error", isLoading: false, autoClose: 5000})
            })
        }


    }
    return (
        <div className='text-black flex flex-col h-screen'>
            <ToastContainer/>
            <NavBar/>
            <HelpModal/>

            <main className='flex flex-grow flex-col pt-28 items-center font-lato justify-end bg-lilac'>
                <div className='flex flex-col items-center w-96 -mb-32 z-10'>
                    <div className='text-rose font-dancing font-bold text-3xl'>Please insert your email</div>
                    <input onChange={(e) => setEmail(e.target.value)} value={email} type="email" id='email' className='bg-lilac w-full mt-8 input-focus p-3.5 outline-0 border border-gallery rounded-md focus:border-gallery focus:ring-0 shadow-md' placeholder='Email'/>
                </div>
                <img className='cursor-pointer' onClick={submitHandler} src={handClick} alt="hand"/>
            </main>

            <footer>
                <Footer/>
            </footer>
        </div>
    );
};

export default PasswordRecovery;