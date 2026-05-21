<template>
    <main>
        <Header></Header>
        <section class="main">
            <section class="intro">
                <div class="texto">
                    <h1>RESERVAS</h1>
                    <p>Reserva ya tu estancia en VORA MAR GLAMPING</p>
                </div>
                <div class="imagen">
                    <img src="../../assets/images/42ec7ef0-0974-468c-9895-1d9d88bab013.png" alt="">
                </div>
            </section>
            <h1 class="titulo">INTRODUCE LOS DATOS</h1>
            <form class="form" @submit.prevent="reservar">
                <div class="formulario">
                    <label>
                        Alojamiento
                    </label>
                    <select v-model="alojamiento_id" required>
                        <option value="1">
                            Suite Panorama
                        </option>
                        <option value="2">
                            Suite Relax
                        </option>
                        <option value="3">
                            Suite Mediterraneo
                        </option>
                        <option value="4">
                            Suite Marina
                        </option>
                        <option value="5">
                            Suite Presidencial
                        </option>
                        <option value="6">
                            Suite Nocturna
                        </option>
                        <option value="7">
                            Suite Aqua
                        </option>
                        <option value="8">
                            Suite Roma
                        </option>
                        <option value="9">
                            Suite Morfeo
                        </option>
                        <option value="10">
                            Suite Matina
                        </option>
                    </select>
                    <label>
                        Fecha entrada
                    </label>
                    <input required
                        type="date"
                        v-model="fecha_entrada"
                    >
                    <label>
                        Fecha salida
                    </label>

                    <input
                        type="date" required
                        v-model="fecha_salida"
                    >
                    <label>
                        Huéspedes
                    </label>
                    <input
                        required
                        type="number"
                        min="1"
                        max="10"
                        v-model="huespedes"
                    >
                </div> 
                <div class="button">
                    <button type="submit">RESERVAR</button>
                </div>
             </form>
             <div class="errores">
                <p v-if="successMessage">
                    {{ successMessage }}
                </p>
                <p v-if="errorMessage">
                    {{ errorMessage }}
                </p>    
            </div>
        </section>
        <Footer></Footer>
    </main>
</template>

<script setup>
    import { ref } from "vue"
    import Header from "@/components/Header.vue"
    import Footer from "@/components/Footer.vue"
    import { createReserva } from "@/services/reservaService"

    const alojamiento_id = ref("")
    const fecha_entrada = ref("")
    const fecha_salida = ref("")
    const huespedes = ref(1)
    const successMessage = ref("")
    const errorMessage = ref("")
    const user = JSON.parse(localStorage.getItem("user"))
    const reservar = async () => {
        successMessage.value = ""
        errorMessage.value = ""
        if (user) {
            try {
                await createReserva({
                    usuario_id: user.id,
                    alojamiento_id: alojamiento_id.value,
                    fecha_inicio: fecha_entrada.value,
                    fecha_fin: fecha_salida.value,
                    num_personas: huespedes.value,       
                })
                successMessage.value = "Reserva realizada correctamente"
            } catch (error) {
                errorMessage.value =  error.response?.data?.error || "Error al realizar la reserva"
            }
        } else {
            errorMessage.value = "Debes iniciar sesión para reservar"
        }
        
    }
</script>

<style scoped lang="sass">
    @use "../../assets/sass/variables" 
    @use "../../assets/sass/mixins"
    main
        .main
            .intro
                @include mixins.flexbox($d: flex , $fd: row , $jc: center, $gap: 2rem )
                align-items: center
                background: variables.$color_background_principal
                .texto
                    @include mixins.flexbox($d: flex , $fd: column , $jc: center , $gap: 3rem)
                    text-align: center
                    align-items: center
                    h1
                        color: variables.$color_texto_principal
                        font-family: variables.$tipografia_titulo
                    p
                        font-family: variables.$tipografia_texto        
                .imagen
                    padding: 2rem
                    img
                        border-radius: 20px
                        width: 500px  
                    &:hover
                        scale: 1.03
                        transition: ease-in-out 0.3s  
            .titulo
                text-align: center
                color: variables.$color_texto_principal
                background: variables.$color_background_secundario
                padding: 1rem
            .form
                padding: 3rem
                @include mixins.flexbox($d: flex, $fd: column , $jc: center , $gap: 3rem)
                align-items: center
                font-family: variables.$tipografia_texto
                background: variables.$color_background_secundario
                .formulario
                    @include mixins.flexbox($d: flex, $fd: row , $jc: center , $gap: 1rem)
                    align-items: center
                    background: white
                    padding: 4rem
                    box-shadow: 0 10px 30px rgba(0,0,0,0.08)
                    border-radius: 20px
                    input
                        box-shadow: 0 10px 30px rgba(0,0,0,0.08)
                        padding: 1rem  
                        border: none
                        border-radius: 20px
                    select
                        box-shadow: 0 10px 30px rgba(0,0,0,0.08)
                        padding: 10px
                        border: none
                        border-radius: 20px
                .button
                    width: 20%
                    @include mixins.flexbox($d: flex , $fd: row , $jc: center , $gap: 0)
                    button
                        padding: 2rem 4rem
                        border: none
                        border-radius: 20px
                        color: white
                        background: variables.$color_boton_principal
                        cursor: pointer
                        font-family: variables.$tipografia_texto
                        &:hover
                            scale: 1.03
                            transition: ease-in-out 0.3s
                            background: variables.$color_hover_principal
            .errores
                text-align: center
                font-family: variables.$tipografia_texto
                background: variables.$color_background_secundario
                padding: 1rem
                @include mixins.flexbox($d: flex, $fd: row , $jc: center , $gap: 0 )
                p
                    padding: 1rem
                    background: variables.$color_alternativo
                    width: 25%
                    align-items: center
                    border-radius: 20px
                    color: white
    @media (max-width: 768px)   
        main
            .main
                .intro
                    @include mixins.flexbox($d: flex , $fd: column, $jc: center , $gap: 1rem )
                    .texto  
                        padding: 1rem
                    .imagen
                        img
                            width: 250px
                .form
                    @include mixins.flexbox($d: flex, $fd: column , $jc: center , $gap: 1rem )
                    .formulario
                        @include mixins.flexbox($d: flex, $fd: column , $jc: center , $gap: 1rem )
                        padding: 2rem 4rem  
                .errores
                    p
                        width: 50%
</style>    