<template>
    <section class="main">
        <Header></Header>
        <section class="login">
            <h1 class="title">
                INICIA SESIÓN
            </h1>
            <div class="container">
                <form class="form" @submit.prevent="login">
                    <p>Correo electrónico</p>
                    <input
                    type="email" required
                    placeholder="Correo electrónico"
                    v-model="email"
                    />
                    <p>Contraseña</p>
                    <input required
                    type="password"
                    placeholder="Contraseña"
                    v-model="password"
                    />
                    <div class="botones">
                        <button type="submit" class="btn_login">
                            Entrar
                        </button>
                        <button type="button" @click="goRegister" class="btn_register">
                            No tengo cuenta
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
    import Header from "@/components/Header.vue";
    import Footer from "@/components/Footer.vue";
    import { ref } from "vue";
    import { useRouter } from "vue-router";
    import { loginRequest } from "../../services/authService";

    const router = useRouter()
    const email = ref("")
    const password = ref("")
    const errorMessage = ref("")
    const goRegister = () => {
        router.push("/register")
    }
    // funcion para loguearse asincrona que obtiene una repuesta de la función loginRequest que 
    // accede a la API de autenticación y obtiene el token y el usuario y lo guarda en el localStorage. 

    const login = async () => {
    
    errorMessage.value = ""
    try{
        const response = await loginRequest({
        email: email.value,
        password: password.value
        })

        localStorage.setItem("token", response.data.token)
        localStorage.setItem(
        "user",
        JSON.stringify(response.data.user)
        )
        if (response.data.user.rol === "admin") {
        router.push("/admin/dashboard")
        } else {
        router.push("/")
        }
    } catch (error) {
        errorMessage.value =
        error.response?.data?.message ||
        "Error al iniciar sesión"
    }
    }
</script>

<style lang="sass" scoped>
    @use "../../assets/sass/variables" 
    @use "../../assets/sass/mixins"
    .main
        height: 100vh
        .login 
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
                width: 33%
                padding: 10px
                border-radius: 12px
                background: variables.$color_background_principal
                padding: 1rem
                .form 
                    @include mixins.flexbox($d: flex , $fd: column , $jc: center , $gap: 11.5px )
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
                height: 80vh
                .container
                    width: 60%
                    .form
                        .botones
                            .btn_login
                                padding: 10px 1rem  
                            .btn_register
                                padding: 10px 1rem
    @media (min-width: 769px) and (max-width: 1024px)
        .main
            .login
                height: 84vh
                .container
                    width: 60%  
                    .form
                        padding: 2rem
                    
</style>