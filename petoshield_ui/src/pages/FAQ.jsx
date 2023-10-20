import React from 'react';
import NavBar from "../components/NavBar";
import HelpModal from "../components/HelpModal";
import Footer from "../components/Footer";

const Faq = () => {
    return (
        <div className='text-black'>
            <NavBar/>
            <HelpModal/>

            <main>
                FAQ
            </main>

            <footer>
                <Footer/>
            </footer>
        </div>
    )
}

export default Faq;