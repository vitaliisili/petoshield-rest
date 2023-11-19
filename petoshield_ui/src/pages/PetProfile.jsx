import React, {useEffect, useState} from 'react';
import {ToastContainer} from "react-toastify";
import NavBar from "../components/NavBar";
import HelpModal from "../components/HelpModal";
import {useNavigate, useParams} from "react-router-dom";
import Footer from "../components/Footer";
import axios from "axios";
import {API_PETS_URL} from "../utils/apiUrls";
import {getCookie} from "../utils/cookiesUtils";
import cat from "../static/images/price/cat-passive.svg"
import dog from "../static/images/price/dog-passive.svg"
import boy from "../static/images/boy-and-bike.svg"
import {LuShieldAlert, LuShieldCheck, LuShieldClose} from "react-icons/lu";
import {MdOutlineEuro} from "react-icons/md";
import ConfirmModal from "../components/ConfirmModal";
import SubscriptionConfirm from "../components/SubscriptionConfirm";
import Clouds from "../components/Clouds";

const PetProfile = () => {

    const navigate = useNavigate()
    const params = useParams()
    const [pet, setPet] = useState(null)
    const [petDeleteModal, setPetDeleteModal] = useState(false)
    const [petSubscription, setPetSubscription] = useState(false)

    useEffect(() => {
        axios.get(`${API_PETS_URL}${params.id}/`, {
            headers: {
                'Authorization': `Bearer ${getCookie('accessToken')}`
            }
        }).then(response  => {
            if (response.status === 200) {
                setPet(response.data)
                console.log(response.data)
            }
        }).catch(error => {
            console.log(error)
        })
    }, [params]);

    return (
        <div className='text-black flex flex-col h-screen'>
            <ToastContainer
                closeOnClick
                draggable
            />
            <NavBar/>
            <HelpModal/>

            {pet && <ConfirmModal type='pet' object={pet} toggle={petDeleteModal} callback={() => setPetDeleteModal(false)}/>}
            {pet && <SubscriptionConfirm object={pet.policy} toggle={petSubscription} callback={() => setPetSubscription(false)}/>}
            <Clouds type='dark' zIndex='-z-20'/>

            <main className='flex-grow pt-44 flex justify-center pb-28'>
                { pet &&
                    <div className='flex flex-col md:flex-row bg-white h-fit p-8 rounded-md shadow-md space-y-10 md:space-y-0 md:space-x-12'>
                        <div className='flex flex-col justify-between h-[400px]'>
                            <div className='space-y-8'>
                                <div className='flex items-center justify-center'>
                                    <img src={pet.species === 'cat' ? cat : dog} alt="pet" className='-mt-6 -ml-3'/>
                                    <div className='font-bold font-dancing text-[60px] text-nobel-dark'>{pet.name}</div>
                                </div>

                                <div className='flex space-x-12'>
                                    <div>
                                        <div className='text-nobel-dark text-2xl'>Breed:</div>
                                        <div className='text-dark-grey text-lg'>{pet.breed}</div>
                                    </div>

                                    <div>
                                        <div className='text-nobel-dark text-2xl'>Pet age:</div>
                                        <div className='text-dark-grey text-lg'>{pet.age} years old</div>
                                    </div>
                                </div>


                                <div>
                                    <div className='text-nobel-dark text-2xl'>Gender:</div>
                                    <div className='text-dark-grey text-lg'>{pet.gender === 'F' ? 'Female' : 'Male'}</div>
                                </div>
                            </div>
                            <button onClick={() => setPetDeleteModal(true)} className='w-full self-end rounded-md bg-rose hover:bg-rose-dark font-bold transition-all duration-300 shadow-[rgba(255,0,131,0.5)_0px_10px_40px_-10px] px-4 py-4 text-white'>Remove Pet From Account</button>
                        </div>

                        <div className='h-[1px] md:h-96 md:w-[1px] bg-rose'></div>

                        <div className='flex flex-col justify-between h-[400px]'>
                            <div className='space-y-12'>
                                <div className='text-4xl mt-8 text-nobel-dark'>Pet Insurance</div>

                                <div className='flex space-x-12'>
                                    <div>
                                        <div className='text-nobel-dark text-2xl'>Status:</div>
                                        {pet.policy.status === 'invalid' && <div className='text-dark-grey flex text-lg items-center'>Insurance is not active <LuShieldAlert className='ml-2 text-rose'/></div>}
                                        {pet.policy.status === 'valid' &&   <div className='text-dark-grey flex text-lg items-center'>Insurance is active       <LuShieldCheck className='ml-2 text-rose'/></div>}
                                        {pet.policy.status === 'expired' && <div className='text-dark-grey flex text-lg items-center'>Insurance expired       <LuShieldClose className='ml-2 text-rose'/></div>}
                                    </div>

                                    {pet.policy.status === 'valid' ?
                                        <div>
                                            <div className='text-nobel-dark text-2xl'>Start Date:</div>
                                            <div className='text-dark-grey text-lg'>{pet.policy.start_date}</div>
                                        </div>: <div></div>
                                    }
                                </div>


                                <div className='flex space-x-12'>
                                    <div>
                                        <div className='text-nobel-dark text-2xl'>Policy Number</div>
                                        <div className='text-dark-grey text-lg'>{pet.policy.policy_number}</div>
                                    </div>

                                    <div>
                                        <div className='text-nobel-dark text-2xl'>Deductible</div>
                                        <div className='text-dark-grey text-lg flex items-center'>{pet.policy.deductible}  <MdOutlineEuro className='ml-1' /></div>
                                    </div>
                                </div>
                            </div>

                            <div className=''>
                                {pet.policy.status === 'valid' ?
                                    <button onClick={() => setPetSubscription(true)} className='w-full rounded-md bg-rose hover:bg-rose-dark font-bold transition-all duration-300 shadow-[rgba(255,0,131,0.5)_0px_10px_40px_-10px] px-4 py-4 text-white'>Cancel Subscription</button> :
                                    <button onClick={() => navigate(`/pet-quote/${pet.id}`)} className='w-full rounded-md bg-rose hover:bg-rose-dark font-bold transition-all duration-300 shadow-[rgba(255,0,131,0.5)_0px_10px_40px_-10px] px-4 py-4 text-white'>Get Your Quote</button>
                                }
                            </div>

                        </div>
                    </div>
                }

            </main>
            <img className='bottom-0 -z-10 -mt-48' src={boy} alt="boy"/>
            <footer className=''>
                <Footer/>
            </footer>
        </div>
    );
};

export default PetProfile;