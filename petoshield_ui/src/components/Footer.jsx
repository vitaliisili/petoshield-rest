import React from 'react'
import {Link} from "react-router-dom"

const Footer = () => {
    return (
        <div className='bg-dark p-16 h-96'>
            <div className='container mx-auto flex justify-center font-lato space-x-32 flex-wrap'>
                <div className='flex flex-col'>
                    <h3 className='uppercase font-bold text-nobel text-sm'>Features</h3>
                    <ul className='text-white flex flex-col mt-5 space-y-4'>
                        <Link to='/price'><li className='hover:text-rose transition-all duration-500'>Pet Care</li></Link>
                        <Link to='/giveback'><li className='hover:text-rose transition-all duration-500'>Giveback</li></Link>
                        <Link to='#'><li className='hover:text-rose transition-all duration-500'>API Doc</li></Link>
                    </ul>
                </div>
                <div className='flex flex-col'>
                    <h3 className='uppercase font-bold text-nobel text-sm'>Resources</h3>
                    <ul className='text-white flex flex-col mt-5 space-y-4'>
                        <Link to='/blog'><li className='hover:text-rose transition-all duration-500'>Blog</li></Link>
                        <Link to='/question'><li className='hover:text-rose transition-all duration-500'>FAQ</li></Link>
                    </ul>
                </div>
                <div className='flex flex-col'>
                    <h3 className='uppercase font-bold text-nobel text-sm'>Companies</h3>
                    <ul className='text-white flex flex-col mt-5 space-y-4'>
                        <Link to='/team'><li className='hover:text-rose transition-all duration-500'>Join the Team</li></Link>
                        <Link to='#'><li className='hover:text-rose transition-all duration-500'>Accessibility</li></Link>
                    </ul>
                </div>
                <div>
                    <h3 className='uppercase font-bold text-nobel text-sm'>Region</h3>
                </div>
            </div>
        </div>
    )
}

export default Footer