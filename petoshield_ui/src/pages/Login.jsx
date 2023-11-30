import React, {useState} from 'react';
import NavBar from "../components/NavBar";
import HelpModal from "../components/HelpModal";
import Footer from "../components/Footer";
import dog from '../static/images/login/dog-and-ball.gif'
import {Link, useNavigate} from "react-router-dom";
import {toast, ToastContainer} from "react-toastify";
import axios from "axios";
import {API_AUTH_TOKEN} from "../utils/apiUrls";
import {setCookie} from "../utils/cookiesUtils";
import {FaRegEye, FaRegEyeSlash} from "react-icons/fa";

const Login = () => {
    const navigate = useNavigate()
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [isHidden, setIsHidden] = useState(true)


    const loginHandler = () => {
        const id = toast.loading('Please Wait...')
        axios.post(API_AUTH_TOKEN, {
            email,
            password
        }).then((response) => {
            if (response.status === 200) {
                toast.update(id, {render: 'Success', type: "success", isLoading: false, autoClose: 2000})
                setCookie('accessToken', response.data.access)
                setCookie('refreshToken', response.data.refresh)
                setTimeout(() => {
                    navigate('/account')
                }, 1000)
            }
        }).catch((error) => {
            if (error.response) {
                toast.update(id, {render: error.response.data.errors[0].detail, type: "error", isLoading: false, autoClose: 5000})
            }else{
                toast.update(id, {render: 'Server error please contact administrator', type: "error", isLoading: false, autoClose: 5000})
            }
        })
    }

    const keyPressedHandler = (e) => {
        if (e.code === 'Enter') {
            loginHandler()
        }
    }
    return (
        <div className='text-black flex flex-col h-screen bg-black-haze'>
            <ToastContainer
                closeOnClick
                draggable
            />
            <NavBar/>
            <HelpModal/>

            <main className='flex-grow pt-44 flex justify-center items-center pb-28 bg-black-haze'>
                <div className='flex flex-col p-4 rounded-sm w-[500px]'>
                    <div>
                        <h1 className='text-center font-bold font-lato text-2xl pb-10'>Account Login</h1>
                    </div>
                    <div className='flex flex-col space-y-8'>
                        <div className='flex flex-col relative'>
                            <input onChange={(e) => setEmail(e.target.value)} value={email} type="email" id='email' className='input-focus p-3.5 outline-0 border border-gallery rounded-md focus:border-gallery focus:ring-0' placeholder='Email'/>
                        </div>

                        <div onKeyDown={keyPressedHandler} className='flex flex-col relative justify-center'>
                            <input onChange={(e) => setPassword(e.target.value)} value={password} type={isHidden ? "password" : "text"} id='password' className=' w-full input-focus p-3.5 outline-0 border border-gallery rounded-md focus:border-gallery focus:ring-0' placeholder='Password'/>
                            {isHidden ?
                                <FaRegEyeSlash className='text-2xl absolute right-4'  onClick={() => setIsHidden(!isHidden)}/> :
                                <FaRegEye className='text-2xl absolute right-4' onClick={() => setIsHidden(!isHidden)}/>}
                        </div>

                        <div>
                            <button onClick={loginHandler} className='rounded-md bg-rose hover:bg-rose-dark font-bold transition-all duration-300 shadow-[rgba(255,0,131,0.5)_0px_10px_40px_-10px] w-full p-3.5 text-white'>Log In</button>
                        </div>

                        <div className='flex justify-around'>
                            <Link to='/register'><span className='hover:text-rose duration-300 transition-all'>Create Account</span></Link>
                            <span>|</span>
                            <Link to='/pass-recovery'><span className='hover:text-rose duration-300 transition-all'>Forgot Password?</span></Link>
                        </div>
                    </div>
                    <div className='mt-16'>
                        <img className='w-full' src={dog} alt="dog"/>
                    </div>
                </div>
            </main>

            <footer className=''>
                <Footer/>
            </footer>
        </div>
    )
}

export default Login