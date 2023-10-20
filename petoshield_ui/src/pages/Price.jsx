import React from 'react';
import HelpModal from "../components/HelpModal";
import NavBar from "../components/NavBar";
import Footer from "../components/Footer";

const Price = () => {
    return (
        <div className='text-black'>
            <HelpModal/>
            <NavBar/>

            <main>
                Price
            </main>

            <footer>
                <Footer/>
            </footer>
        </div>
    )
}

export default Price