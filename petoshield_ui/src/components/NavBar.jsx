import React, {useEffect, useRef, useState} from 'react'
import {Link} from "react-router-dom"
import {RxHamburgerMenu} from "react-icons/rx"
import SideMenu from "./SideMenu"
import {VscAccount} from "react-icons/vsc";

const NavBar = () => {

    const [isMenuOpen, setIsMenuOpen] = useState(false)
    let menuRef = useRef()

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

    return (
        <div>
            <nav className='p-6 border-b border-b-gallery w-full top-0 bg-white z-40 fixed '>
                <div className='flex justify-between'>
                    <left-menu className='flex border'>
                        <ul className='space-x-6 hidden md:flex'>
                            <Link to='/'><li className='transition-all duration-700 hover:scale-110'>Home</li></Link>
                            <Link to='/price'><li className='transition-all duration-700 hover:scale-110'>Price</li></Link>
                            <Link to='/blog'><li className='transition-all duration-700 hover:scale-110'>Blog</li></Link>
                            <Link to='/partners'><li className='transition-all duration-700 hover:scale-110 hidden lg:block'>Partners Program</li></Link>
                        </ul>
                        <div className='flex md:hidden cursor-pointer' onClick={() => setIsMenuOpen(true)}>
                            <RxHamburgerMenu id='menu-icon' className='text-xl'/>
                        </div>
                    </left-menu>
                    <div className='right-menu transition-all duration-700 hover:scale-110 hidden md:flex'><Link to='/account'>My Account</Link></div>
                    <div className='right-menu transition-all duration-700 hover:scale-110 flex items-center text-2xl md:hidden'><Link to='/account'><VscAccount/></Link></div>
                </div>
                <div className='font-bold font-dancing text-3xl flex justify-center -mt-8'>Petoshield</div>
            </nav>
            { isMenuOpen &&
                <div ref={menuRef} className='md:hidden'>
                    <SideMenu closeMenuHandler={closeMenuHandler}/>
                </div>
            }
        </div>
    )
}

export default NavBar