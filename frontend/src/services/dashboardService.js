import axios from "axios"



axios.get(

)
export const getDashboard = async () => {

    const token = localStorage.getItem("token")

    return await axios.get(`${import.meta.env.VITE_API_URL}/api/dashboard`, { headers:{ 
        Authorization:`Bearer ${token}` }})
}

export const confirmarReserva = async (id) => {
    return await axios.put(`${import.meta.env.VITE_API_URL}/api/dashboard/${id}`)
}