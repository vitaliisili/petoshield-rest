import React from 'react';
import NavBar from "../components/NavBar";
import HelpModal from "../components/HelpModal";
import Footer from "../components/Footer";

const Blog = () => {
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

export default Blog;