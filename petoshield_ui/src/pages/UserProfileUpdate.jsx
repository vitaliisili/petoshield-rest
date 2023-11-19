import React, {useEffect, useState} from 'react';
import {toast, ToastContainer} from "react-toastify";
import NavBar from "../components/NavBar";
import HelpModal from "../components/HelpModal";
import Footer from "../components/Footer";
import axios from "axios";
import {API_USER_SELF, API_USER_URL} from "../utils/apiUrls";
import {getCookie} from "../utils/cookiesUtils";
import houses from "../static/images/boy-and-bike.svg";

const UserProfileUpdate = () => {

    const [profile, setProfile] = useState(null)

    const [name, setName] = useState('')
    const [email, setEmail] = useState('')
    const [image, setImage] = useState(null)

    useEffect(() => {
        const id = toast.loading('Please Wait...')
        axios.get(API_USER_SELF, {
            headers: {
                'Authorization': `Bearer ${getCookie('accessToken')}`
            }
        }).then(response => {
            if (response.status === 200) {
                console.log(response.data)
                setProfile(response.data)
                setName(response.data.name)
                setEmail(response.data.email)
                toast.update(id, {render: 'Success', type: "success", isLoading: false, autoClose: 2000})
            }
        }).catch(error => {
            if (error.response) {
                toast.update(id, {render: error.response.data.errors[0].detail, type: "error", isLoading: false, autoClose: 5000})
            }else{
                toast.update(id, {render: 'Server error please contact administrator', type: "error", isLoading: false, autoClose: 5000})
            }
        })
    }, [])

    const getFileInfo = (file) => {
        if (file.target.files[0]) {
            const formData = new FormData()
            formData.append('profileImage', file.target.files[0], file.target.files[0].name)
            setImage(formData)
        }
    }
    const updateProfileHandler = () => {
        const id = toast.loading('Please Wait...')

        let data = {
            name,
            email
        }

        if (image) {
            data['image'] = image
        }

        axios.patch(`${API_USER_URL}${profile.id}/`, data, {
            headers: {
                'Authorization': `Bearer ${getCookie('accessToken')}`
            }
        }).then(response => {
            if (response.status === 200) {
                toast.update(id, {render: 'Success', type: "success", isLoading: false, autoClose: 2000})
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
        <div className='text-black flex flex-col h-screen'>
            <ToastContainer/>
            <NavBar/>
            <HelpModal/>

            <main className='flex flex-grow flex-col pt-28 items-center font-lato relative z-20'>
                <div className='flex flex-col items-center justify-end w-full h-full z-10 absolute overflow-hidden '>
                    <img className='min-w-[1200px] xl:min-w-[2000px] mb-28 opacity-10' src={houses} alt="bg"/>
                </div>

                <section className='z-50'>
                    <div className='shadow-xl rounded-md p-4'>
                        { profile &&
                            <div className='space-y-8'>
                                <div className='flex flex-col space-y-4'>
                                    <label className="block mb-1 text-xl text-nobel-dark" htmlFor="file_input">Upload profile image</label>
                                    {/*<input onChange={getFileInfo} className="file:bg-rose file:h-full file:outline-0 file:ring-0 file:border-0 file:text-white file:p-3 file:cursor-pointer file:font-bold file:rounded-l-md block w-full text-sm text-black border border-gallery rounded-md cursor-pointer focus:outline-none" id="file_input" type="file"/>*/}
                                    <input onChange={(e) => setImage(e.target.files[0])} className="file:bg-rose file:h-full file:outline-0 file:ring-0 file:border-0 file:text-white file:p-3 file:cursor-pointer file:font-bold file:rounded-l-md block w-full text-sm text-black border border-gallery rounded-md cursor-pointer focus:outline-none" id="file_input" type="file"/>
                                </div>

                                <div className='flex flex-col space-y-4'>
                                    <label className="block mb-1 text-xl text-nobel-dark" htmlFor="update-name">Full name</label>
                                    <input onChange={(e) => setName(e.target.value)} value={name} type="text" id='update-name' className='input-focus p-3 outline-0 border border-gallery rounded-md focus:border-gallery focus:ring-0' placeholder='Full Name'/>
                                </div>

                                <div className='flex flex-col space-y-4'>
                                    <label className="block mb-1 text-xl text-nobel-dark" htmlFor="update-email">Email address</label>
                                    <input onChange={(e) => setEmail(e.target.value)} value={email} type="email" id='update-email' className='input-focus p-3 outline-0 border border-gallery rounded-md focus:border-gallery focus:ring-0' placeholder='Email'/>
                                </div>

                                <button onClick={updateProfileHandler} className='w-full self-end rounded-md bg-rose hover:bg-rose-dark font-bold transition-all duration-300 shadow-[rgba(255,0,131,0.5)_0px_10px_40px_-10px] px-4 py-3 text-white'>Save changes</button>

                            </div>
                        }
                    </div>
                </section>
            </main>

            <footer className='z-30'>
                <Footer/>
            </footer>
        </div>
    );
};

export default UserProfileUpdate;