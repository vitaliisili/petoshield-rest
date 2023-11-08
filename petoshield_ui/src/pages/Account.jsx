import React, {useEffect, useState} from 'react';
import Footer from "../components/Footer";
import NavBar from "../components/NavBar";
import HelpModal from "../components/HelpModal";
import axios from "axios";
import {getCookie, removeCookie} from "../utils/cookiesUtils";
import {Link, useNavigate} from "react-router-dom";
import defaultProfile from '../static/images/account/default-profile.svg'
// import defaultProfile from '../static/images/account/test-profile.png'
import {API_PETS_URL, API_USER_SELF, API_USER_URL} from "../utils/apiUrls";
import {toast, ToastContainer} from "react-toastify";
import {IoLogOutOutline} from "react-icons/io5";
import {PiCatDuotone, PiDogDuotone} from "react-icons/pi";

const Account = () => {

    const [profile, setProfile] = useState(null)
    const navigate = useNavigate()
    const [pets, setPets] = useState(null)

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

    useEffect(() => {
        axios.get(API_PETS_URL, {
            headers: {
                "Authorization": `Bearer ${getCookie('accessToken')}`
            }
        }).then(response => {
            if (response.status === 200){
                setPets(response.data)
            }
        }).catch(error => {
            toast.error('Failed to load pets')
        })
    }, [])

    const logoutHandler = () => {
        removeCookie('accessToken')
        toast.success(`Bye Bye ${profile.name}`)
        setTimeout(() => {
            navigate('/login')
        }, 3000)

    }

    return (
        <div className='text-black flex flex-col h-screen bg-black-haze'>
            <ToastContainer/>
            <NavBar/>
            <HelpModal/>

            <main className='flex flex-col pt-28 pb-10 bg-black-haze items-center justify-center font-lato'>
                <div className='flex flex-col lg:flex-row items-center lg:items-start'>
                    { profile &&
                        <div className='left flex flex-col w-96 lg:w-72 h-fit bg-white p-8 rounded-md space-y-8'>
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

                            <button onClick={logoutHandler} className='flex justify-center text-xs items-center border border-rose rounded-md w-28 py-1.5 px-1.5 bg-rose text-white font-bold uppercase hover:bg-rose-dark transition-all duration-300 shadow-[rgba(255,0,131,0.5)_0px_10px_40px_-10px]'><IoLogOutOutline className='text-xl mr-2'/> Logout</button>
                        </div>
                    }

                    <div className='right flex flex-col bg-white rounded-md p-8 ml-4 shadow-sm align-top mt-8 lg:mt-0'>
                        <div className='flex justify-between'>
                            <div className='text-xl font-bold'>Pet Information</div>
                            <Link to='/new-pet'><button className='rounded-md bg-rose hover:bg-rose-dark font-bold transition-all duration-300 shadow-[rgba(255,0,131,0.5)_0px_10px_40px_-10px] py-2 px-3 text-sm text-white uppercase'>Add new pet</button></Link>
                        </div>
                        
                        <div className='flex flex-col mt-8 space-y-4'>

                            {pets && pets.map((pet) => (
                                    <div onClick={() => navigate(`/pet-profile/${pet.id}`)} key={pet.id} className='pet-card flex justify-center items-center border-2 border-gallery rounded-md p-4 shadow-md transition-all duration-500 hover:scale-105 cursor-pointer'>
                                        <div className='border-2 border-gallery rounded-full p-2'>
                                            {pet.species === 'cat'? <PiCatDuotone className='text-4xl'/> : <PiDogDuotone className='text-4xl'/>}
                                        </div>
                                        <div className='flex flex-col ml-4 w-full'>
                                            <div className='flex justify-between'>
                                                <div className='font-bold text-lg'>{pet.name}</div>
                                                <div className='text-sm'>Insurance is active</div>
                                            </div>
                                            <div className='flex justify-between w-full'>
                                                {pet.gender === 'F' ? 'Female' : 'Male'}
                                                <span className='text-rose mx-1'>|</span>
                                                {pet.breed}
                                                <span className='text-rose mx-1'>|</span>
                                                {pet.age} years old
                                            </div>

                                        </div>
                                    </div>
                                ))}
                        </div>
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