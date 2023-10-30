import React, {useEffect, useRef, useState} from 'react'
import {Link, useNavigate} from "react-router-dom"
import {RxHamburgerMenu} from "react-icons/rx"
import SideMenu from "./SideMenu"
import {VscAccount} from "react-icons/vsc";
import {getCookie, removeCookie} from "../utils/cookiesUtils";
import axios from "axios";
import {API_USER_SELF} from "../utils/apiUrls";

const NavBar = () => {

    const [isMenuOpen, setIsMenuOpen] = useState(false)
    let menuRef = useRef()
    const navigate = useNavigate()

    const closeMenuHandler = () => {
        setIsMenuOpen(false)
    }

    useEffect(() => {
        let handler = (e) => {
            if (menuRef.current && !menuRef.current.contains(e.target)) {
                setIsMenuOpen(false)
            }
        }
        document.addEventListener('mousedown', handler)
    })

    const profileHandle = () => {
        const accessToken = getCookie('accessToken')

        if (accessToken) {
            axios.get(API_USER_SELF, {
                headers: {
                    "Authorization": `Bearer ${getCookie('accessToken')}`
                }
            })
                .then(response => {
                    if (response.status === 200) {
                        localStorage.setItem('userId', response.data.id)
                        navigate('/account')
                    }
                    else {
                        throw new Error(response.data)
                    }
                }).catch(error => {
                    // console.log(error.detail)
                    navigate('/login')
            })
        } else {
            navigate('/login')
        }
    }

    return (
        <div>
            <nav className='p-6 border-b border-b-gallery w-full top-0 bg-white z-40 fixed h-[75px]'>
                <div className='flex justify-between'>
                    <left-menu className='flex border'>
                        <ul className='space-x-6 hidden md:flex'>
                            <Link to='/'>
                                <li className='transition-all duration-700 hover:scale-110'>Home</li>
                            </Link>
                            <Link to='/price'>
                                <li className='transition-all duration-700 hover:scale-110'>Price</li>
                            </Link>
                            <Link to='/blog'>
                                <li className='transition-all duration-700 hover:scale-110'>Blog</li>
                            </Link>
                            <Link to='/partners'>
                                <li className='transition-all duration-700 hover:scale-110 hidden lg:block'>Partners
                                    Program
                                </li>
                            </Link>
                        </ul>
                        <div className='flex md:hidden cursor-pointer' onClick={() => setIsMenuOpen(true)}>
                            <RxHamburgerMenu id='menu-icon' className='text-xl'/>
                        </div>
                    </left-menu>
                    <div onClick={profileHandle}
                         className='right-menu cursor-pointer transition-all duration-700 hover:scale-110 hidden md:flex'>My
                        Account
                    </div>
                    <div onClick={profileHandle}
                         className='right-menu cursor-pointer transition-all duration-700 hover:scale-110 flex items-center text-2xl md:hidden'>
                        <VscAccount/></div>
                </div>
                <div className='font-bold font-dancing text-3xl flex justify-center -mt-8'>Petoshield</div>
            </nav>
            {isMenuOpen &&
                <div ref={menuRef} className='md:hidden'>
                    <SideMenu closeMenuHandler={closeMenuHandler}/>
                </div>
            }
        </div>
    )
}

export default NavBar