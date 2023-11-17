import React, {useEffect, useState} from 'react'
import {FiHelpCircle} from "react-icons/fi"
import {AiOutlineClose} from "react-icons/ai";

const TermsModal = ({callback}) => {


    return (
        <div className='fixed bg-gallery-transparent w-screen h-screen z-40 top-0 py-20 flex justify-center'>
            <div className='z-50 flex flex-col text-center bg-white rounded-md p-8 '>
                <div className='max-h-[700px] w-[500px] overflow-y-scroll'>
                    <p>Terms</p>
                    <h1 id="terms-of-website-use-for-petoshield">Terms of Website Use for Petoshield</h1>
                    <h2 id="introduction">Introduction</h2>
                    <ul className='mt-8'>
                        <li><em>Website</em>: petoshield.com</li>
                        <li><em>Date of Effect</em>: 08.11.2023</li>
                        <li><em>Applicability</em>: Guests and Registered Users
                            <h2 className='mt-8' id="acceptance-of-terms">Acceptance of Terms</h2>
                        </li>
                        <li>By accessing the Petoshield website, you agree to these terms.</li>
                        <li>Additional terms apply to registered members.<h2 id="section-a-all-users">Section A: All Users</h2>
                            <h3 id="information-about-petoshield">Information about Petoshield</h3>
                        </li>
                        <li><em>Operator</em>: Petoshield Insurance Services</li>
                        <li><em>Registration</em>: Petoshield Limited</li>
                        <li><em>Regulation</em>: Financial Conduct Authority (FCA), No. 123456</li>
                        <li><em>Services</em>: Insurance brokerage without direct insurance services.</li>
                        <li><em>Liability</em>: Limited as per the terms.
                            <h3 className='mt-8' id="website-access">Website Access</h3>
                        </li>
                        <li><em>Temporary Basis</em>: Right to withdraw or amend service.</li>
                        <li><em>Restrictions</em>: Possible for certain sections or the entire site.</li>
                        <li><em>Security</em>: User credentials to be kept confidential.<h3 id="intellectual-property-rights">Intellectual Property Rights</h3>
                        </li>
                        <li><em>Ownership</em>: Respective companies and Petoshield.</li>
                        <li><em>Usage</em>: Limited to personal reference and internal sharing.</li>
                        <li><em>Restrictions</em>: No commercial use without a license.<h3 id="reliance-on-information">Reliance on Information</h3>
                        </li>
                        <li><em>Accuracy</em>: Reasonable steps for up-to-date information.</li>
                        <li><em>Liability</em>: Disclaimed for errors, omissions, or reliance.<h3 id="website-changes">Website Changes</h3>
                        </li>
                        <li>Regular updates and potential suspension of access.<h3 id="liability-limitations">Liability Limitations</h3>
                        </li>
                        <li>Exclusions and limitations on certain damages and warranties.<h2 id="section-b-registered-users">Section B: Registered Users</h2>
                            <h3 id="user-eligibility">User Eligibility</h3>
                        </li>
                        <li>Age and residency requirements.<h3 id="service-description">Service Description</h3>
                        </li>
                        <li>Brokerage services and role limitations.</li>
                        <li>No insurance advice provided.<h3 id="partner-contracts">Partner Contracts</h3>
                        </li>
                        <li>Relationship between users and insurance partners.</li>
                        <li>Importance of understanding partner terms.<h3 id="contact-information">Contact Information</h3>
                        </li>
                        <li>How to reach Petoshield for concerns or inquiries.<h2 id="amendments-and-jurisdiction">Amendments and Jurisdiction</h2>
                        </li>
                        <li>Terms subject to change.</li>
                        <li>Jurisdiction for disputes.
                            Thank you for using Petoshield.
                            © [2023] Petoshield Insurance Services</li>
                    </ul>
                </div>
                <button onClick={() => callback()} className='rounded-md mt-8 bg-rose hover:bg-rose-dark font-bold transition-all duration-300 shadow-[rgba(255,0,131,0.5)_0px_10px_40px_-10px] w-full p-3.5 text-white'>Close</button>

            </div>
        </div>
    )
}

export default TermsModal