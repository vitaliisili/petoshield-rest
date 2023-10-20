import React from 'react';
import NavBar from "../components/NavBar";
import HelpModal from "../components/HelpModal";
import Footer from "../components/Footer";

const Giveback = () => {
    return (
        <div className='text-black'>
            <NavBar/>
            <HelpModal/>

            <main>
                Giveback
            </main>

            <footer>
                <Footer/>
            </footer>
        </div>
    )
}

export default Giveback;