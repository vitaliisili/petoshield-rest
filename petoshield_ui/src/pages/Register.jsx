import React, {useEffect, useState} from 'react';
import NavBar from "../components/NavBar";
import HelpModal from "../components/HelpModal";
import Footer from "../components/Footer";
import cat from '../static/images/register/cat-round.gif'
import {Link, useNavigate} from "react-router-dom";
import axios from "axios";
import {API_AUTH_TOKEN, API_USER_URL} from "../utils/apiUrls";
import {toast, ToastContainer} from "react-toastify";
import {setCookie} from "../utils/cookiesUtils";
import {FaRegEye, FaRegEyeSlash} from "react-icons/fa";
import TermsModal from "../components/TermsModal";
import PrivacyPolicyModal from "../components/PrivacyPolicyModal";

const Register = () => {
    const navigate = useNavigate()
    const [termsModalEnable, setTermsModalEnable] = useState(false)
    const [policyModalEnable, setPolicyModalEnable] = useState(false)

    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [fullName, setFullName] = useState('')
    const [checkPassword, setCheckPassword] = useState('')
    const [isHidden, setIsHidden] = useState(true)

    useEffect(() => {
        document.body.style.overflow = termsModalEnable || policyModalEnable ? 'hidden' : 'unset'
    }, [termsModalEnable, policyModalEnable])

    const registerHandler = () => {
        const id = toast.loading('Please Wait...')
        if (password !== checkPassword) {
            toast.update(id, {render: 'Password and check password not equals', type: "error", isLoading: false, autoClose: 7000})
            return
        }
        axios.post(API_USER_URL, {
            email,
            password,
            "name": fullName
        }).then((response) => {
            if (response.status === 201) {
                setTimeout(()=> {
                    toast.update(id, {render: 'Success', type: "success", isLoading: false, autoClose: 500})
                    setCookie('accessToken', response.data.access)
                    setCookie('refreshToken', response.data.refresh)
                    navigate('/account')
                }, 1000)
            }
        }).catch((error) => {
            toast.update(id, {render: error.response.data.errors[0].detail, type: "error", isLoading: false, autoClose: 10000})
        })
    }

    const closeModal = () => {
        setTermsModalEnable(false)
        setPolicyModalEnable(false)
    }

    return (
        <div className='text-black flex flex-col h-screen bg-black-haze'>
            <ToastContainer
                closeOnClick
            />
            <NavBar/>
            <HelpModal/>
            {termsModalEnable && <TermsModal callback={closeModal}/>}
            {policyModalEnable && <PrivacyPolicyModal callback={closeModal}/>}

            <main className='flex-grow pt-44 flex justify-center items-center bg-black-haze'>
                <div className='flex flex-col p-4 rounded-sm w-[500px]'>
                    <div>
                        <h1 className='text-center font-bold font-lato text-2xl pb-10'>Create your account</h1>
                    </div>
                    <div className='flex flex-col space-y-8'>
                        <div className='flex flex-col relative'>
                            <input onChange={(e) => setEmail(e.target.value)} value={email} type="email" id='email' className='input-focus p-3.5 outline-0 border border-gallery rounded-md focus:border-gallery focus:ring-0' placeholder='Email'/>
                        </div>

                        <div className='flex flex-col relative'>
                            <input onChange={(e) => setFullName(e.target.value)} value={fullName} type="text" id='name' className='input-focus p-3.5 outline-0 border border-gallery rounded-md focus:border-gallery focus:ring-0' placeholder='Full Name'/>
                        </div>

                        <div className='flex flex-col relative justify-center'>
                            <input onChange={(e) => setPassword(e.target.value)} value={password} type={isHidden ? "password" : "text"} id='password' className=' w-full input-focus p-3.5 outline-0 border border-gallery rounded-md focus:border-gallery focus:ring-0' placeholder='Password'/>
                            {isHidden ?
                                <FaRegEyeSlash className='text-2xl absolute right-4'  onClick={() => setIsHidden(!isHidden)}/> :
                                <FaRegEye className='text-2xl absolute right-4' onClick={() => setIsHidden(!isHidden)}/>}
                        </div>

                        <div className='flex flex-col relative justify-center'>
                            <input onChange={(e) => setCheckPassword(e.target.value)} value={checkPassword} type={isHidden ? "password" : "text"} id='check-password' className=' w-full input-focus p-3.5 outline-0 border border-gallery rounded-md focus:border-gallery focus:ring-0' placeholder='Check password'/>
                            {isHidden ?
                                <FaRegEyeSlash className='text-2xl absolute right-4'  onClick={() => setIsHidden(!isHidden)}/> :
                                <FaRegEye className='text-2xl absolute right-4' onClick={() => setIsHidden(!isHidden)}/>}
                        </div>

                        <div className='text-sm text-center text-nobel-dark'>
                            To click button bellow you are agree with <span onClick={() => setTermsModalEnable(true)} className='text-rose cursor-pointer'>Terms</span> and <span onClick={() => setPolicyModalEnable(true)} className='text-rose cursor-pointer'>Privacy Policy</span>
                        </div>

                        <div>
                            <button onClick={registerHandler} className='rounded-md bg-rose hover:bg-rose-dark font-bold transition-all duration-300 shadow-[rgba(255,0,131,0.5)_0px_10px_40px_-10px] w-full p-3.5 text-white'>Register</button>
                        </div>

                        <div className='flex items-center justify-center'>
                            <span>Already have an account? <Link to='/login'><span className='text-rose'>Login now</span></Link></span>
                        </div>
                    </div>
                    <div className='mt-8'>
                        <img className='w-full' src={cat} alt="dog"/>
                    </div>
                </div>
            </main>

            <footer className=''>
                <Footer/>
            </footer>
        </div>
    )
}

export default Register