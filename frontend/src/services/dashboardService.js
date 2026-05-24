import axios from "axios"

const API = "http://127.0.0.1:5000/api/dashboard/"

export const getDashboard = async () => {

    const token = localStorage.getItem("token")

    return await axios.get(API, { headers:{ 
        Authorization:`Bearer ${token}` }})
}

export const confirmarReserva = async (id) => {
    return await axios.put(`http://127.0.0.1:5000/api/dashboard/${id}`)
}