import axios from "axios"
 
// crea la reserva con un post a la api pasandole los datos al endpoint
export const createReserva = async (data) => {

    return await axios.post(`${import.meta.env.VITE_API_URL}/api/reservas/`, data)
}

// obtiene las reservas del usuario actual pasandole el id al endpoint con un get
export const getReservasUsuario = async (id) => {

    return await axios.get(`${import.meta.env.VITE_API_URL}/api/reservas/reserva/${id}`)
}
 
// cancela la reserva mediante un axios.put pasandole el id de la reserva al endpoint
export const cancelarReserva = async (id) => {
    return await axios.put(`${import.meta.env.VITE_API_URL}/api/reservas/${id}`)
}
