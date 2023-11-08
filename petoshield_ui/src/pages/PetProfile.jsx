import React, {useEffect, useState} from 'react';
import {ToastContainer} from "react-toastify";
import NavBar from "../components/NavBar";
import HelpModal from "../components/HelpModal";
import {Link, useParams} from "react-router-dom";
import Footer from "../components/Footer";
import axios from "axios";
import {API_PETS_URL} from "../utils/apiUrls";
import {getCookie} from "../utils/cookiesUtils";

const PetProfile = () => {

    const params = useParams()
    const [pet, setPet] = useState(null)

    useEffect(() => {
        axios.get(`${API_PETS_URL}${params.id}/`, {
            headers: {
                'Authorization': `Bearer ${getCookie('accessToken')}`
            }
        }).then(response  => {
            if (response.status === 200) {
                setPet(response.data)
            }
        }).catch(error => {
            console.log(error)
        })
    }, []);


    return (
        <div className='text-black flex flex-col h-screen bg-black-haze'>
            <ToastContainer
                closeOnClick
                draggable
            />
            <NavBar/>
            <HelpModal/>

            <main className='flex-grow pt-44 flex justify-center items-center pb-28 bg-black-haze'>

            </main>

            <footer className=''>
                <Footer/>
            </footer>
        </div>
    );
};

export default PetProfile;