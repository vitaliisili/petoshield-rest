import React, {useState} from 'react';
import NavBar from "../components/NavBar";
import HelpModal from "../components/HelpModal";
import Footer from "../components/Footer";
import cat from '../static/images/register/cat-round.gif'
import {Link} from "react-router-dom";

const Register = () => {

    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [fullName, setFullName] = useState('')
    const [checkPassword, setCheckPassword] = useState('')

    const registerHandler = () => {
        //     TODO: Register User and redirect to login page send email
    }

    return (
        <div className='text-black flex flex-col h-screen bg-black-haze'>
            <NavBar/>
            <HelpModal/>

            <main className='flex-grow pt-44 flex justify-center items-center bg-black-haze'>
                <form action="#" className='flex flex-col p-4 rounded-sm w-[500px]'>
                    <div>
                        <h1 className='text-center font-bold font-lato text-2xl pb-10'>Create your account</h1>
                    </div>
                    <div className='flex flex-col space-y-8'>
                        <div className='flex flex-col relative'>
                            <input onChange={(e) => setEmail(e.target.value)} value={email} type="email" id='email' className='input-focus p-3.5 outline-0 border border-gallery rounded-md' placeholder='Email'/>
                        </div>

                        <div className='flex flex-col relative'>
                            <input onChange={(e) => setFullName(e.target.value)} value={fullName} type="text" id='name' className='input-focus p-3.5 outline-0 border border-gallery rounded-md' placeholder='Full Name'/>
                        </div>

                        <div className='flex flex-col relative'>
                            <input onChange={(e) => setPassword(e.target.value)} value={password} type="password" id='password' className='input-focus p-3.5 outline-0 border border-gallery rounded-md' placeholder='Password'/>
                        </div>

                        <div className='flex flex-col relative'>
                            <input onChange={(e) => setCheckPassword(e.target.value)} value={checkPassword} type="password" id='cpassword' className='input-focus p-3.5 outline-0 border border-gallery rounded-md' placeholder='Confirm Password'/>
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
                </form>
            </main>

            <footer className=''>
                <Footer/>
            </footer>
        </div>
    )
}

export default Register