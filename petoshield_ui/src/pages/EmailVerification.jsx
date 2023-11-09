import React, {useEffect} from 'react';
import NavBar from "../components/NavBar";
import HelpModal from "../components/HelpModal";
import givebackPizza from "../static/images/giveback/giveback-pizza.svg";
import {MdOutlineDone} from "react-icons/md";
import givebackPhone from "../static/images/giveback/giveback-phone.svg";
import givebackArrow from "../static/images/giveback/arrow.svg";
import givebackFaces from "../static/images/giveback/giveback-people.svg";
import givebackCoin from "../static/images/giveback/giveback-coin.svg";
import givebackHearth from "../static/images/giveback/giveback-hearth.svg";
import {Link, useNavigate, useParams} from "react-router-dom";
import Footer from "../components/Footer";
import axios from "axios";
import {API_USER_URL} from "../utils/apiUrls";

const EmailVerification = () => {

    const queryParams = new URLSearchParams(window.location.search);
    const token = queryParams.get('token');
    const navigate = useNavigate()

    useEffect(() => {
        axios.post(`${API_USER_URL}verify_email/`, {
            token
        }).then(response => {
            if (response.status === 200){
                console.log('Email verified success')
            }
        }).catch(error => {
            console.log(error)
        })
    }, [])

    return (
        <div className='text-black'>
            <NavBar/>
            <HelpModal/>

            <main className='pt-32'>

            </main>

            <footer>
                <Footer/>
            </footer>
        </div>
    );
};

export default EmailVerification;