import React, {useEffect, useState} from 'react';
import Footer from "../components/Footer";
import NavBar from "../components/NavBar";
import HelpModal from "../components/HelpModal";
import axios from "axios";
import {getCookie, removeCookie} from "../utils/cookiesUtils";
import {Link, useNavigate} from "react-router-dom";
import defaultProfile from '../static/images/account/nature.gif'
import {API_PETS_URL, API_USER_SELF, API_USER_URL} from "../utils/apiUrls";
import {toast, ToastContainer} from "react-toastify";
import {IoLogOutOutline} from "react-icons/io5";
import cat from "../static/images/price/cat-passive.svg"
import dog from "../static/images/price/dog-passive.svg"
import houses from "../static/images/account/houses.png"
import {MdOutlineMail, MdOutlineSettings} from "react-icons/md";
import {REACT_APP_BACKEND_URL} from "../utils/config";

const Account = () => {

    const [profile, setProfile] = useState(null)
    const navigate = useNavigate()
    const [pets, setPets] = useState(null)
    const [isLoading, setIsLoading] = useState(true)

    useEffect(() => {
            axios.get(API_USER_SELF, {
                headers: {
                    "Authorization": `Bearer ${getCookie('accessToken')}`
                }
            }).then(response => {
                if (response.status === 200){
                    setProfile(response.data)
                    setIsLoading(false)
                }
            }).catch(error => {
                toast.error('Failed to load profile')
                if (error.response.status === 401) {
                    removeCookie('accessToken')
                    navigate('/login')
                }
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
                setIsLoading(false)
            }
        }).catch(error => {
            toast.error('Failed to load pets')
            if (error.response.status === 401) {
                removeCookie('accessToken')
                navigate('/login')
            }
        })
    }, [])

    const logoutHandler = () => {
        removeCookie('accessToken')
        toast.success(`Bye Bye ${profile.name}`)
        setTimeout(() => {
            navigate('/login')
        }, 2000)

    }

    return (
        <div className='text-black flex flex-col h-screen bg-black-haze'>
            <ToastContainer/>
            <NavBar/>
            <HelpModal/>

            <main className='flex flex-grow flex-col pt-28 pb-10 bg-black-haze items-center justify-center font-lato relative'>
                <div className='flex flex-col items-center justify-end w-full h-full z-10 absolute overflow-hidden '>
                    <img className='min-w-[1200px] xl:min-w-[2000px] -mb-32 opacity-10' src={houses} alt="bg"/>
                </div>

                <div className='flex flex-col lg:flex-row items-center py-20 lg:items-start z-20'>
                    { profile &&
                        <div className='left flex flex-col w-96 lg:w-72 h-fit bg-white p-8 rounded-md space-y-8 shadow-md'>
                            <div className='flex justify-center items-center border rounded-full w-32 h-32 self-center overflow-hidden'>
                                <img className='p-1 w-full h-full rounded-full bg-cover' src={profile.image ? `${REACT_APP_BACKEND_URL}/${profile.image}` : defaultProfile} alt="profile"/>
                            </div>

                            <div className='flex justify-center items-center'>
                                <div className='text-2xl text-nobel-dark font-bold '>{profile.name}</div>
                            </div>

                            <div>
                                <div className='flex justify-between items-center'>
                                    <div className='font-bold text-nobel-dark flex justify-center items-center'><MdOutlineMail className='text-xl mr-2' /> Email Address</div>
                                    {profile.is_verified ?
                                        <div className='text-xs text-green font-bold'>verified</div> :
                                        <div className='text-xs text-rose-dark font-bold'>not verified</div>
                                    }
                                </div>
                                <div className='ml-7'>{profile.email}</div>
                            </div>

                            <div className='flex flex-col'>
                                <div className='font-bold text-nobel-dark flex items-center'><MdOutlineSettings className='text-xl mr-2'/> Profile Settings</div>
                                <div className='text-sm ml-7'><Link className='hover:text-rose shadow-sm' to={`/profile-update`}>Update Profile</Link></div>
                            </div>

                            <button onClick={logoutHandler} className='flex justify-center text-xs items-center border border-rose rounded-md w-28 py-1.5 px-1.5 bg-rose text-white font-bold uppercase hover:bg-rose-dark transition-all duration-300 shadow-[rgba(255,0,131,0.5)_0px_10px_40px_-10px]'><IoLogOutOutline className='text-xl mr-2'/> Logout</button>
                        </div>
                    }

                    <div className='right flex flex-col bg-white rounded-md py-8 px-4 md:p-8 ml-4 shadow-md align-top mt-8 lg:mt-0'>
                        <div className='flex justify-between min-w-[400px]'>
                            <div className='text-xl font-bold'>Pet Information</div>
                            <Link to='/new-pet'><button className='rounded-md bg-rose hover:bg-rose-dark font-bold transition-all duration-300 shadow-[rgba(255,0,131,0.5)_0px_10px_40px_-10px] py-2 px-3 text-sm text-white uppercase'>Add new pet</button></Link>
                        </div>
                        
                        <div className='flex flex-col mt-8 space-y-4'>
                            {pets && pets.map((pet) => (
                                    <div onClick={() => navigate(`/pet-profile/${pet.id}`)} key={pet.id} className='pet-card flex justify-center items-center border-2 border-gallery rounded-md p-4 shadow-md transition-all duration-500 hover:scale-105 cursor-pointer md:w-full'>
                                        <div className=''>
                                            <img src={pet.species === 'cat' ? cat : dog} alt="pet" className='-mt-6 w-20 md:w-full'/>
                                        </div>
                                        <div className='flex flex-col ml-4 w-full'>
                                            <div className='flex justify-between'>
                                                <div className='font-bold text-2xl text-nobel-dark font-dancing'>{pet.name}</div>
                                                {pet.policy.status === 'invalid' && <div className='text-sm text-rose'>insurance is not active</div>}
                                                {pet.policy.status === 'valid' && <div className='text-sm text-green font-bold'>insurance is active</div>}
                                                {pet.policy.status === 'expired' && <div className='text-sm text-rose'>insurance expired</div>}

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

            <footer className='z-30'>
                <Footer/>
            </footer>
        </div>
    )
}

export default Account;