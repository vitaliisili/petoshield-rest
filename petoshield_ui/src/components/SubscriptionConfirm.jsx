import React, {useEffect, useState} from 'react';
import {useNavigate} from "react-router-dom";
import {toast} from "react-toastify";
import axios from "axios";
import {API_PAYMENT_CANCEL_SUBSCRIPTION, API_PETS_URL} from "../utils/apiUrls";
import {getCookie} from "../utils/cookiesUtils";
import {AiOutlineClose} from "react-icons/ai";
import {IoWarningOutline} from "react-icons/io5";

const SubscriptionConfirm = ({callback, toggle, object}) => {
    const [modal, setModal] = useState(false)
    const navigate = useNavigate()

    useEffect(() => {
        document.body.style.overflow = modal ? 'hidden' : 'unset'
        setModal(toggle)

    }, [modal, toggle])

    const handleModal = (e) => {
        if (e.target.id === 'confirm-modal') {
            callback()
            setModal(false)
        }
    }

    const closeModal = () => {
        callback()
        setModal(false)
    }

    const removeHandler = () => {
        const id = toast.loading('Please Wait...')
        axios.post(API_PAYMENT_CANCEL_SUBSCRIPTION, {
            'policy': object.id
        }, {
            headers: {
                'Authorization': `Bearer ${getCookie('accessToken')}`
            }
        }).then(response => {
            if (response.status === 200) {
                toast.update(id, {render: 'Subscription was canceled', type: "success", isLoading: false, autoClose: 5000})
                setModal(false)
                setTimeout(() => {
                    navigate('/account')
                }, 2000)
            }
        }).catch(error => {
            if (error.response) {
                toast.update(id, {render: error.response.data.errors[0].detail, type: "error", isLoading: false, autoClose: 5000})
            }else{
                toast.update(id, {render: 'Server error please contact administrator', type: "error", isLoading: false, autoClose: 5000})
            }
        })
    }

    return (
        <div className=''>
            {modal &&
                <div id='confirm-modal' onClick={(e) => handleModal(e)} className='fixed bg-gallery-transparent w-screen h-screen z-50 top-0 flex justify-center items-center'>
                    <div className='flex flex-col relative bg-white rounded-[5px] p-8 items-center'>
                        <button onClick={closeModal} className='absolute top-2 right-2 z-50 transition-all duration-500 hover:scale-110'><AiOutlineClose/></button>
                        <div className='flex'>
                            <div>
                                <IoWarningOutline className='text-rose text-4xl'/>
                            </div>
                                <div className='w-96 font-lato ml-4'>
                                    Are you sure you want to unsubscribe your pet? This action cannot be undone.
                                </div>
                        </div>

                        <div className=' flex w-full mt-4 justify-end items-end space-x-4'>
                            <button onClick={closeModal} className='rounded-md bg-rose hover:bg-rose-dark font-bold transition-all duration-300 shadow-[rgba(255,0,131,0.5)_0px_10px_40px_-10px]  py-1 px-4 text-white'>Cancel</button>
                            <button onClick={removeHandler} className='rounded-md bg-rose hover:bg-rose-dark font-bold transition-all duration-300 shadow-[rgba(255,0,131,0.5)_0px_10px_40px_-10px]  py-1 px-4 text-white'>Unsubscribe</button>
                        </div>
                    </div>
                </div>
            }
        </div>
    )
};

export default SubscriptionConfirm;