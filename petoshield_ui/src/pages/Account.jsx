import React, {useEffect, useState} from 'react';
import Footer from "../components/Footer";
import NavBar from "../components/NavBar";
import HelpModal from "../components/HelpModal";
import axios from "axios";
import {getCookie} from "../utils/cookiesUtils";
import {Link, useNavigate} from "react-router-dom";
import defaultProfile from '../static/images/account/default-profile.svg'
// import defaultProfile from '../static/images/account/test-profile.png'
import {API_USER_SELF, API_USER_URL} from "../utils/apiUrls";
import {toast, ToastContainer} from "react-toastify";
import {IoLogOutOutline} from "react-icons/io5";

const Account = () => {

    const [profile, setProfile] = useState(null)
    const navigate = useNavigate()

    useEffect(() => {
            axios.get(API_USER_SELF, {
                headers: {
                    "Authorization": `Bearer ${getCookie('accessToken')}`
                }
            }).then(response => {
                if (response.status === 200){
                    setProfile(response.data)
                }
            }).catch(error => {
                toast.error('Failed to load profile')
            })
    }, [])



    return (
        <div className='text-black flex flex-col h-screen bg-black-haze'>
            <ToastContainer/>
            <NavBar/>
            <HelpModal/>

            <main className='flex flex-col md:flex-row flex-grow pt-20 bg-black-haze justify-center items-center font-lato'>
                { profile &&
                    <div className='left flex flex-col w-72 bg-white p-8 rounded-md space-y-8'>
                        <div className='flex justify-center items-center border-2 border-rose rounded-full w-32 h-32 self-center overflow-hidden'>
                            <img className='p-1 w-full h-full rounded-full bg-cover' src={defaultProfile} alt="profile"/>
                        </div>

                        <div className='flex justify-center items-center'>
                            <div className='text-xl font-bold'>{profile.name}</div>
                        </div>

                        <div>
                            <div className='flex justify-between items-center'>
                                <div className='text-sm font-bold text-nobel-dark'>Email Address</div>
                                <div className='text-xs text-green font-bold'>verified</div>
                                {/*<div className='text-xs text-rose-dark font-bold'>not verified</div>*/}
                            </div>
                            <div className='text-rose'>{profile.email}</div>
                        </div>

                        <div className='flex flex-col'>
                            <div className='text-sm font-bold text-nobel-dark'>Profile Settings</div>
                            <div className='text-sm'><Link className='hover:text-rose shadow-sm' to=''>Update Profile</Link> | <Link className='hover:text-rose shadow-sm' to='#'>Delete Account</Link></div>
                        </div>

                        <button className='flex justify-center text-xs items-center border border-rose rounded-md w-28 py-1.5 px-1.5 bg-rose text-white font-bold uppercase hover:bg-rose-dark transition-all duration-300 shadow-[rgba(255,0,131,0.5)_0px_10px_40px_-10px]'><IoLogOutOutline className='text-xl mr-2'/> Logout</button>
                    </div>
                }

                <div className='right flex flex-col '>
                    <div>
                        
                    </div>
                </div>
            </main>

            <footer>
                <Footer/>
            </footer>
        </div>
    )
}

export default Account;