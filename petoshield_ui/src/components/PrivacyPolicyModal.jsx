import React from 'react';

const PrivacyPolicyModal = ({callback}) => {
    return (
        <div className='fixed bg-gallery-transparent w-screen h-screen z-40 top-0 py-20 flex justify-center'>
            <div className='z-50 flex flex-col text-center bg-white rounded-md p-8 '>
                <div className='max-h-[700px] w-[300px] md:w-[500px] overflow-y-scroll'>
                    <p>Privacy Policy</p>

                    <h1 id="petoshieldprivacypolicy">Petoshield Privacy Policy</h1>

                    <h2 id="background">Background</h2>

                    <p>At Petoshield, protecting your privacy is paramount. We are dedicated to the secure and lawful handling of your personal information.</p>

                    <h2 id="whoweare">Who We Are</h2>

                    <p>Petshield is responsible for your personal data.</p>

                    <ul>
                        <li><em>Company</em>: Petoshield Insurance Services, Petoshield Limited</li>

                        <li><em>Contact</em>: petoshield@gmail.com</li>
                    </ul>

                    <h2 id="dataprocessing">Data Processing</h2>

                    <p>This policy pertains to all Petoshield customers and users.</p>

                    <h2 id="lawfulbasesforprocessing">Lawful Bases for Processing</h2>

                    <p>We process personal data based on various lawful bases, tailored to our services.</p>

                    <h2 id="collectionanduseofdata">Collection and Use of Data</h2>

                    <p>We collect data necessary for policy management, claims processing, and customer service.</p>

                    <h2 id="yourrights">Your Rights</h2>

                    <p>You can access, amend, or request deletion of your personal data.</p>

                    <h2 id="sharingandtransferringdata">Sharing and Transferring Data</h2>

                    <p>Data is shared with third parties under strict conditions for essential services.</p>

                    <h2 id="dataretention">Data Retention</h2>

                    <p>We hold personal data as legally required or for legitimate business needs.</p>

                    <h2 id="contactingus">Contacting Us</h2>

                    <p>For privacy concerns, reach out to our Data Protection Officer.</p>

                    <h2 id="cookiesandthirdpartylinks">Cookies and Third-Party Links</h2>

                    <p>We use cookies and provide links to third-party sites, over which we have no control.</p>

                    <h2 id="updatestoourprivacypolicy">Updates to Our Privacy Policy</h2>

                    <p>We will inform you of significant changes to our privacy practices.</p>
                </div>
                <button onClick={() => callback()} className='rounded-md mt-8 bg-rose hover:bg-rose-dark font-bold transition-all duration-300 shadow-[rgba(255,0,131,0.5)_0px_10px_40px_-10px] w-full p-3.5 text-white'>Close</button>

            </div>
        </div>
    );
};

export default PrivacyPolicyModal;