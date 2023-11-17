import React, {useEffect, useState} from 'react';
import NavBar from "../components/NavBar";
import HelpModal from "../components/HelpModal";
import Footer from "../components/Footer";
import axios from "axios";
import {API_PAYMENT_CHECKOUT, API_PETS_URL} from "../utils/apiUrls";
import {getCookie} from "../utils/cookiesUtils";
import {useLocation, useNavigate, useParams} from "react-router-dom";
import catIcon from "../static/images/account/cat-icon.svg"
import dogIcon from "../static/images/account/dog-icon.svg"
import {BsCurrencyEuro} from "react-icons/bs";
import {ANNUAL_DISCOUNT, PAYMENT_REDIRECT_LINK} from "../utils/config";

const Quote = () => {
    const navigate = useNavigate()
    const [pet, setPet] = useState(null)
    const params = useParams()
    const [frequency, setFrequency] = useState('annual')
    const [discount, setDiscount] = useState(0)
    const [price, setPrice] = useState(0)
    const [finalPrice, setFinalPrice] = useState(0)

    useEffect(() => {
        axios.get(`${API_PETS_URL}${params.id}`, {
            headers: {
                'Authorization': `Bearer ${getCookie('accessToken')}`
            }
        }).then(response => {
            if (response.status === 200) {
                setPet(response.data)
            }
        }).catch(error => {
            console.log(error)
        })
    }, [])

    useEffect(() => {
        if (pet) {
            const monthly_price = pet.policy.price
            setPrice(frequency === 'annual' ? (monthly_price * 12).toFixed(2) : monthly_price)
            setDiscount(frequency === 'annual' ? ANNUAL_DISCOUNT : 0)
            setFinalPrice(frequency === 'annual' ? (price - discount).toFixed(2) : monthly_price)
        }
    }, [frequency, pet, finalPrice, price])

    const paymentHandler = () => {
        axios.post(API_PAYMENT_CHECKOUT, {
            frequency,
            "final_price": parseFloat(finalPrice).toFixed(2),
            'pet': pet.id,
            'redirect_link': PAYMENT_REDIRECT_LINK
        },{
            headers: {
                'Authorization': `Bearer ${getCookie('accessToken')}`
            }
        }).then(response => {
            if (response.status === 200) {
                // console.log(response.data)
                window.location.replace(response.data.checkout_url)
            }
        }).catch(error => {
            console.log(error)
        })
    }

    return (
        <div className='text-black h-screen flex flex-col'>
            <NavBar/>
            <HelpModal/>

            <main className='flex flex-grow pt-28 pb-16 justify-center items-center bg-black-haze font-lato'>
                <div className='flex flex-col md:flex-row justify-center px-4'>
                    <div className='bg-white rounded-md p-8 shadow-md h-fit'>
                        {pet &&
                            <div className="flex flex-col">
                                <div className='flex justify-start items-center'>
                                    <div className='flex justify-center items-center'>
                                        {pet.species === 'cat' ? <img src={catIcon} alt="cat"/> :
                                            <img src={dogIcon} alt="dog"/>}
                                    </div>

                                    <div className='text-2xl ml-3'>{pet.name}</div>
                                </div>

                                <div className='flex font-bold mt-3'>
                                    {pet.gender === 'F' ? 'Female' : 'Male'} <span
                                    className='text-rose px-2'>|</span> {pet.breed} <span
                                    className='text-rose px-2'>|</span> {pet.age} years old
                                </div>
                                <div className='flex space-x-8 mt-8'>
                                    <div>
                                        <div className='font-bold'>Coverage:</div>
                                        <div className='flex items-center text-sm'>Annual
                                            Coverage: {pet.policy.initial_limit} <BsCurrencyEuro/></div>
                                        <div className='flex items-center text-sm'>Deductible: {pet.policy.deductible}
                                            <BsCurrencyEuro/></div>
                                        <div className='flex items-center text-sm'>Giveback: 80%</div>
                                    </div>

                                    <div>
                                        <div className='font-bold'>Insurance Period:</div>
                                        <div className='flex items-center text-sm'>Start date: {pet.policy.start_date}</div>
                                        <div className='flex items-center text-sm'>End date: {pet.policy.end_date}</div>
                                    </div>
                                </div>


                            </div>
                        }
                    </div>

                    <div className='flex flex-col bg-white p-8 mt-8 w-full md:mt-0 md:ml-8 rounded-md shadow-md h-fit md:w-80'>
                        {pet &&
                            <div className=''>
                                <div className='font-bold'>Payment Frequency:</div>
                                <div className='text-xs text-nobel-dark'>Pay annually and save up to $24/yr</div>
                                <select onChange={(e) => setFrequency(e.target.value)}
                                        className='w-full rounded-md mt-4 border border-gallery focus:ring-0 focus:border-nobel'
                                        name="frequency" id="frequency">
                                    <option value='annual'>Annual</option>
                                    <option value='monthly'>Monthly</option>
                                </select>

                                <div className='font-bold mt-8'>Plan:</div>
                                <div className='flex items-center mt-2 justify-between'>
                                    <div className='flex items-center'>
                                        <img className='w-5 h-5' src={pet.species === 'cat' ? catIcon : dogIcon} alt="pet"/>
                                        <div className='ml-2'>{pet.name}</div>
                                    </div>

                                    <div className=''>
                                        {price &&
                                            <div className='flex items-center'>
                                                <BsCurrencyEuro/> <span className='font-bold'>{price}</span>
                                            </div>
                                        }
                                    </div>
                                </div>

                                {finalPrice &&
                                    <div>
                                        <div className='flex justify-between mt-4'>
                                            <div>Discount</div>
                                            <div className='flex items-center text-rose'>
                                                - <BsCurrencyEuro/> <span className='font-bold '>{discount}</span>
                                            </div>
                                        </div>

                                        <div className='h-[1px] bg-nobel mt-4'></div>

                                        <div className='flex justify-between mt-4'>
                                            <div className='font-bold'>{frequency === 'annual' ? 'Annual ' : 'Monthly '} total: </div>
                                            <div className='flex items-center'><BsCurrencyEuro/> <span className='font-bold'>{finalPrice}</span></div>
                                        </div>



                                        <button onClick={paymentHandler} className='mt-8 rounded-md bg-rose hover:bg-rose-dark font-bold transition-all duration-300 shadow-[rgba(255,0,131,0.5)_0px_10px_40px_-10px] w-full p-3.5 text-white'>SUBMIT PAYMENT</button>
                                    </div>
                                }
                            </div>
                        }
                    </div>
                </div>

            </main>

            <footer>
                <Footer/>
            </footer>
        </div>
    );
};

export default Quote;