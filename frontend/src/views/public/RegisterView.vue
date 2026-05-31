<template>
    <section class="main">
        <Header></Header>
        <section class="login">
            <h1 class="title">
                CREAR CUENTA
            </h1>
            <div class="container">
                <form class="form" @submit.prevent="register">
                    <p>Correo electrónico</p>
                    <input
                    type="email" required
                    placeholder="Correo electrónico"
                    v-model="email"
                    />
                    <p>Nombre</p>
                    <input type="text" required
                    placeholder="Nombre"
                    v-model="nombre">
                    <p>Teléfono</p>
                    <input type="text" required
                    placeholder="Teléfono"
                    v-model="telefono">
                    <p>Contraseña</p>
                    <input required
                    type="password"
                    placeholder="Contraseña"
                    v-model="password"
                    />
                    <p>Repetir contraseña</p>
                    <input type="password"
                    placeholder="Vuelve a introducir la contraseña"
                    v-model="repetirPassword"
                    >
                    <div class="botones">
                        <button type="submit" class="btn_register">
                            Registrarse
                        </button>
                        <button type="button" @click="goLogin" class="btn_login">
                            Ya tengo cuenta
                        </button>
                    </div>
                </form>
                <p v-if="errorMessage" class="error">
                    {{ errorMessage }}
                </p>
            </div>
        </section>
        <Footer></Footer>
    </section>
</template>


<script setup>
    import Footer from '@/components/Footer.vue';
    import Header from '@/components/Header.vue';
    import { ref } from "vue"
    import { useRouter } from "vue-router"
    import { registerRequest } from "../../services/authService"

    const router = useRouter()
    const nombre = ref("")
    const email = ref("")
    const telefono = ref("")
    const password = ref("")
    const repetirPassword = ref("")
    const errorMessage = ref("")
    const successMessage = ref("")
    // funcion asincrona para registrarse, comprueba que el password sea lo suficientemente grande, 
    // comprueba que el password y el password repetido sea iguales y luego hace la petición mediante 
    // registerRequest con lo que postea los datos obtenidos. tambien asigna mensajes de exito y error.
    const register = async () => {
        errorMessage.value = ""
        successMessage.value = ""
        if (password.value !== repetirPassword.value) {
            errorMessage.value = "Las contraseñas no coinciden"
            return
        }
        if (password.value.length < 6) {
            errorMessage.value = "La contraseña debe tener mínimo 6 caracteres"
            return
        }
        try {
            await registerRequest({
                nombre: nombre.value,
                email: email.value,
                telefono: telefono.value,
                password: password.value
            })
            successMessage.value = "Usuario registrado correctamente"
            setTimeout(() => {
                router.push("/login")
            }, 1500)
        } catch (error) {
            console.log(error)
            errorMessage.value =
                error.response?.data?.message ||
                "Error al registrarse"
        }
    }
    const goLogin = () => {
        router.push("/login")
    }



</script>

<style scoped lang="sass">
    @use "../../assets/sass/variables" 
    @use "../../assets/sass/mixins"
    .main
        background-color: variables.$color_background_secundario
        .login 
            margin-top: 2rem
            @include mixins.flexbox($d: flex , $fd: column, $jc: center , $gap: 1rem )
            align-items: center
            background-color: variables.$color_background_secundario
            padding-bottom: 2.8rem  
            height: 100vh
            .title 
                text-align: center
                font-size: 1.5rem
                font-family: variables.$tipografia_texto
                padding: 1rem
            .container 
                width: 350px
                padding: 10px
                border-radius: 12px
                background: variables.$color_background_principal
                padding: 1rem
                width: 33%  
            .form 
                @include mixins.flexbox($d: flex , $fd: column , $jc: center , $gap: 1rem )
                font-family: variables.$tipografia_texto
                font-size: 15px
                input 
                    padding: 10px
                    border-radius: 10px
                    border: none
                .botones
                    @include mixins.flexbox($d: flex, $fd: row, $jc: center , $gap: 2rem )
                    padding-top: 10px
                    .btn_login
                        padding: 1rem
                        border: none
                        border-radius: 12px
                        background-color: variables.$color_boton_principal
                        color: variables.$color_background_secundario
                        cursor: pointer
                        &:hover 
                            scale: 1.05 
                            transition: ease-in-out 0.3s
                            background: variables.$color_hover_principal
                    .btn_register
                        padding: 1rem
                        border-radius: 12px
                        border: none
                        background-color: variables.$color_alternativo
                        cursor: pointer
                        color: variables.$color_background_secundario
                        &:hover
                            scale: 1.05
                            transition: ease-in-out 0.3s
            .error
                font-family: variables.$tipografia_texto
                margin-top: 15px
                color: red
                text-align: center
    @media (max-width: 768px)
        .main
            .login
                .container
                    width: 60%
                    .form
                        .botones
                            .btn_login
                                padding: 10px  
                                font-size: 12px
                            .btn_register
                                padding: 10px 
                                font-size: 12px
    @media (min-width: 769px) and (max-width: 1024px)
        .main
            .login
                height: 84vh
                .container
                    width: 60%
                    .form
                        padding: 2rem
</style>