import React from 'react';
import NavBar from "../components/NavBar";
import HelpModal from "../components/HelpModal";
import Footer from "../components/Footer";

const Partners = () => {
    return (
        <div className='text-black'>
            <HelpModal/>
            <NavBar/>

            <main>
                Partners
            </main>

            <footer>
                <Footer/>
            </footer>
        </div>
    )
}

export default Partners;