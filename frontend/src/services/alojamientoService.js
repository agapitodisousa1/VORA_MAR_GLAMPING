import axios from "axios"

// funcion que mediante axios realiza una petición get al endpoint de la api
export const getAlojamientos = async () => {

    return await axios.get(`${import.meta.env.VITE_API_URL}/api/alojamientos`)
}

