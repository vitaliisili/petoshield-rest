import React from 'react';
import Footer from "../components/Footer";
import NavBar from "../components/NavBar";
import HelpModal from "../components/HelpModal";

const Account = () => {
    return (
        <div className='text-black'>
            <NavBar/>
            <HelpModal/>

            <main>
                Account Page
            </main>

            <footer>
                <Footer/>
            </footer>
        </div>
    )
}

export default Account;