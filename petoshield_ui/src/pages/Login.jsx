import React, {useState} from 'react';
import NavBar from "../components/NavBar";
import HelpModal from "../components/HelpModal";
import Footer from "../components/Footer";
import dog from '../static/images/login/dog-and-ball.gif'
import {Link} from "react-router-dom";

const Login = () => {

    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')


    const loginHandler = () => {
    //     TODO: Login User save access token in cookie and redirect to account page
    }

    return (
        <div className='text-black flex flex-col h-screen bg-black-haze'>
            <NavBar/>
            <HelpModal/>

            <main className='flex-grow pt-44 flex justify-center items-center pb-28 bg-black-haze'>
                <form action="#" className='flex flex-col p-4 rounded-sm w-[500px]'>
                    <div>
                        <h1 className='text-center font-bold font-lato text-2xl pb-10'>Account Login</h1>
                    </div>
                    <div className='flex flex-col space-y-8'>
                        <div className='flex flex-col relative'>
                            <input onChange={(e) => setEmail(e.target.value)} value={email} type="email" id='email' className='input-focus p-3.5 outline-0 border border-gallery rounded-md' placeholder='Email'/>
                        </div>

                        <div className='flex flex-col relative'>
                            <input onChange={(e) => setPassword(e.target.value)} value={password} type="password" id='password' className='input-focus p-3.5 outline-0 border border-gallery rounded-md' placeholder='Password'/>
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
                </form>
            </main>

            <footer className=''>
                <Footer/>
            </footer>
        </div>
    )
}

export default Login