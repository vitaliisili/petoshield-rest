import React from 'react'
import {Link} from "react-router-dom"
import {BsApple, BsGooglePlay} from "react-icons/bs";
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import {FaFacebookF, FaInstagram, FaTwitter, FaYoutube} from "react-icons/fa";

const Footer = () => {

    const appNotify = () => toast.info('App is coming soon!')

    return (
        <div className='bg-dark pt-16 pb-32 '>
            <ToastContainer />
            <div className='container pl-5 pr-5 md:pl-0 md:pr-0 mx-auto grid grid-cols-2 md:flex justify-around xl:justify-center xl:space-x-32 font-lato'>
                <div className='flex flex-col'>
                    <h3 className='uppercase font-bold text-nobel text-sm'>Companies</h3>
                    <ul className='text-white flex flex-col mt-5 space-y-4'>
                        <Link to='/team'><li className='hover:text-rose transition-all duration-500'>Join the Team</li></Link>
                        <Link to='/partners'><li className='transition-all duration-500 hover:text-rose'>Partners Program</li></Link>
                    </ul>
                </div>

                <div className='flex flex-col'>
                    <h3 className='uppercase font-bold text-nobel text-sm'>Resources</h3>
                    <ul className='text-white flex flex-col mt-5 space-y-4'>
                        <Link to='/account'><li className='hover:text-rose transition-all duration-500'>Account</li></Link>
                        <Link to='https://api.petoshield.com' target="_blank" rel="noopener noreferrer"><li className='hover:text-rose transition-all duration-500'>API Doc</li></Link>
                    </ul>
                </div>

                <div className='flex flex-col mt-7 md:mt-0'>
                    <h3 className='uppercase font-bold text-nobel text-sm'>Features</h3>
                    <ul className='text-white flex flex-col mt-5 space-y-4'>
                        <Link to='/price'><li className='hover:text-rose transition-all duration-500'>Pet Care</li></Link>
                        <Link to='/giveback'><li className='hover:text-rose transition-all duration-500'>Giveback</li></Link>
                    </ul>
                </div>

                <div className='flex flex-col mt-7 md:mt-0 '>
                    <h3 className='uppercase font-bold text-nobel text-sm'>GET OUR APP</h3>
                    <div className='flex mt-5 flex-col md:flex-row'>
                        <div className='text-gallery'>
                            <div onClick={appNotify}  className='border w-40 border-black hover:bg-dark-grey cursor-pointer flex rounded-md p-1 pr-4 pl-2 justify-center items-center'>
                                <BsApple className='text-3xl'/>
                                <div className='ml-2'>
                                    <div className='text-[12px]'>Coming Soon!</div>
                                    <div className='text-[14px] font-bold font-[time]'>App Store</div>
                                </div>
                            </div>
                        </div>

                        <div className='text-gallery ml-0 md:ml-4 mt-3 md:mt-0'>
                            <div onClick={appNotify} className='border w-40 border-black hover:bg-dark-grey cursor-pointer flex rounded-md p-1 pr-4 pl-2 justify-center items-center'>
                                <BsGooglePlay className='text-3xl'/>
                                <div className='ml-2'>
                                    <div className='text-[12px]'>Coming Soon!</div>
                                    <div className='text-[14px] font-bold font-[time]'>Google Play</div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div className='mt-7'>
                        <div className='font-bold text-nobel text-sm'>FOLLOW US</div>
                        <div className='mt-5 flex justify-start space-x-4 md:space-x-0 md:justify-between text-2xl text-gallery'>
                            <Link to='https://www.facebook.com/petoshield.eu/' target="_blank" rel="noopener noreferrer"><FaFacebookF className='hover:text-rose cursor-pointer transition-all duration-300'/></Link>
                            <Link to='https://twitter.com/petoshield' target="_blank" rel="noopener noreferrer"><FaTwitter className='hover:text-rose cursor-pointer transition-all duration-300'/></Link>
                            <Link to='https://www.youtube.com/@petoshield' target="_blank" rel="noopener noreferrer"><FaYoutube className='hover:text-rose cursor-pointer transition-all duration-300'/></Link>
                            <Link to='https://www.instagram.com/petoshield.eu/' target="_blank" rel="noopener noreferrer"><FaInstagram className='hover:text-rose cursor-pointer transition-all duration-300'/></Link>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    )
}

export default Footer