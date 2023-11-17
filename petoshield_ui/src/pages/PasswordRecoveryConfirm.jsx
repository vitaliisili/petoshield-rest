import React, {useState} from 'react';
import {toast, ToastContainer} from "react-toastify";
import NavBar from "../components/NavBar";
import HelpModal from "../components/HelpModal";
import handClick from "../static/images/payment/click.gif";
import Footer from "../components/Footer";
import axios from "axios";
import {API_USER_URL} from "../utils/apiUrls";
import {useLocation, useNavigate} from "react-router-dom";
import QueryString from "query-string";

const PasswordRecoveryConfirm = () => {

    const location = useLocation()
    const query_option = QueryString.parse(location.search)
    const navigate = useNavigate()

    const [password, setPassword] = useState('')
    const [checkPassword, setCheckPassword] = useState('')

    const submitHandler = () => {
        const id = toast.loading('Please Wait...')
        if (password !== checkPassword) {
            toast.update(id, {render: 'Passwords and check password are not equal', type: "error", isLoading: false, autoClose: 5000})
        }else {
            axios.post(`${API_USER_URL}reset_password_confirm/`, {
                'token': query_option.token,
                password
            }).then(response => {
                if(response.status === 200) {
                    toast.update(id, {render: response.data.message, type: "success", isLoading: false, autoClose: 5000})
                    setTimeout(() => {
                        navigate('/login')
                    }, 4000)
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
                    <div className='text-rose font-dancing font-bold text-3xl'>Reset Password</div>
                    <input onChange={(e) => setPassword(e.target.value)} value={password} type="password" id='reset-password' className='bg-lilac w-full mt-8 input-focus p-3.5 outline-0 border border-gallery rounded-md focus:border-gallery focus:ring-0 shadow-md' placeholder='Password'/>
                    <input onChange={(e) => setCheckPassword(e.target.value)} value={checkPassword} type="password" id='check-reset-password' className='bg-lilac w-full mt-8 input-focus p-3.5 outline-0 border border-gallery rounded-md focus:border-gallery focus:ring-0 shadow-md' placeholder='Check Password'/>
                </div>
                <img className='cursor-pointer' onClick={submitHandler} src={handClick} alt="hand"/>
            </main>

            <footer>
                <Footer/>
            </footer>
        </div>
    );
};

export default PasswordRecoveryConfirm;