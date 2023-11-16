import React, {useEffect, useState} from 'react';
import {ToastContainer} from "react-toastify";
import NavBar from "../components/NavBar";
import HelpModal from "../components/HelpModal";
import {Link, useNavigate, useParams} from "react-router-dom";
import Footer from "../components/Footer";
import axios from "axios";
import {API_PETS_URL} from "../utils/apiUrls";
import {getCookie} from "../utils/cookiesUtils";
import cat from "../static/images/price/cat-passive.svg"
import dog from "../static/images/price/dog-passive.svg"
import {LuShieldAlert, LuShieldCheck, LuShieldClose} from "react-icons/lu";

const PetProfile = () => {

    const navigate = useNavigate()
    const params = useParams()
    const [pet, setPet] = useState(null)

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
    }, []);


    return (
        <div className='text-black flex flex-col h-screen bg-black-haze'>
            <ToastContainer
                closeOnClick
                draggable
            />
            <NavBar/>
            <HelpModal/>

            <main className='flex-grow pt-44 flex justify-center pb-28 bg-black-haze'>
                { pet &&
                    <div className='flex flex-col md:flex-row bg-white h-fit p-8 rounded-md shadow-md space-y-10 md:space-y-0 md:space-x-12'>
                        <div className='flex flex-col space-y-8'>
                            <div className='flex items-center justify-center'>
                                <img src={pet.species === 'cat' ? cat : dog} alt="pet" className='-mt-6 -ml-3'/>
                                <div className='font-bold font-dancing text-[60px] text-nobel-dark'>{pet.name}</div>
                            </div>

                            <div>
                                <div className='text-nobel-dark text-2xl'>Breed:</div>
                                <div className='text-dark-grey text-lg'>{pet.breed}</div>
                            </div>

                            <div>
                                <div className='text-nobel-dark text-2xl'>Pet age:</div>
                                <div className='text-dark-grey text-lg'>{pet.age} years old</div>
                            </div>

                            <div>
                                <div className='text-nobel-dark text-2xl'>Gender:</div>
                                <div className='text-dark-grey text-lg'>{pet.gender === 'F' ? 'Female' : 'Male'}</div>
                            </div>

                        </div>
                        <div className='h-[1px] md:h-96 md:w-[1px] bg-rose'></div>
                        <div className='space-y-8'>
                            <div className='text-4xl mt-2 text-nobel-dark'>{pet.name} Insurance</div>
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

                            <div>
                                <div className='text-nobel-dark text-2xl'>Policy Number:</div>
                                <div className='text-dark-grey text-lg'>{pet.policy.policy_number}</div>
                            </div>

                            {pet.policy.status === 'valid' ?
                                <button  className='mt-5 self-center rounded-md bg-rose hover:bg-rose-dark font-bold transition-all duration-300 shadow-[rgba(255,0,131,0.5)_0px_10px_40px_-10px] px-4 py-2 text-white'>Cancel Subscription</button> :
                                <button onClick={() => navigate(`/pet-quote/${pet.id}`)} className='mt-5 self-center rounded-md bg-rose hover:bg-rose-dark font-bold transition-all duration-300 shadow-[rgba(255,0,131,0.5)_0px_10px_40px_-10px] px-4 py-2 text-white'>Get Your Quote</button>
                            }
                        </div>
                    </div>
                }

            </main>

            <footer className=''>
                <Footer/>
            </footer>
        </div>
    );
};

export default PetProfile;