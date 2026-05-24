<template>
    <main>
        <Header></Header>
        <section class="intro">
            <h1>
                EL DESCANSO QUE MERECES LA HUELLA QUE RESPETAS
            </h1>
            <p>
                ¿Buscas un retiro con desconexión total?<br><br>
                Un lugar donde se respeta el medio ambiente, libre de humos y con alojamientos exclusivos de alta calidad.<br><br>
                Es lo que ofrecemos en VORA MAR GLAMPING
            </p>
        </section>
        <section class="instalaciones">
            <div class="titulo_instalaciones">
                <h1>
                    INSTALACIONES
                </h1>
            </div>
            <section class="cards">
                <div class="card">
                    <img src="../../assets/images/42ec7ef0-0974-468c-9895-1d9d88bab013.png" alt="">
                </div>
                <div class="card">
                    <img src="../../assets/images/5c74b65b-9555-4a56-85be-9420193b5a52.png" alt="">
                </div>
                <div class="card">
                    <img src="../../assets/images/5c74b65b-9555-4a56-85be-9420193b5a52 (2).png" alt="">
                </div>
                <div class="card">
                    <img src="../../assets/images/instalaciones.png" alt="">
                </div>
            </section> 
        </section>
        <section class="reservas">
            <div class="titulo_reservas">
                <h1>
                    RESERVAS
                </h1>
            </div>
            <div class="texto_btn">
                <div class="texto_reservas">
                    <p>Nuestro glamping está disponible los 365 días del año, reserva tu plaza ya.</p>
                </div>
                <div class="div_btn">
                    <button class="btn_reserva" @click="goReservas" >RESERVA AHORA</button>
                </div>
            </div>  
        </section>
        <section class="alojamientos">
            <div class="titulo_alojamientos">
                <h1>ALOJAMIENTOS</h1> 
            </div>
            <div class="texto_img">
                <div class="imagen">
                    <img src="../../assets/images/5c74b65b-9555-4a56-85be-9420193b5a52 (1).png" alt="">
                </div>
                <div class="texto_alojamientos">
                    <button class="btn_alojamientos" @click="goAlojamientos" >VER EN DETALLE</button>
                    <p>Nuestros alojamientos ofrecen el ambiente perfecto para la relajación y el descanso</p>
                </div>
            </div>
        </section>
        <Footer></Footer>
    </main>
  
</template>

<script setup>
    import Header from '@/components/Header.vue';
    import Footer from '@/components/Footer.vue';
    import { useRouter } from 'vue-router';
    const router = useRouter()
    const goAlojamientos = () => {
        router.push("/alojamientos")
    }
    const goReservas = () => {
        router.push("/reservas")
    }


</script>

<style scoped lang="sass">
    @use "../../assets/sass/variables" 
    @use "../../assets/sass/mixins"

    .intro
        padding: 4rem
        @include mixins.flexbox($d: flex, $fd: column , $jc: center , $gap: 3rem )
        text-align: center
        background: variables.$color_background_principal
        h1
            font-family: variables.$tipografia_titulo
            color: variables.$color_texto_principal
        p
            font-family: variables.$tipografia_texto

    .instalaciones
        @include mixins.flexbox($d: flex, $fd: column, $jc: start , $gap: 0 )
        background: #F8F6F1
        .titulo_instalaciones
            background: variables.$color_boton_principal
            padding: 1.5rem
            h1
                font-family: variables.$tipografia_titulo
                color: variables.$color_background_secundario
        .cards
            background: variables.$color_background_secundario
            padding: 1rem
            @include mixins.flexbox($d: flex, $fd: row , $jc: start , $gap: 20px)
            overflow-x: auto 
            scroll-behavior: smooth
            .card
                background: variables.$color_background_secundario
                min-width: 500px              
                img
                    transition: 0.4s ease
                    width: 100%
                    height: 320px
                    object-fit: cover
                    border-radius: 12px
                    &:hover
                        scale: 1.03         
    .reservas
        background: #F8F6F1
        @include mixins.flexbox($d: flex, $fd: column, $jc: end , $gap: 0 )
        text-align: end
        .titulo_reservas
            background: variables.$color_boton_principal
            padding: 1.5rem
            h1
                font-family: variables.$tipografia_titulo
                color: variables.$color_background_secundario
        .texto_btn
            padding: 3rem
            @include mixins.flexbox($d: flex, $fd: row, $jc: center, $gap: 4rem )
            .texto_reservas
                @include mixins.flexbox($d: flex , $fd: column, $jc: center , $gap: 0 )
                font-size: 32px
                text-align: center  
                font-family: variables.$tipografia_texto
            .div_btn
                padding: 4rem
                .btn_reserva
                    background: variables.$color_boton_principal
                    border: none
                    border-radius: 12px
                    padding: 2rem 4rem
                    color: variables.$color_background_secundario
                    font-family: variables.$tipografia_texto
                    font-size: 20px 
                    cursor: pointer
                    &:hover 
                        scale: 1.05 
                        transition: ease-in-out 0.3s
                        background: variables.$color_hover_principal
            
    .alojamientos
        @include mixins.flexbox($d: flex, $fd: column, $jc: start , $gap: 0 )
        background: #F8F6F1   
        .titulo_alojamientos
            background: variables.$color_boton_principal
            padding: 1.5rem
            h1
                font-family: variables.$tipografia_titulo
                color: variables.$color_background_secundario
        .texto_img
            @include mixins.flexbox($d: flex, $fd: row , $jc: center , $gap: 4rem )
            .imagen
                min-width: 500px
                overflow: hidden
                padding: 1rem
                img
                    width: 100%
                    height: 320px
                    object-fit: cover
                    border-radius: 12px
            .texto_alojamientos
                padding: 1rem
                @include mixins.flexbox($d: flex, $fd: column, $jc: center, $gap: 2rem )
                align-items: center
                p
                    font-family: variables.$tipografia_texto
                    font-size: 20px
                .btn_alojamientos
                    border: none
                    background: variables.$color_boton_principal
                    border-radius: 12px
                    padding: 2rem 3rem
                    color: variables.$color_background_secundario
                    font-family: variables.$tipografia_texto
                    font-size: 20px 
                    cursor: pointer
                    &:hover 
                        scale: 1.05 
                        transition: ease-in-out 0.3s
                        background: variables.$color_hover_principal


        

        
            

        

</style>