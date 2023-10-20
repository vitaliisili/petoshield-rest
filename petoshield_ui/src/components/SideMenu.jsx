import React from 'react';
import {IoCloseSharp} from "react-icons/io5";
import {Link} from "react-router-dom";
import {FaFacebookF, FaInstagram, FaTwitter} from "react-icons/fa";

const SideMenu = (props) => {
    return (
        <div className={`fixed flex flex-col h-full bg-dark-grey w-72 flex z-50`}>
            <div id='side-menu' className='h-screen flex flex-col justify-between p-8'>
                <div onClick={() => props.closeMenuHandler()} className='absolute top-3 right-3 text-gallery cursor-pointer flex justify-center items-center w-8 h-8'>
                    <IoCloseSharp className='text-xl'/>
                </div>

                <ul className='flex flex-col text-white space-y-5 font-lato'>
                    <Link to='/'><li className='transition-all duration-300 hover:text-rose'>Home</li></Link>
                    <Link to='/price'><li className='transition-all duration-300 hover:text-rose'>Price</li></Link>
                    <Link to='#'><li className='transition-all duration-300 hover:text-rose'>Blog</li></Link>
                    <Link to='#'><li className='transition-all duration-300 hover:text-rose'>Partners Program</li></Link>
                    <Link to='#'><li className='transition-all duration-300 hover:text-rose'>My Account</li></Link>
                </ul>

                <div className='flex justify-around'>
                    <Link to='#'><div className='w-14 h-14 bg-black text-white rounded-full transition-all duration-300 flex justify-center items-center hover:bg-rose cursor-pointer'><FaFacebookF className='text-3xl'/></div></Link>
                    <Link to='#'><div className='w-14 h-14 bg-black text-white rounded-full transition-all duration-300 flex justify-center items-center hover:bg-rose cursor-pointer'><FaInstagram className='text-3xl'/></div></Link>
                    <Link to='#'><div className='w-14 h-14 bg-black text-white rounded-full transition-all duration-300 flex justify-center items-center hover:bg-rose cursor-pointer'><FaTwitter className='text-3xl'/></div></Link>
                </div>
            </div>

        </div>
    )
}

export default SideMenu;