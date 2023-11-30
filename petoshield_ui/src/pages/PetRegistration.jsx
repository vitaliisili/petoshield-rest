import React, {useEffect, useState} from 'react';
import HelpModal from "../components/HelpModal";
import NavBar from "../components/NavBar";
import Footer from "../components/Footer";
import {Link, useLocation, useNavigate} from "react-router-dom";
import {API_BREEDS_URL, API_PETS_CREATE_WITH_USER_URL} from "../utils/apiUrls";
import axios from "axios";
import {getCookie, setCookie} from "../utils/cookiesUtils";
import {toast, ToastContainer} from "react-toastify";
import {FaRegEye, FaRegEyeSlash} from "react-icons/fa";
import TermsModal from "../components/TermsModal";
import PrivacyPolicyModal from "../components/PrivacyPolicyModal";

const PetRegistration = () => {
    const location = useLocation()
    const navigate = useNavigate()
    const [termsModalEnable, setTermsModalEnable] = useState(false)
    const [policyModalEnable, setPolicyModalEnable] = useState(false)
    const [isHidden, setIsHidden] = useState(true)

    const [petName, setPetName] = useState('')
    const [petAge, setPetAge] = useState('')
    const [petGender, setPetGender] = useState('F')
    const [petSpecies, setPetSpecies] = useState('')
    const [petBreed, setPetBreed] = useState('')

    const [firstName, setFirstName] = useState('')
    const [lastName, setLastName] = useState('')
    const [userEmail, setUserEmail] = useState('')
    const [userPassword, setUserPassword] = useState('')
    const [userVerifyPassword, setUserVerifyPassword] = useState('')

    const [breeds, setBreeds] = useState([])

    useEffect(() => {
        if (getCookie('accessToken')) {
            navigate('/new-pet')
        }

        if (location.state) {
            setPetSpecies(location.state.type)
        } else {
            navigate('/price')
        }


        if(petSpecies) {
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
        }
    }, [petSpecies]);

    const onSubmitHandler = () => {
        const id = toast.loading('Please Wait...')
        if (userPassword !== userVerifyPassword){
            toast.update(id, {render: 'Password and verify password not equals', type: "error", isLoading: false, autoClose: 7000})
            return
        }

        axios.post(API_PETS_CREATE_WITH_USER_URL, {
                pet: {
                    "name": petName,
                    "age": petAge,
                    "gender": petGender,
                    "species": petSpecies,
                    "breed": petBreed
                },
                user: {
                    "email": userEmail,
                    "name": `${firstName} ${lastName}`,
                    "password": userPassword
                }
        }).then(response => {
            if (response.status === 201){
                setCookie('accessToken', response.data.access)
                setCookie('refreshToken', response.data.refresh)
                toast.update(id, {render: 'Success', type: "success", isLoading: false, autoClose: 1000})
                setTimeout(()=> {
                    navigate(`/pet-quote/${response.data.pet}`)
                }, 1000)
            }
        }).catch(error => {
            if (error.response) {
                toast.update(id, {render: error.response.data.errors[0].detail, type: "error", isLoading: false, autoClose: 5000})
            }else{
                toast.update(id, {render: 'Server error please contact administrator', type: "error", isLoading: false, autoClose: 5000})
            }
        })
    }

    const keyPressedHandler = (e) => {
        if (e.code === 'Enter') {
            onSubmitHandler()
        }
    }
    const closeModal = () => {
        setTermsModalEnable(false)
        setPolicyModalEnable(false)
    }
    return (
        <div className='text-black flex flex-col h-screen'>
            <ToastContainer/>
            <HelpModal/>
            <NavBar/>
            {termsModalEnable && <TermsModal callback={closeModal}/>}
            {policyModalEnable && <PrivacyPolicyModal callback={closeModal}/>}

            <main className='flex-grow pt-44 flex justify-center items-center pb-28 px-4 font-lato text-black bg-black-haze'>
                <div className='flex flex-col'>
                    <div className='flex flex-col lg:flex-row'>
                        <div className='pet w-80 p-4 self-center lg:self-start'>
                            <div className='font-bold text-2xl text-center'>Pet Information</div>

                            <div className='flex flex-col space-y-8 mt-8'>
                                <input onChange={(e) => setPetName(e.target.value)} value={petName} type="text"
                                       className='outline-0 p-3 border border-gallery rounded-md focus:ring-1 focus:ring-rose shadow-sm focus:border-rose'
                                       placeholder='Pet Name'/>
                                <div className='flex justify-around'>
                                    <div className='flex justify-center items-center p-3'>
                                        <input onChange={(e) => setPetGender(e.target.value)}
                                               checked={petGender === 'F'}
                                               className='w-4 h-4 focus:ring-0 text-rose' type="radio" id='pet-gender-f'
                                               value='F' name='pet-gender'/>
                                        <label htmlFor="pet-gender-f" className='ml-1'>Female</label>
                                    </div>

                                    <div className='flex justify-center items-center p-3'>
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
                            </div>
                        </div>

                        <div className='user rounded-md p-4 ml-0 lg:ml-8'>
                            <div className='text-2xl font-bold text-center'>Owner Information</div>
                            <div className='form flex flex-col space-y-8 mt-8 w-80 lg:w-full'>
                                <div className='flex flex-col lg:flex-row justify-start lg:justify-between space-y-8 lg:space-y-0'>
                                    <input onChange={(e) => setFirstName(e.target.value)} value={firstName} type="text"
                                           className='outline-0 p-3 border border-gallery rounded-md focus:ring-1 focus:ring-rose shadow-sm focus:border-rose'
                                           placeholder='First Name'/>
                                    <input onChange={(e) => setLastName(e.target.value)} value={lastName} type="text"
                                           className='outline-0 p-3 border border-gallery rounded-md ml-0 lg:ml-8 focus:ring-1 focus:ring-rose shadow-sm focus:border-rose'
                                           placeholder='Last Name'/>
                                </div>
                                <input onChange={(e) => setUserEmail(e.target.value)} value={userEmail} type="email"
                                       className='outline-0 p-3 border border-gallery rounded-md focus:ring-1 focus:ring-rose shadow-sm focus:border-rose'
                                       placeholder='Email Adress'/>

                                <div className='flex flex-col relative justify-center'>
                                    <input onChange={(e) => setUserPassword(e.target.value)} value={userPassword} type={isHidden ? "password" : "text"} id='user-password' className=' w-full input-focus p-3.5 outline-0 border border-gallery rounded-md focus:border-gallery focus:ring-0' placeholder='Password'/>
                                    {isHidden ?
                                        <FaRegEyeSlash className='text-2xl absolute right-4'  onClick={() => setIsHidden(!isHidden)}/> :
                                        <FaRegEye className='text-2xl absolute right-4' onClick={() => setIsHidden(!isHidden)}/>}
                                </div>

                                <div onKeyDown={keyPressedHandler} className='flex flex-col relative justify-center'>
                                    <input onChange={(e) => setUserVerifyPassword(e.target.value)} value={userVerifyPassword} type={isHidden ? "password" : "text"} id='user-verify-password' className=' w-full input-focus p-3.5 outline-0 border border-gallery rounded-md focus:border-gallery focus:ring-0' placeholder='Verify password'/>
                                    {isHidden ?
                                        <FaRegEyeSlash className='text-2xl absolute right-4'  onClick={() => setIsHidden(!isHidden)}/> :
                                        <FaRegEye className='text-2xl absolute right-4' onClick={() => setIsHidden(!isHidden)}/>}
                                </div>
                            </div>
                        </div>
                    </div>
                    <div className='text-sm text-center text-nobel-dark'>
                        To click button bellow you are agree with <span onClick={() => setTermsModalEnable(true)} className='text-rose cursor-pointer'>Terms</span> and <span onClick={() => setPolicyModalEnable(true)} className='text-rose cursor-pointer'>Privacy Policy</span>
                    </div>
                    <button onClick={onSubmitHandler}
                            className='w-80 lg:w-96 mt-5 self-center rounded-md bg-rose hover:bg-rose-dark font-bold transition-all duration-300 shadow-[rgba(255,0,131,0.5)_0px_10px_40px_-10px] p-3.5 text-white'>GET YOUR QUOTE
                    </button>
                </div>


            </main>

            <footer>
                <Footer/>
            </footer>
        </div>
    )
}

export default PetRegistration