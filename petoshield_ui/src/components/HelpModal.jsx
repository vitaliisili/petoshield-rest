import React, {useEffect, useState} from 'react'
import {FiHelpCircle} from "react-icons/fi"
import {AiOutlineClose} from "react-icons/ai";

const HelpModal = () => {

    const [modal, setModal] = useState(false)
    const [isDisabled, setIsDisabled] = useState(true)
    const [fullName, setFullName] = useState('')
    const [email, setEmail] = useState('')
    const [message, setMessage] = useState('')

    useEffect(() => {
        document.body.style.overflow = modal ? 'hidden' : 'unset'
    }, [modal])

    useEffect(() => {
        setIsDisabled(!(fullName && email && message))
    }, [fullName, email, message])

    const sendForm = () => {
    //    Todo: Validate and Send form then empty all fields
        setFullName('')
        setEmail('')
        setMessage('')
        setModal(false)
    }

    const handleModal = (e) => {
        if (e.target.id === 'help-modal') {
            setModal(false)
        }
    }

    return (
        <div className=''>
            {modal &&
                <div id='help-modal' onClick={(e) => handleModal(e)} className='fixed bg-gallery-transparent w-screen h-screen z-50 top-0 flex justify-center items-center'>
                    <div className='flex flex-col relative bg-white rounded-[5px] p-10 pl-16 pr-16 items-center'>
                        <button onClick={() => setModal(false)} className='absolute top-2 right-2 z-50 transition-all duration-500 hover:scale-110'><AiOutlineClose/></button>
                        <h2 className='uppercase font-bold'>ask us anything</h2>
                        <div className='flex flex-col space-y-5 mt-10'>
                            <input onChange={(e) => setFullName(e.target.value)} value={fullName} type="text" className='border border-gallery-dark  rounded-[3px] outline-0 p-3' placeholder='FULL NAME'/>
                            <input onChange={(e) => setEmail(e.target.value)} value={email} type="email" className='border border-gallery-dark  rounded-[3px] outline-0 p-3' placeholder='EMAIL ADDRESS'/>
                            <textarea onChange={(e) => setMessage(e.target.value)} value={message} name="message" id="message" cols="30" rows="2" className='border border-gallery-dark  rounded-[3px] outline-0 p-3' placeholder='HOW CAN WE HELP?'></textarea>
                            <button onClick={sendForm} className={`p-2 pl-8 pr-8 rounded-md font-bold font-lato w-fit self-center uppercase text-white transition-all duration-300 ${isDisabled ? 'bg-gallery': 'bg-rose hover:bg-rose-dark shadow-[rgba(255,0,131,0.5)_0px_10px_40px_-10px]'}`} disabled={isDisabled}>Send</button>
                        </div>
                    </div>
                </div>
            }
            <button onClick={() => setModal(true)} className='fixed z-40 bottom-3 right-3 rounded-full p-3 pl-6 pr-6 flex justify-center items-center text-white bg-rose font-merriweather'><FiHelpCircle/><span className='ml-2 mt-[-1px]'>Help</span></button>
        </div>
    )
}

export default HelpModal