import React from 'react';
import NavBar from "../components/NavBar";
import HelpModal from "../components/HelpModal";
import Footer from "../components/Footer";
import givebackPizza from "../static/images/giveback/giveback-pizza.svg"
import givebackPhone from "../static/images/giveback/giveback-phone.svg"
import givebackFaces from "../static/images/giveback/giveback-people.svg"
import givebackCoin from "../static/images/giveback/giveback-coin.svg"
import givebackArrow from "../static/images/giveback/arrow.svg"
import givebackHearth from "../static/images/giveback/giveback-hearth.svg"
import {MdOutlineDone} from "react-icons/md";
import {Link} from "react-router-dom";

const Giveback = () => {
    return (
        <div className='text-black'>
            <NavBar/>
            <HelpModal/>

            <main className='pt-32'>
                <section className='flex flex-col justify-center items-center pb-12 px-4'>
                    <h1 className='text-[50px] font-merriweather text-center' >The Petoshield Giveback</h1>

                    <p className='text-center max-w-[700px] mt-3'>
                        Here’s our mission: transform insurance from a necessary evil into a social good. We’ve designed Petoshield to bring out the best in people, while giving society a push for the better. Introducing the Petoshield Giveback.
                    </p>

                    <div className='mt-16'>
                        <img src={givebackPizza} alt='giveback-pizza'/>
                    </div>

                    <h2 className='text-[40px] font-bold font-lato mt-8'>Making a change</h2>

                    <p className='text-center max-w-[700px] mt-4'>
                        Lemonade takes a flat fee and treats the rest of the money as yours, not ours. We use it to pay claims, and give what’s left to charities you choose, so we never fight over the same coin.
                    </p>

                    <h4 className='font-bold mt-10 flex text-lg'>This means:</h4>

                    <div className='flex justify-center items-center w-96 space-x-8 mt-4'>
                        <MdOutlineDone className='text-rose text-3xl'/>
                        <p className='text-sm'>
                            You get some great insurance, while making a mark on a cause you care about.
                        </p>
                    </div>

                    <div className='flex justify-center items-center w-96 space-x-8 mt-8'>
                        <MdOutlineDone className='text-rose text-3xl'/>
                        <p className='text-sm'>
                            Social good is baked into our business model — we’re a Public Benefit Corporation
                        </p>
                    </div>

                </section>

                <section className='bg-black-haze flex flex-col justify-center items-center py-12 px-4'>
                    <h2 className='text-[40px] font-bold font-lato'>How Giveback works</h2>

                    <div className='flex flex-col lg:flex-row'>
                        <div className='w-60 flex flex-col justify-center items-center'>
                            <img src={givebackPhone} alt="phone"/>
                            <p className='text-center leading-6 text-sm'>You get a Petoshield policy, and <span className='font-bold'>select a nonprofit</span> you care about</p>
                        </div>

                        <img src={givebackArrow} alt="arrow"/>

                        <div className='w-60 flex flex-col justify-center items-center'>
                            <img src={givebackFaces} alt="faces"/>
                            <p className='text-center leading-6 text-sm'>You get a Petoshield policy, and <span className='font-bold'>select a nonprofit</span> you care about</p>
                        </div>

                        <img src={givebackArrow} alt="arrow"/>

                        <div className='w-60 flex flex-col justify-center items-center'>
                            <img src={givebackCoin} alt="coin"/>
                            <p className='text-center leading-6 text-sm'>You get a Petoshield policy, and <span className='font-bold'>select a nonprofit</span> you care about</p>
                        </div>
                    </div>
                </section>

                <section className='px-4 flex flex-col justify-center items-center py-12'>
                    <img src={givebackHearth} alt="hearth"/>
                    <h2 className='text-[40px] mt-8 font-bold font-lato text-center'>Join the Giveback movemen</h2>
                    <p className='text-center max-w-[520px] mt-4'>
                        Tens of thousands of members already support causes they care about,
                        simply by getting a Petoshield insurance policy. As our Petoshield
                        community grows, your social impact can become even stronger.
                    </p>
                    <Link to='/price'><button className='uppercase rounded-md bg-rose hover:bg-rose-dark font-bold transition-all duration-300 shadow-[rgba(255,0,131,0.5)_0px_10px_40px_-10px] w-full px-6 py-3 text-white max-w-fit mt-8'>Get insured and give back</button></Link>
                </section>
            </main>

            <footer>
                <Footer/>
            </footer>
        </div>
    )
}

export default Giveback;