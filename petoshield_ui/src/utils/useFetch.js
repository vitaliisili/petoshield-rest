import {useEffect, useState} from "react";
import axios from "axios";

const useFetch = (url) => {
    const [data, setData] = useState(null)
    const [isPending, setPending] = useState(true)
    const [error, setError] = useState(null)


    useEffect(() => {
        axios.get(url, {

        })
            .then(response => {
                setData(response.data)
                setPending(false)
                setError(null)
            }).catch(error => {
            setPending(false)
            setError(error)
        })
    }, [url])


    return {data, isPending, error}
}

export default useFetch