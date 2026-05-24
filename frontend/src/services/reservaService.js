import axios from "axios"

const API = "http://127.0.0.1:5000/api/reservas/"


export const createReserva = async (data) => {

    return await axios.post(`${import.meta.env.VITE_API_URL}/api/reservas/`, data)
}

export const getReservasUsuario = async (id) => {

    return await axios.get(`${import.meta.env.VITE_API_URL}/api/reservas/reserva/${id}`)
}

export const cancelarReserva = async (id) => {
    return await axios.put(`${import.meta.env.VITE_API_URL}/api/reservas/${id}`)
}
