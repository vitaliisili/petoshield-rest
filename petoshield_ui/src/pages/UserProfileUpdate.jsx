import React, {useEffect, useState} from 'react';
import {toast, ToastContainer} from "react-toastify";
import NavBar from "../components/NavBar";
import HelpModal from "../components/HelpModal";
import Footer from "../components/Footer";
import axios from "axios";
import {API_USER_CHANGE_PASSWORD, API_USER_SELF, API_USER_URL} from "../utils/apiUrls";
import {getCookie} from "../utils/cookiesUtils";
import houses from "../static/images/boy-and-bike.svg";
import ConfirmModal from "../components/ConfirmModal";
import {FaRegEye, FaRegEyeSlash} from "react-icons/fa";

const UserProfileUpdate = () => {

    const [profile, setProfile] = useState(null)

    const [name, setName] = useState('')
    const [email, setEmail] = useState('')
    const [image, setImage] = useState(null)

    const [oldPassword, setOldPassword] = useState('')
    const [newPassword, setNewPassword] = useState('')
    const [verifyNewPassword, setVerifyNewPassword] = useState('')

    const [deleteModal, setDeleteModal] = useState(false)
    const [isHidden, setIsHidden] = useState(true)

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

    const changePasswordHandler = () => {
        const id = toast.loading('Please Wait...')
        if (newPassword !== verifyNewPassword) {
            toast.update(id, {render: 'new password and verify password not equal', type: "error", isLoading: false, autoClose: 5000})
            return
        }

        axios.post(API_USER_CHANGE_PASSWORD, {
            'old_password': oldPassword,
            'new_password': newPassword
        }, {
            headers: {
                'Authorization': `Bearer ${getCookie('accessToken')}`
            }
        }).then(response => {
            if (response.status === 200) {
                toast.update(id, {render: 'Success', type: "success", isLoading: false, autoClose: 2000})
                setNewPassword('')
                setOldPassword('')
                setVerifyNewPassword('')
            }
        }).catch(error => {
            if (error.response.data.errors) {
                toast.update(id, {render: error.response.data.errors[0].detail, type: "error", isLoading: false, autoClose: 5000})
            }else{
                toast.update(id, {render: 'Server error please contact administrator', type: "error", isLoading: false, autoClose: 5000})
            }
        })

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
                'Authorization': `Bearer ${getCookie('accessToken')}`,
                'Content-Type': 'multipart/form-data'
            }
        }).then(response => {
            if (response.status === 200) {
                toast.update(id, {render: 'Success', type: "success", isLoading: false, autoClose: 2000})
            }
        }).catch(error => {
            if (error.response.data.errors) {
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
            {profile && <ConfirmModal type='user' object={profile} toggle={deleteModal} callback={() => setDeleteModal(false)}/>}

            <main className='flex flex-grow flex-col pt-28 items-center font-lato relative z-20'>
                <div className='flex flex-col items-center justify-end w-full h-full z-10 absolute overflow-hidden '>
                    <img className='min-w-[1200px] xl:min-w-[2000px] mb-28 opacity-10' src={houses} alt="bg"/>
                </div>

                <section className='z-50 bg-white mb-20 flex space-x-8'>
                    <div className='shadow-xl rounded-md p-8'>
                        { profile &&
                            <div className='space-y-8'>
                                <div className='flex flex-col space-y-4'>
                                    <label className="block mb-1 text-xl text-nobel-dark" htmlFor="file_input">Upload profile image</label>
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

                    <div className='p-8 bg-white shadow-xl'>
                        <div className='flex flex-col space-y-4 min-w-[300px]'>
                            <div className='text-nobel-dark text-xl'>Change password</div>
                            <div className='flex flex-col relative justify-center'>
                                <input onChange={(e) => setOldPassword(e.target.value)} value={oldPassword} type={isHidden ? "password" : "text"} className='input-focus p-3 outline-0 border border-gallery rounded-md focus:border-gallery focus:ring-0' placeholder='Old password'/>
                                {isHidden ?
                                    <FaRegEyeSlash className='text-2xl absolute right-4'  onClick={() => setIsHidden(!isHidden)}/> :
                                    <FaRegEye className='text-2xl absolute right-4' onClick={() => setIsHidden(!isHidden)}/>}
                            </div>
                            <div className='flex flex-col relative justify-center'>
                                <input onChange={(e) => setNewPassword(e.target.value)} value={newPassword} type={isHidden ? "password" : "text"} className='input-focus p-3 outline-0 border border-gallery rounded-md focus:border-gallery focus:ring-0' placeholder='New password'/>
                                {isHidden ?
                                    <FaRegEyeSlash className='text-2xl absolute right-4'  onClick={() => setIsHidden(!isHidden)}/> :
                                    <FaRegEye className='text-2xl absolute right-4' onClick={() => setIsHidden(!isHidden)}/>}
                            </div>
                            <div className='flex flex-col relative justify-center'>
                                <input onChange={(e) => setVerifyNewPassword(e.target.value)} value={verifyNewPassword} type={isHidden ? "password" : "text"} className='input-focus p-3 outline-0 border border-gallery rounded-md focus:border-gallery focus:ring-0' placeholder='Verify new password'/>
                                {isHidden ?
                                    <FaRegEyeSlash className='text-2xl absolute right-4'  onClick={() => setIsHidden(!isHidden)}/> :
                                    <FaRegEye className='text-2xl absolute right-4' onClick={() => setIsHidden(!isHidden)}/>}
                            </div>
                            <button onClick={changePasswordHandler} className='w-full self-end rounded-md bg-rose hover:bg-rose-dark font-bold transition-all duration-300 shadow-[rgba(255,0,131,0.5)_0px_10px_40px_-10px] px-4 py-3 text-white'>Change password</button>
                        </div>

                        <div className='flex flex-col'>
                            <div className='text-nobel-dark text-xl mt-12'>Danger zone</div>
                            <button onClick={() => setDeleteModal(true)} className='mt-5 w-full self-end rounded-md bg-rose hover:bg-rose-dark font-bold transition-all duration-300 shadow-[rgba(255,0,131,0.5)_0px_10px_40px_-10px] px-4 py-3 text-white'>Remove Account</button>
                        </div>
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