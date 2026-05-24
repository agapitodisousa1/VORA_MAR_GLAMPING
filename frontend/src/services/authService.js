import axios from "axios";

const API = "http://127.0.0.1:5000/api/auth"

export const loginRequest = async (data) => {
  return await axios.post(`${import.meta.env.VITE_API_URL}/api/auth/login`, data)
}

export const registerRequest = async (data) => {
    return await axios.post(`${import.meta.env.VITE_API_URL}/api/auth/register`, data);
}
export const isLogged = () => { 
    const token = localStorage.getItem("token")

    return !!token
}
export const getUser = () => {

    const user = localStorage.getItem("user")

    return user ? JSON.parse(user) : null
}

export const logout = () => {
    localStorage.removeItem("token")
    localStorage.removeItem("user")
}