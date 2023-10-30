import React, {useState} from 'react';
import HelpModal from "../components/HelpModal";
import NavBar from "../components/NavBar";
import Footer from "../components/Footer";
import {useLocation} from "react-router-dom";
import useFetch from "../utils/useFetch";

const PetRegistration = () => {
    const location = useLocation()
    const { type } = location.state

    const [petName, setPetName] = useState(null)
    const [petAge, setPetAge] = useState(null)
    const [petGender, setPetGender] = useState(null)
    const [petSpecies, setPetSpecies] = useState(null)
    const [petBreed, setPetBreed] = useState(null)

    const [userName, setUserName] = useState(null)
    const [userEmail, setUserEmail] = useState(null)
    const [userPassword, setUserPassword] = useState(null)

    const {data:breed, isPending, error} = useFetch("http://localhost:8080")
    console.log(breed)

    return (
        <div className='text-black flex flex-col h-screen'>
            <HelpModal/>
            <NavBar/>

            <main className='flex-grow pt-44 flex justify-center items-center pb-28'>
                <div>

                </div>
            </main>

            <footer>
                <Footer/>
            </footer>
        </div>
    );
};

export default PetRegistration;