import React, {useState} from 'react';
import NavBar from "../components/NavBar";
import HelpModal from "../components/HelpModal";
import Footer from "../components/Footer";
import {toast, ToastContainer} from "react-toastify";
import petSleep from "../static/images/pet-sleep.svg"
import axios from "axios";
import {API_JOB_TICKETS_URL, API_TICKETS_URL} from "../utils/apiUrls";

const Team = () => {
    const [position, setPosition] = useState('')
    const [firstName, setFirstName] = useState('')
    const [email, setEmail] = useState('')
    const [lastName, setLastName] = useState('')

    const positionData = [
        {
            'name': 'Customer Experience Specialist, French Market',
            'shortName' : 'Customer Experience',
            'location': 'Remote'
        },
        {
            'name': 'Product Quality and Compliance Specialist',
            'shortName' : 'Product Quality',
            'location': 'Remote'
        },
        {
            'name': 'Customer Experience Specialist',
            'shortName' : 'Customer Experience',
            'location': 'Remote'
        },
        {
            'name': 'Insurance Product Manager',
            'shortName' : 'Product Manager',
            'location': 'Remote'
        },
        {
            'name': 'Senior Backend Engineer',
            'shortName' : 'Backend Engineer',
            'location': 'Remote'
        },
        {
            'name': 'Senior FrontEnd',
            'shortName' : 'Senior FrontEnd',
            'location': 'Remote'
        },
        {
            'name': 'Head of Procurement',
            'shortName' : 'General & Administration',
            'location': 'Remote'
        },
        {
            'name': 'Senior Product Manager',
            'shortName' : 'Product',
            'location': 'Remote'
        },

    ]

    const positionApplyHandler = () => {
        const id = toast.loading('Please Wait...')

        axios.post(API_JOB_TICKETS_URL, {
            position,
            'first_name': firstName,
            'last_name': lastName,
            email
        }).then(response => {
            if (response.status === 201) {
                toast.update(id, {render: 'Success', type: "success", isLoading: false, autoClose: 2000})
                setFirstName('')
                setEmail('')
                setLastName('')
                setPosition('')
            }
        }).catch(error => {
            if (error.response.data.errors) {
                toast.update(id, {render: error.response.data.errors[0].detail, type: "error", isLoading: false, autoClose: 5000})
            }else{
                toast.update(id, {render: 'Server error please contact administrator', type: "error", isLoading: false, autoClose: 5000})
            }
        })
    }

    return (
        <div className='text-black flex flex-col h-screen'>
            <ToastContainer/>
            <NavBar/>
            <HelpModal/>

            <main className='flex flex-grow flex-col pt-28 items-center font-lato'>
                <section className='flex flex-col justify-center items-center px-4 py-12'>
                    <h1 className='font-merriweather text-3xl md:text-[40px] lg:text-[50px] text-center'>Calling All Petoshield Makers!</h1>
                    <p className='text-center text-xl md:max-w-[550px] mt-8'>We’re looking for smart creatives, filled with positive energy, and a passion for building products people love</p>
                    <img src={petSleep} alt="pet-sleep" className='mt-8'/>
                </section>

                <section className='flex flex-col justify-center items-center bg-black-haze w-full py-20 h-full'>
                    <div className='container mx-auto px-4 flex flex-col items-center max-w-[1200px]'>
                        <h2 className='font-bold text-4xl text-center'>Open positions</h2>
                        <p className='text-center text-xl md:max-w-[640px] mt-8'>Check out our available positions around the world. If you can’t find what you’re looking for, check back often as new positions open up frequently.</p>
                        <div className='bg-white rounded-md mt-16 w-full'>
                            { positionData.map((pos, index) => (
                              <div key={index} onClick={() => setPosition(pos.name)} className='flex border-b-2 px-8 py-8 border-b-black-haze justify-between hover:border hover:border-rose hover:rounded-md cursor-pointer'>
                                  <div className='font-bold w-1/2'>{pos.name}</div>
                                  <div className='flex w-1/2 pl-4'>
                                      <div className='text-nobel-dark w-1/2'>{pos.shortName}</div>
                                      <div className='flex justify-center text-nobel-dark w-1/2 pl-4'>{pos.location}</div>
                                  </div>

                              </div>
                            ))}
                        </div>
                    </div>
                </section>

                <section className='flex flex-col py-20 w-full justify-center items-center px-4'>
                    <div>
                        <h2 className='font-bold text-4xl'>Apply for position</h2>
                    </div>
                    <div className='flex flex-col  space-y-4 mt-12'>
                        <div className='flex space-x-4 text-center'>
                            <input className='w-full input-focus p-3 outline-0 border border-gallery rounded-md focus:border-gallery focus:ring-0' type="text" onChange={(e) => setFirstName(e.target.value)} value={firstName} placeholder='First Name'/>
                            <input className='w-full input-focus p-3 outline-0 border border-gallery rounded-md focus:border-gallery focus:ring-0' type="text" onChange={(e) => setLastName(e.target.value)} value={lastName} placeholder='Last Name'/>
                        </div>
                        <input className='w-full input-focus p-3 outline-0 border border-gallery rounded-md focus:border-gallery focus:ring-0' type="email" onChange={(e) => setEmail(e.target.value)} value={email} placeholder='Email address'/>
                        <input className='w-full input-focus p-3 outline-0 border border-gallery rounded-md focus:border-gallery focus:ring-0' type="text" placeholder='Position' disabled value={position}/>
                        <button onClick={positionApplyHandler} className='w-full self-end rounded-md bg-rose hover:bg-rose-dark font-bold transition-all duration-300 shadow-[rgba(255,0,131,0.5)_0px_10px_40px_-10px] px-4 py-3 text-white'>APPLY NOW</button>
                    </div>

                </section>
            </main>

            <footer>
                <Footer/>
            </footer>
        </div>
    )
}

export default Team;