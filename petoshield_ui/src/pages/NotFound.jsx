import React from 'react';
import NavBar from "../components/NavBar";
import '../static/styles/not-found.css';

const NotFound = () => {
    return (
        <div className='h-screen text-black'>
            <NavBar/>
            <main className='flex justify-center items-center h-full '>
                <div className="center">
                    <div className="error">
                        <div className="number">4</div>
                        <div className="illustration">
                            <div className="circle"></div>
                            <div className="clip">
                                <div className="paper">
                                    <div className="face">
                                        <div className="eyes">
                                            <div className="eye eye-left"></div>
                                            <div className="eye eye-right"></div>
                                        </div>
                                        <div className="rosyCheeks rosyCheeks-left"></div>
                                        <div className="rosyCheeks rosyCheeks-right"></div>
                                        <div className="mouth"></div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div className="number">4</div>
                    </div>

                    <div className="text">Oops. The page you're looking for doesn't exist.</div>
                </div>
            </main>


        </div>
    );
};

export default NotFound;