import React from 'react';
import vs from "../static/images/slider/vs.jpg";
import johanna from "../static/images/slider/johanna.jpeg";
import john from "../static/images/slider/john.jpeg";
import mathias from "../static/images/slider/mathias.jpeg";
import vanessa from "../static/images/slider/vanessa.jpeg";
import sara from "../static/images/slider/sara.jpeg";
import mike from "../static/images/slider/mike.jpeg";
import marissa from "../static/images/slider/marissa.jpeg";

const Carousel = () => {

    const items = [
        {
            'image': vs,
            'name': 'Vitalii Sili',
            'message': `wow this was hands down the best insurance experience ever. holy shit I love your app.`
        },
        {
            'image': john,
            'name': 'John P. Roebuck',
            'message': `I am absolutely thrilled with the outstanding service and coverage provided by this pet insurance company. I knew I made the right choice for my furry family member.`
        },
        {
            'image': johanna,
            'name': 'Johanna Shuster',
            'message': `Additionally, this company genuinely cares about the well-being of pets. They provide helpful resources and tips for pet care`
        },
        {
            'image': mathias,
            'name': 'Mathias Pfeffer',
            'message': `I highly recommend this pet insurance company to all pet owners. Their exceptional service, extensive coverage options`
        },
        {
            'image': vanessa,
            'name': 'Vanessa Bader',
            'message': `I was pleasantly surprised by how quickly my claims were processed and reimbursed, allowing me to focus on taking care of my pet`
        },
        {
            'image': sara,
            'name': 'Sara Lorem',
            'message': `The peace of mind I gained from knowing that my pet is protected, no matter what life throws our way, is invaluable.`
        },
        {
            'image': mike ,
            'name': 'Mike Kobold',
            'message': `In summary, I wholeheartedly endorse Petoshield to every pet parent seeking reliable and compassionate insurance coverage`
        },
        {
            'image': marissa ,
            'name': 'Marissa Dallas',
            'message': `Thank you, Petoshield, for being a reliable partner in ensuring my pet's health and happiness!`
        },
    ]

    return (
        <div className=''>
            <div className='flex slider absolute left-0 w-[6882px]'>
                <div className='flex w-full space-x-8'>
                <div className='flex space-x-8'>
                    {items && items.map(user => (
                        <div key={user.name} className='card rounded-md bg-white w-[400px] h-52 shadow-[rgba(100,100,111,0.2)_0px_7px_29px_0px] flex flex-col pt-4 pl-8 pr-8 font-lato'>
                            <div className='flex items-center'>
                                <div className='bg-rose w-12 h-12 relative rounded-full overflow-hidden'>
                                    <img className='w-full h-full object-cover' src={user.image} alt={user.name}/>
                                </div>
                                <div className='pl-4'>{user.name}</div>
                            </div>
                            <div className='pt-2'>
                                <p className='leading-5'><span className='text-rose'>@Petoshield </span> {user.message}</p>
                            </div>
                        </div>
                        ))}
                </div>
                <div className='flex space-x-8'>
                    {items && items.map(user => (
                        <div key={user.name} className='card rounded-md bg-white w-[400px] h-52 shadow-[rgba(100,100,111,0.2)_0px_7px_29px_0px] flex flex-col pt-4 pl-8 pr-8 font-lato'>
                            <div className='flex items-center'>
                                <div className='bg-rose w-12 h-12 relative rounded-full overflow-hidden'>
                                    <img className='w-full h-full object-cover' src={user.image} alt={user.name}/>
                                </div>
                                <div className='pl-4'>{user.name}</div>
                            </div>
                            <div className='pt-2'>
                                <p className='leading-5'><span className='text-rose'>@Petoshield </span> {user.message}</p>
                            </div>
                        </div>
                    ))}
                </div>
                </div>
            </div>
        </div>
    )
}

export default Carousel;