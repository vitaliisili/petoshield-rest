import React from 'react';

const Clouds = ({type, zIndex}) => {
    return (
        <div className={`absolute top-0 w-full ${zIndex} pt-20 overflow-hidden`}>
            <div className="x1">
                <div className={`${type === 'light' ? 'cloud-light': 'cloud'} cloud1`}></div>
            </div>

            <div className="x2">
                <div className={`${type === 'light' ? 'cloud-light': 'cloud'} cloud2`}></div>
            </div>

            <div className="x3">
                <div className={`${type === 'light' ? 'cloud-light': 'cloud'} cloud3`}></div>
            </div>

            <div className="x4">
                <div className={`${type === 'light' ? 'cloud-light': 'cloud'} cloud4`}></div>
            </div>

            <div className="x5">
                <div className={`${type === 'light' ? 'cloud-light': 'cloud'} cloud5`}></div>
            </div>
        </div>
    );
};

export default Clouds;