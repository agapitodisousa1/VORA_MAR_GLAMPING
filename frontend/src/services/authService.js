import axios from "axios";

// funcion que postea los datos del formulario mediante axios.post
// al endpoint de la API
export const loginRequest = async (data) => {
  return await axios.post(`${import.meta.env.VITE_API_URL}/api/auth/login`, data)
}
// hace los mismo que la anterior pero del register
export const registerRequest = async (data) => {
    return await axios.post(`${import.meta.env.VITE_API_URL}/api/auth/register`, data);
}
// comprueba que el usuario esté logueado recogiendo el token del localStorage
// y devolviendo un booleano que es true si existe y false si no existe token
export const isLogged = () => { 
    const token = localStorage.getItem("token")

    return !!token
}
// obtiene el user del localStorage y devuelve el user si hay o null si no hay 
export const getUser = () => {

    const user = localStorage.getItem("user")

    return user ? JSON.parse(user) : null
}
// cierra la sesión eliminando el token y el user del localStorage
export const logout = () => {
    localStorage.removeItem("token")
    localStorage.removeItem("user")
}