import axios from "axios"


export const getAlojamientos = async () => {

    return await axios.get(`${import.meta.env.VITE_API_URL}/api/alojamientos`)
}

