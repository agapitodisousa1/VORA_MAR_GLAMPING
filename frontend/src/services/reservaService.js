import axios from "axios"

const API = "http://127.0.0.1:5000/api/reservas/"

export const createReserva = async (data) => {

    return await axios.post(API, data)
}

export const getReservasUsuario = async (id) => {

    return await axios.get(`http://127.0.0.1:5000/api/reservas/reserva/${id}`)
}

export const cancelarReserva = async (id) => {
    return await axios.put(`http://127.0.0.1:5000/api/reservas/${id}`)
}
