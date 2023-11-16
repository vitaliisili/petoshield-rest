import React from 'react';
import {useLocation} from "react-router-dom";

const Payment = () => {

    const location = useLocation()

    return (
        <div>
            <h1>Payment</h1>
        </div>
    );
};

export default Payment;