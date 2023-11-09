import React, {useEffect, useState} from 'react';
import NavBar from "../components/NavBar";
import HelpModal from "../components/HelpModal";
import Footer from "../components/Footer";
import partnerPlant from "../static/images/partner/partner-plant.png"
import partnerContent from "../static/images/partner/partner-content.png"
import partnerInf from "../static/images/partner/partner-inf.png"
import partnerMedia from "../static/images/partner/partner-media.png"
import partnerBrand from "../static/images/partner/partner-brand.png"

const Partners = () => {

    const [isDisabled, setIsDisabled] = useState(true)
    const [name, setName] = useState('')
    const [businessName, setBusinessName] = useState('')
    const [email, setEmail] = useState('')
    const [type, setType] = useState('')
    const [message, setMessage] = useState('')
    const [url, setUrl] = useState('')

    useEffect(() => {
        setIsDisabled(!(name && email && message && type && url && businessName))
    }, [name, email, message, type, url, businessName])

    const sendForm = () => {
        // TODO: add logic to send form
    }

    return (
        <div className='text-black'>
            <HelpModal/>
            <NavBar/>

            <main className='pt-20 lg:pt-28'>
                <section className='flex flex-col justify-center items-center px-4 py-12 container mx-auto'>
                    <h1 className='text-[30px] md:text-[40px] lg:text-[54px] font-merriweather text-center'>
                        Hey there, partner! <br/>
                        Let’s grow together.
                    </h1>

                    <p className='text-center max-w-[560px] mt-8 font-lato text-xl'>
                        Tell the world about the most loved insurance product out there,
                        while earning money and creating real social impact.
                    </p>

                    <a href={'#form-business'}><button className='rounded-md bg-rose hover:bg-rose-dark font-bold transition-all duration-300 shadow-[rgba(255,0,131,0.5)_0px_10px_40px_-10px] w-full py-3.5 px-16 text-white max-w-fit mt-12'>APPLY NOW</button></a>

                    <img className='-mt-16 md:-mt-24 lg:-mt-32 xl:-mt-60 -z-10' src={partnerPlant} alt="plant"/>
                </section>

                <section className='flex flex-col justify-center items-center px-4 py-12 container mx-auto'>
                    <h2 className='text-[40px] font-bold font-lato'>Who is this for?</h2>
                    <div className='flex flex-col lg:flex-row items-center w-full justify-around mt-16'>

                        <div className='flex flex-col justify-center items-center'>
                            <img className='w-16 h-16' src={partnerContent} alt="content"/>
                            <h3 className='text-center text-2xl font-lato font-bold mt-3'>Content Curators</h3>
                            <p className='text-center max-w-[400px] mt-3'>Have a high traffic blog or website readers love? Earn money for every Petoshield user.</p>
                        </div>

                        <div className='flex flex-col justify-center items-center mt-16 lg:mt-0'>
                            <img className=' h-16' src={partnerInf} alt="influencer"/>
                            <h3 className='text-center text-2xl font-lato font-bold mt-2'>Influencers</h3>
                            <p className='text-center max-w-[400px] mt-3'>If your fans can easily fill a stadium, spread the word and get paid.</p>
                        </div>
                    </div>

                    <div className='flex flex-col lg:flex-row items-center w-full justify-around mt-16'>

                        <div className='flex flex-col justify-center items-center'>
                            <img className='w-16 h-16' src={partnerBrand} alt="brand"/>
                            <h3 className='text-center text-2xl font-lato font-bold mt-3'>World Class Brand</h3>
                            <p className='text-center max-w-[400px] mt-3'>If your brand is synonymous with creativity, tech, and customer love, let's talk!</p>
                        </div>

                        <div className='flex flex-col justify-center items-center mt-16 lg:mt-0'>
                            <img className=' h-16' src={partnerMedia} alt="media"/>
                            <h3 className='text-center text-2xl font-lato font-bold mt-2'>Media Companies</h3>
                            <p className='text-center max-w-[400px] mt-3'>Share Petoshield with your top publishers and content providers. They’ll thank you.</p>
                        </div>
                    </div>
                </section>

                <section id='form-business' className='bg-black-haze py-12 pb-16 font-lato'>

                    <h3 className='text-center text-[40px] font-lato font-bold mt-3'>Apply Here!</h3>
                    <p className='text-center max-w-[400px] mx-auto mt-4'>
                        Tell us about your business and our team will get
                        back to you soon.
                    </p>

                    <div className='container mx-auto justify-center items-center flex flex-col mt-12'>
                        <div className='flex w-[380px] md:w-[700px] justify-between flex-col md:flex-row space-y-8 md:space-x-4 md:space-y-0'>
                            <input onChange={(e) => setBusinessName(e.target.value)} value={businessName} type="text" className='focus:ring-0 border-gallery focus:border-gallery rounded-md placeholder-nobel-dark px-4 py-3 w-full md:w-[60%]' placeholder='BUSINESS NAME'/>
                            <select onChange={(e) => setType(e.target.value)} value={type} name="type" id="type" className='focus:ring-0 border-gallery focus:border-gallery rounded-md placeholder-nobel-dark px-4 py-3 w-full md:w-[40%]'>
                                <option className='nobel-dark' selected={true} value="">WE'RE A...</option>
                                <option value="1">Content curator</option>
                                <option value="2">Leading brand</option>
                                <option value="3">Thought leader</option>
                                <option value="4">Media Company</option>
                                <option value="5">Other</option>
                            </select>
                        </div>

                        <div className='flex w-[380px] justify-between flex-col md:flex-row space-y-8 md:space-x-4 md:space-y-0 mt-8 md:mt-4 md:w-[700px]'>
                            <input onChange={(e) => setName(e.target.value)} value={name} type="text" className='focus:ring-0 border-gallery focus:border-gallery rounded-md placeholder-nobel-dark px-4 py-3 w-full md:w-[40%]' placeholder='YOUR NAME'/>
                            <input onChange={(e) => setEmail(e.target.value)} value={email} type="email" className='focus:ring-0 border-gallery focus:border-gallery rounded-md placeholder-nobel-dark px-4 py-3 w-full md:w-[60%]' placeholder='EMAIL'/>
                        </div>

                        <input onChange={(e) => setUrl(e.target.value)} value={url} type="text" className='w-[380px] md:w-[700px] focus:ring-0 border-gallery focus:border-gallery rounded-md placeholder-nobel-dark px-4 py-3 mt-8 md:mt-4' placeholder='BUSINESS URL'/>
                        <input onChange={(e) => setMessage(e.target.value)} value={message} type="text" className='w-[380px] md:w-[700px] focus:ring-0 border-gallery focus:border-gallery rounded-md placeholder-nobel-dark px-4 pb-16 py-3 mt-8 md:mt-4' placeholder='TELL US A BIT ABOUT YOUR BUSINESS'/>

                        <button onClick={sendForm} className={`py-3 px-28  mt-8 rounded-md font-bold font-lato w-[380px] md:w-fit self-center uppercase text-white transition-all duration-300 ${isDisabled ? 'bg-gallery': 'bg-rose hover:bg-rose-dark shadow-[rgba(255,0,131,0.5)_0px_10px_40px_-10px]'}`} disabled={isDisabled}>Send</button>

                    </div>
                </section>

            </main>

            <footer>
                <Footer/>
            </footer>
        </div>
    )
}

export default Partners;