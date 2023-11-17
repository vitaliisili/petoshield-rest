import React from 'react';
import NavBar from "../components/NavBar";
import HelpModal from "../components/HelpModal";
import Footer from "../components/Footer";
import {ToastContainer} from "react-toastify";

const Team = () => {
    return (
        <div className='text-black flex flex-col h-screen'>
            <ToastContainer/>
            <NavBar/>
            <HelpModal/>

            <main className='flex flex-grow flex-col pt-28 items-center font-lato'>
                Team
            </main>

            <footer>
                <Footer/>
            </footer>
        </div>
    )
}

export default Team;