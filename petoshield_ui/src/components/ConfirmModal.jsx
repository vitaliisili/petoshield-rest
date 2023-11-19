import React, {Fragment, useEffect, useState} from 'react'
import {AiOutlineClose} from "react-icons/ai";
import {IoWarningOutline} from "react-icons/io5";
import axios from "axios";
import {API_PETS_URL} from "../utils/apiUrls";
import {getCookie} from "../utils/cookiesUtils";
import {toast} from "react-toastify";
import {useNavigate} from "react-router-dom";

const ConfirmModal = ({type, object, toggle, callback}) => {
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
        axios.delete(`${API_PETS_URL}${object.id}/`, {
            headers: {
                'Authorization': `Bearer ${getCookie('accessToken')}`
            }
        }).then(response => {
            if (response.status === 204) {
                toast.update(id, {render: 'Pet has been deleted', type: "success", isLoading: false, autoClose: 5000})
                setTimeout(() => {
                    navigate('/account')
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

                            { type && type === 'pet' ?
                                <div className='w-96 font-lato ml-4'>
                                    Are you sure you want to remove your pet? All pet data will be permanently removed
                                    from our servers forever. This action cannot be undone.
                                </div> :
                                <div className='w-96 font-lato ml-4'>
                                    Are you sure you want to deactivate your account? All of your data will be permanently removed
                                    from our servers forever. This action cannot be undone.
                                </div>
                            }
                        </div>

                        <div className=' flex w-full mt-4 justify-end items-end space-x-4'>
                            <button onClick={closeModal} className='rounded-md bg-rose hover:bg-rose-dark font-bold transition-all duration-300 shadow-[rgba(255,0,131,0.5)_0px_10px_40px_-10px]  py-1 px-4 text-white'>Cancel</button>
                            <button onClick={removeHandler} className='rounded-md bg-rose hover:bg-rose-dark font-bold transition-all duration-300 shadow-[rgba(255,0,131,0.5)_0px_10px_40px_-10px]  py-1 px-4 text-white'>Remove</button>

                        </div>
                    </div>
                </div>
            }
        </div>
    )
}

export default ConfirmModal

