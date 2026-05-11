<template>
    <header>
        <div class="izquierda">
            <div class="instalaciones">
                <p @click="goInstalaciones">INSTALACIONES</p>
            </div>
            <div class="reservas">
                <p @click="goReservas">RESERVAS</p>
            </div>
        </div>
        <div class="logo">
            <img src="../assets/images/logo.png" alt="" @click="goHome">
        </div>
        <div class="derecha">
            <div class="alojamientos">
                <p @click="goAlojamientos">ALOJAMIENTOS</p>
            </div>
            <div class="botones">
                <div class="botones_login" v-if="isLogged()">
                    <button @click="goLogout()" >Cerrar sesión</button>
                    <button @click="goDashboard" v-if="user?.rol === 'admin'">Dashboard</button>
                </div>
                <div class="botones_no_login" v-else>
                    <button @click="goLogin"  >Iniciar sesión</button>
                    <button @click="goRegister" >Registrarse</button>
                </div>
            </div>
        </div>
    </header>
</template>

<script setup>
    import { useRouter } from 'vue-router';
    import { isLogged, getUser, logout } from '@/services/authService';

    const router = useRouter()
    const user = getUser()

    const goLogout = () => {
        logout()
        window.location.reload()
    }
    const goDashboard = () => {
        router.push("/admin/dashboard")
    }
    const goHome = () => {
        router.push("/")
    }
    const goReservas = () => {
        router.push("/reservas")

    }
    const goAlojamientos = () => {
        router.push("/alojamientos")
    }
    const goInstalaciones = () => {
        router.push("/instalaciones")
    } 
    const goLogin = () => {
        router.push("/login")
    }
    const goRegister = () => {
        router.push("/register")
    }
</script>

<style scoped lang="sass">
    @use "../assets/sass/variables"
    @use "../assets/sass/mixins"
    header
        @include mixins.flexbox($d: flex , $fd: row , $jc: space-around , $gap:0 )
        position: sticky
        top: 0
        z-index: 1000
        width: 100%
        font-family: variables.$tipografia_titulo 
        background: variables.$color_texto_principal
        color: variables.$color_background_secundario
        align-items: center
        .izquierda
            @include mixins.flexbox($d: flex , $fd: row , $jc: flex-start, $gap: 8rem)
            width: 33%
            .reservas
                padding: 1rem
                margin-top:10px
                p
                    cursor: pointer
                &:hover
                    scale: 1.05
                    transition: ease-in-out 0.2s
            .instalaciones
                padding: 1rem
                margin-top: 10px
                p
                    cursor: pointer
                &:hover
                    scale: 1.05
                    transition: ease-in-out 0.2s
        .logo
            padding: 1rem
            img
                height: 60px
                width:  75px
                border-radius: 12px
                cursor: pointer
            &:hover
                scale: 1.05
                transition: ease-in-out 0.2s
        .derecha
            @include mixins.flexbox($d: flex, $fd: row , $jc: flex-end , $gap: 2rem )
            .alojamientos
                padding: 1rem 
                margin-top: 25px    
                p
                    cursor: pointer
                &:hover
                    scale: 1.05
                    transition: ease-in-out 0.2s 
            .botones
                padding: 1rem
                margin-bottom: 2rem
                .botones_login
                    @include mixins.flexbox($d: flex, $fd: row , $jc: center , $gap: 1rem )
                    button
                        @include mixins.flexbox($d: flex, $fd: row , $jc: center , $gap: 1rem )
                        border-radius: 12px
                        cursor: pointer
                        font-size: 12px
                        padding: 12px
                        font-family: variables.$tipografia_texto
                        border-radius: 10px
                        background: variables.$color_boton_secundario
                        color: variables.$color_background_secundario
                        border: none
                        &:hover
                            background: variables.$color_hover_secundario
                            transition: ease-in-out 0.2s
                            scale: 1.05
                .botones_no_login
                    @include mixins.flexbox($d: flex , $fd: row , $jc: center, $gap: 1rem)
                    button
                        @include mixins.flexbox($d: flex, $fd: row , $jc: center , $gap: 1rem )
                        font-size: 12px
                        border-radius: 12px
                        cursor: pointer
                        padding: 12px
                        font-family: variables.$tipografia_texto
                        background: variables.$color_boton_secundario
                        color: variables.$color_background_secundario
                        border: none
                        &:hover
                            background: variables.$color_hover_secundario
                            transition: ease-in-out 0.2s
                            scale: 1.05
</style>