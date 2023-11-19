import React from 'react';
import leftHouse from '../static/images/home/left-house.svg';
import rightHouse from '../static/images/home/right-house.svg';
import stars from '../static/images/home/stars.svg';
import pizzaXl from '../static/images/home/pizza-xxl.svg';
import companyH from '../static/images/home/company-h.svg';
import companyV from '../static/images/home/company-v.svg';
import {Link} from "react-router-dom";
import HelpModal from "../components/HelpModal";
import Carousel from "../components/Carousel";
import NavBar from "../components/NavBar";
import Footer from "../components/Footer";
import Clouds from "../components/Clouds";

const Home = () => {
    return (
        <div className='text-black overflow-y-hidden'>
            <HelpModal/>
            <NavBar/>
            <Clouds type='dark' zIndex='-z-20'/>
            <header className=''>
                <div className='flex flex-col items-center h-full relative mt-32 overflow-hidden'>
                    <h1 className='text-3xl md:text-5xl pl-5 pr-5 font-bold content-center font-merriweather leading-10 md:leading-[70px] text-center'>
                        <p>Peace of Mind for Every Paw</p>
                        <p>Our Pet Insurance Saves the Day.</p>
                    </h1>
                    <div>
                        <Link to='/price'><button className='text-black-haze transition-all duration-300 shadow-[rgba(255,0,131,0.5)_0px_10px_40px_-10px] bg-rose hover:bg-rose-dark p-4 pl-12 pr-12 rounded-md mt-12 uppercase font-bold font-lato text-lg'>Check our price</button></Link>
                    </div>
                    <div className='flex justify-between items-end w-full'>
                        <img className='' src={leftHouse} alt="left-house"/>
                        <img className='h-[473px] z-20' src={rightHouse} alt="right-house"/>
                    </div>
                    <div className='h-[58px] w-full bg-black-haze border-[2px] border-b-black-haze border-r-black-haze border-l-black-haze border-t-gallery bottom-0 absolute -z-10'></div>
                </div>
            </header>

            <main>
                <section className='bg-black-haze font-lato p-10 pr-5 pl-5'>
                    <div className='container mx-auto pb-52'>
                        <h2 className='text-3xl md:text-5xl text-center pt-10 font-bold'>The 5 Star Insurance Company</h2>
                        <div className='mx-auto'>
                            <p className='text-center text-lg pt-3 leading-[25px]'>Petoshield one of the fastest growing pet insurance companies</p>
                            <p className='text-center text-lg leading-[25px]'>And is highly recommended by financial experts, industry leaders, and other reputable sources.</p>
                        </div>
                        <img src={stars} alt="starts" className='mt-20 h-28 mx-auto'/>
                    </div>
                </section>

                <section id='slider' className='pb-60 -mt-24 relative overflow-hidden'>
                    <Carousel/>
                </section>

                <section className='p-16 pt-28 pr-5 pl-5'>
                    <div className='container mx-auto flex items-center flex-col font-lato'>
                        <h2 className='text-3xl md:text-5xl text-center font-bold'>Already insured? We’ll help you switch!</h2>
                        <p className='text-lg pt-4 text-center'>People left these insurance companies to join Petoshield:</p>
                        <div className='p-10'>
                            <img className='hidden lg:flex w-[600px]' src={companyH} alt="company-h"/>
                            <img className='lg:hidden h-[500px]' src={companyV} alt="company-v"/>
                        </div>

                        <Link to='/price'><button className='bg-rose hover:bg-rose-dark shadow-[rgba(255,0,131,0.5)_0px_10px_40px_-10px] uppercase transition-all duration-300 p-4 text-white font-bold rounded-md'>check price and switch</button></Link>
                    </div>
                </section>

                <section className='bg-black-haze p-16 pr-5 pl-5'>
                    <div className='container mx-auto flex flex-col items-center justify-center'>
                        <h2 className='text-3xl md:text-5xl font-lato font-bold text-center'>How Petoshield Works</h2>
                        <p className='text-center text-black lg:w-[900px] mx-auto pt-4'>Petoshield reverses the traditional insurance model. We treat the premiums you pay as if it's your money, not ours. With Petoshield, everything becomes simple and transparent. We take a flat fee, pay claims super fast, and <Link to='/giveback' className='text-rose hover:text-rose-dark'>give back</Link> what’s left to causes you care about.</p>
                        <img className='mt-20 md:mt-32' src={pizzaXl} alt="pizza"/>
                    </div>
                </section>
            </main>

            <footer>
                <Footer/>
            </footer>
        </div>
    )
}

export default Home;