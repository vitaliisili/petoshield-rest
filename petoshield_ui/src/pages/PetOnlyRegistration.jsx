import React, {useEffect, useState} from 'react';
import HelpModal from "../components/HelpModal";
import NavBar from "../components/NavBar";
import Footer from "../components/Footer";
import {Link, useNavigate} from "react-router-dom";
import {API_BREEDS_URL, API_PETS_URL} from "../utils/apiUrls";
import axios from "axios";
import {getCookie} from "../utils/cookiesUtils";
import {toast, ToastContainer} from "react-toastify";
import catActive from "../static/images/pet/cat-active.svg"
import catPassive from "../static/images/pet/cat-passive.svg"
import dogActive from "../static/images/pet/dog-active.svg"
import dogPassive from "../static/images/pet/dog-passive.svg"

const PetOnlyRegistration = () => {
    const navigate = useNavigate()

    const [petName, setPetName] = useState('')
    const [petAge, setPetAge] = useState('')
    const [petGender, setPetGender] = useState('F')
    const [petSpecies, setPetSpecies] = useState('dog')
    const [petBreed, setPetBreed] = useState('')

    const [breeds, setBreeds] = useState([])
    const [isDog, setIsDog] = useState(true)

    useEffect(() => {
        axios.get(`${API_BREEDS_URL}?species=${petSpecies}`, {
            headers: {
                "Authorization": `bearer${getCookie('accessToken')}`
            }
        }).then(response => {
            if (response.status === 200) {
                setBreeds(response.data)
            }
        }).catch(error => {
            console.log(error)
        })
    }, [petSpecies]);

    const onSubmitHandler = () => {
        const id = toast.loading('Please Wait...')
        let data = {
            "name": petName,
            "age": petAge,
            "gender": petGender,
            "species": petSpecies,
            "breed": petBreed,
        }

        let options = {
            headers: {
                "Authorization": `Bearer ${getCookie('accessToken')}`,
                'Content-Type': 'application/json'
            }
        }
        axios.post(API_PETS_URL, data, options)
            .then(response => {
                if (response.status === 201) {
                    toast.update(id, {render: 'Success', type: "success", isLoading: false, autoClose: 500})
                    setTimeout(() => {
                        navigate(`/pet-quote/${response.data.pet}`)
                    }, 1000)
                }
            }).catch(error => {
            toast.update(id, {
                render: error.response.data.errors[0].detail,
                type: "error",
                isLoading: false,
                autoClose: 10000
            })
        })
    }

    const catToggle = () => {
        setIsDog(false)
        setPetSpecies('cat')
        toast.success('Cat Selected', {autoClose: 1000})
    }

    const dogToggle = () => {
        setIsDog(true)
        setPetSpecies('dog')
        toast.success('Dog Selected', {autoClose: 1000})
    }

    return (
        <div className='text-black flex flex-col h-screen'>
            <ToastContainer/>
            <HelpModal/>
            <NavBar/>

            <main
                className='flex-grow pt-32 flex justify-center items-center pb-28 px-4 font-lato text-black bg-black-haze'>
                <div className='flex flex-col justify-center items-center'>
                    <div className='flex flex-col'>
                        <div className='p-4 self-center lg:self-start'>
                            <div className='font-bold text-2xl text-center'>Pet Information</div>

                            <div className='flex flex-col space-y-8 w-80'>
                                <div className='flex justify-between'>
                                    <img onClick={dogToggle} src={isDog ? dogActive : dogPassive} alt="dog"
                                         className='cursor-pointer transition-all duration-500 hover:scale-105'/>
                                    <img onClick={catToggle} src={isDog ? catPassive : catActive} alt="cat"
                                         className='cursor-pointer transition-all duration-500 hover:scale-105'/>
                                </div>
                                <input onChange={(e) => setPetName(e.target.value)} value={petName} type="text"
                                       className='outline-0 p-3 border border-gallery rounded-md focus:ring-1 focus:ring-rose shadow-sm focus:border-rose'
                                       placeholder='Pet Name'/>
                                <div className='flex justify-around'>
                                    <div className='flex justify-center items-center p-0'>
                                        <input onChange={(e) => setPetGender(e.target.value)}
                                               checked={petGender === 'F'}
                                               className='w-4 h-4 focus:ring-0 text-rose' type="radio" id='pet-gender-f'
                                               value='F' name='pet-gender'/>
                                        <label htmlFor="pet-gender-f" className='ml-1'>Female</label>
                                    </div>

                                    <div className='flex justify-center items-center p-0'>
                                        <input onChange={(e) => setPetGender(e.target.value)}
                                               checked={petGender === 'M'}
                                               className='w-4 h-4 focus:ring-0 text-rose' type="radio" id='pet-gender-m'
                                               value='M' name='pet-gender'/>
                                        <label htmlFor="pet-gender-m" className='ml-1'>Male</label>
                                    </div>
                                </div>
                                <select onChange={(e) => setPetBreed(e.target.value)} value={petBreed} name="breed"
                                        id="breed"
                                        className='outline-0 p-3 pt-3 pb-3.5 bg-white border border-gallery rounded-md text-black focus:ring-1 focus:ring-rose shadow-sm focus:border-rose'>
                                    <option className='text-gallery-dark' value=''>Please select a breed name</option>
                                    {breeds && breeds.map((breed, index) => (
                                        <option key={index} value={breed.id}>{breed.name}</option>
                                    ))}
                                </select>
                                <select onChange={(e) => setPetAge(e.target.value)} value={petAge} name="breed"
                                        id="breed"
                                        className='outline-0 p-3 pt-3 pb-3.5 bg-white border border-gallery rounded-md text-black focus:ring-1 focus:ring-rose shadow-sm focus:border-rose'>
                                    <option className='text-gallery-dark' value=''>Please select pet age</option>
                                    <option value='1'>Less than 6 month</option>
                                    <option value='1'>1 Years old</option>
                                    <option value='2'>2 Years old</option>
                                    <option value='3'>3 Years old</option>
                                    <option value='4'>4 Years old</option>
                                    <option value='5'>5 Years old</option>
                                    <option value='7'>6 Years old</option>
                                    <option value='8'>8 Years old</option>
                                    <option value='9'>9 Years old</option>
                                    <option value='10'>10 Years old</option>
                                    <option value='11'>11 Years old</option>
                                    <option value='12'>12 Years old</option>
                                    <option value='13'>13 Years old</option>
                                    <option value='14'>14 Years old</option>
                                    <option value='15'>15 Years old</option>
                                    <option value='16'>16 Years old</option>
                                    <option value='17'>17 Years old</option>
                                    <option value='18'>18 Years old</option>
                                    <option value='19'>19 Years old</option>
                                    <option value='20'>20 Years old</option>
                                    <option value='20'>20+ Years old</option>
                                </select>

                                <button onClick={onSubmitHandler}
                                        className='w-full mt-5 self-center rounded-md bg-rose hover:bg-rose-dark font-bold transition-all duration-300 shadow-[rgba(255,0,131,0.5)_0px_10px_40px_-10px] p-3.5 text-white'>GET
                                    YOUR QUOTE
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </main>

            <footer>
                <Footer/>
            </footer>
        </div>
    )
}

export default PetOnlyRegistration