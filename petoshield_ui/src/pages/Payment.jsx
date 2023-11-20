import React, {useEffect, useState} from 'react';
import {Link, useLocation, useNavigate} from "react-router-dom";
import QueryString from 'query-string'
import axios from "axios";
import {API_PAYMENT_CHECKOUT_CONFIRM} from "../utils/apiUrls";
import {getCookie} from "../utils/cookiesUtils";
import {toast, ToastContainer} from "react-toastify";
import NavBar from "../components/NavBar";
import HelpModal from "../components/HelpModal";
import Footer from "../components/Footer";
import catDog from "../static/images/payment/dog-cat.png"
import click from "../static/images/payment/click.gif"

const Payment = () => {

    const navigate = useNavigate()
    const location = useLocation()
    const query_option = QueryString.parse(location.search)
    const [status, setStatus] = useState(null)

    useEffect(() => {
        if (query_option.success) {
            setStatus('success')

            axios.post(API_PAYMENT_CHECKOUT_CONFIRM, {
                'session_id': query_option.session_id
            }, {
                headers: {
                    'Authorization': `Bearer ${getCookie('accessToken')}`
                }
            }).then(response => {
                if (response.status === 200) {
                    console.log(response.data)
                }
            }).catch(error => {
                console.log(error)
            })
        }else if (query_option.cancel) {
            setStatus('cancel')
        }else {
            navigate('/account')
        }
    }, [])

    return (
        <div className='text-black flex flex-col h-screen'>
            <ToastContainer/>
            <NavBar/>
            <HelpModal/>

            <main className={`flex flex-grow flex-col pt-28 items-center font-lato ${status && status === "success" ? "bg-white" : "bg-lilac"}`}>
                {
                    status && status === 'success' ?
                        <div className='flex flex-col bg-white rounded-md p-8 text-center justify-center items-center'>
                            <div className='font-bold font-dancing text-[60px] flex justify-center text-rose text-center'>Thank You For Your Order</div>
                            <div className='mt-16'>
                                <img src={catDog} alt="cad-dog" className='w-[500px]'/>
                            </div>
                            <button onClick={() => navigate('/account')} className='w-80 lg:w-96 mt-5 self-center rounded-md bg-rose hover:bg-rose-dark font-bold transition-all duration-300 shadow-[rgba(255,0,131,0.5)_0px_10px_40px_-10px] p-3.5 text-white'>Go To My Account</button>
                        </div>
                        :
                        <div className=' flex flex-col bg-lilac rounded-md h-full justify-end'>
                            <div className='-mb-20 z-10'>
                                <div className='font-bold font-dancing text-[60px] flex justify-center text-rose text-center'>Your payment has failed</div>
                                <div className='font-bold font-lato text-nobel text-2xl flex justify-center mt-4'>Please try again</div>
                            </div>

                            <div className=''>
                                <Link to='/account'><img src={click} alt="click"/></Link>
                            </div>
                        </div>
                }
            </main>

            <footer>
                <Footer/>
            </footer>
        </div>
    );
};

export default Payment;