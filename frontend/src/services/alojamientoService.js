import axios from "axios"

const API = "http://127.0.0.1:5000/api/alojamientos"

export const getAlojamientos = async () => {

    return await axios.get(API)
}
