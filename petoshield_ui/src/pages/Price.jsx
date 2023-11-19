import React from 'react';
import HelpModal from "../components/HelpModal";
import NavBar from "../components/NavBar";
import Footer from "../components/Footer";
import dog from "../static/images/price/dog-active.svg"
import cat from "../static/images/price/cat-active.svg"
import tree from "../static/images/price/tree.svg"
import {Link} from "react-router-dom";
import {BsCurrencyEuro} from "react-icons/bs";
import Clouds from "../components/Clouds";

const Price = () => {
    return (
        <div className='text-black flex flex-col h-screen'>
            <HelpModal/>
            <NavBar/>

            <main className='flex-grow p-8 pt-28 flex justify-center items-center pb-28'>
                {/*<Clouds type='dark' zIndex='z-10'/>*/}
                <div className='flex flex-col md:flex-row space-x-0 md:space-x-10 space-y-10 md:space-y-0 z-20'>
                    <div className="flex flex-col justify-center items-center rounded-md bg-white p-8 pl-10 pr-10 transition-all duration-500 hover:scale-105 shadow-xl">
                        <div className='text-4xl font-lato font-bold'>Dogs</div>
                        <div className='line h-[2px] w-full bg-rose rounded-2xl mt-5'></div>
                        <img className='h-60' src={dog} alt="dog"/>
                        <Link to='/pet-registration' state={{"type": "dog"}}><button className='font-bold mt-8 bg-rose font-lato hover:bg-rose-dark text-white p-2 pl-4 pr-4 rounded-md transition-all duration-300 shadow-[rgba(255,0,131,0.5)_0px_10px_40px_-10px]'>Select Coverage</button></Link>
                        <div className='mt-5'>
                            <p className='text-xs font-lato font-bold flex justify-center items-center'>Start from 10<BsCurrencyEuro/>/mo</p>
                        </div>
                    </div>

                    <div className="flex flex-col justify-center items-center rounded-md bg-white p-8 pl-10 pr-10 transition-all duration-500 hover:scale-105 shadow-xl">
                        <div className='text-4xl font-lato font-bold'>Cats</div>
                        <div className='line h-[2px] w-full bg-rose rounded-2xl mt-5'></div>
                        <img className='h-60' src={cat} alt="cat"/>
                        <Link to='/pet-registration' state={{"type": "cat"}}><button className='font-bold mt-8 bg-rose font-lato hover:bg-rose-dark text-white p-2 pl-4 pr-4 rounded-md transition-all duration-300 shadow-[rgba(255,0,131,0.5)_0px_10px_40px_-10px]'>Select Coverage</button></Link>
                        <div className='mt-5'>
                            <p className='text-xs font-lato font-bold flex justify-center items-center'>Start from 10<BsCurrencyEuro/>/mo</p>
                        </div>
                    </div>

                </div>
            </main>
            <img className='relative bottom-0 w-full -mt-36  xl:-mt-72 z-10' src={tree} alt="tree"/>
            <footer>
                <Footer/>
            </footer>
        </div>
    )
}

export default Price