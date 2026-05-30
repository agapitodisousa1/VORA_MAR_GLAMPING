import axios from "axios"

// hace una petición get a la API que  como necesita permisos de admin le pasa el token
// recogido del localStorage en la cabecera http Authorization. Recoge los datos del dashboard
export const getDashboard = async () => {

    const token = localStorage.getItem("token")

    return await axios.get(`${import.meta.env.VITE_API_URL}/api/dashboard/`, { headers:{ 
        Authorization:`Bearer ${token}` }})
}

// confirma la reserva mediante axios.put al endpoint de la API pasando el id de la reserva
export const confirmarReserva = async (id) => {
    
    return await axios.put(`${import.meta.env.VITE_API_URL}/api/dashboard/${id}`)
}