<template>
    <main>
        <Header></Header>
        <h1 class="titulo_reservas">MIS RESERVAS</h1>
        <div class="sin_reservas" v-if=" reservas.length === 0">
            <h1 class="titulo_nada">No tienes reservas todavía</h1>
            <button class="reservas" @click="goReservas" >Ve a reservas</button>
        </div>
        <section class="mis_reservas">
            <div class="card_reservas" v-for="reserva in reservas" :key="reserva.id">
                <h2>{{ reserva.nombre }}</h2>
                <p><strong>Entrada:</strong> {{ reserva.fecha_inicio }}</p>
                <p><strong>Salida:</strong> {{ reserva.fecha_fin }}</p>
                <p><strong>Estado:</strong> {{ reserva.estado }}</p>
                <p><strong>Alojamiento:</strong> {{ reserva.nombre }}</p>
                <div class="btn_cancelar">
                    <button v-if="reserva.estado != 'cancelada'" @click="cancelar(reserva.id)">Cancelar</button>
                </div>
                </div>
            </section>
        <Footer></Footer>
    </main>
  
</template>

<script setup>
    import Header from '@/components/Header.vue';
    import Footer from '@/components/Footer.vue';
    import { getReservasUsuario, cancelarReserva } from '@/services/reservaService';
    import { onMounted, ref } from 'vue';
    import { useRouter } from 'vue-router';
    
    const router = useRouter()
    const goReservas = () => {
        router.push("/reservas")
    }   
    const reservas = ref([])
    const user = JSON.parse(localStorage.getItem("user"))
    const fetchReservas = async () => {
        try {
            const response = await getReservasUsuario(user.id)
            reservas.value = response.data
        } catch (error) {
            console.log(error)
        }
    }
    const cancelar = async (id) => {

        try {
            await cancelarReserva(id)
            fetchReservas()
        } catch (error) {
            console.log(error)
        }
    }
    onMounted(() => {

        fetchReservas()
    })

</script>

<style scoped lang="sass">
    @use "../../assets/sass/variables" 
    @use "../../assets/sass/mixins"
    main
        .titulo_reservas
            text-align: center
            color: variables.$color_texto_principal
            background: variables.$color_background_secundario
            padding: 1rem
        .sin_reservas
            height: 50vh
            font-family: variables.$tipografia_texto
            @include mixins.flexbox($d: flex , $fd: row , $jc: center , $gap: 3rem )
            align-items: center
            text-align: center
            background: variables.$color_background_secundario
            button
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
        .mis_reservas
            background: variables.$color_background_secundario
            display: flex
            flex-wrap: wrap
            flex-direction: row
            gap: 1rem
            padding: 2rem
            justify-content: center
            text-align: center
            .card_reservas
                width: 40%
                background: white
                @include mixins.flexbox($d: flex , $fd: column , $jc: center, $gap: 1rem )
                font-family: variables.$tipografia_texto
                box-shadow: 0 10px 30px rgba(0,0,0,0.08)
                padding: 2rem
                border-radius: 20px
                text-align: center
                &:hover
                    scale: 1.03
                    transition: ease-in-out 0.3s
                .btn_cancelar
                    align-items: center
                    button
                        padding: 1rem
                        background: variables.$color_alternativo
                        border-radius: 20px
                        border: none
                        color: white
                        cursor: pointer
                        &:hover
                            scale: 1.03
                            transition: ease-in-out 0.3s
    @media (max-width:768px)
        main
            .sin_reservas
                height: 60vh
            .mis_reservas
                min-height: 69vh
                @include mixins.flexbox($d: flex , $fd: column , $jc: center , $gap: 1rem)
                flex-wrap: none
                .card_reservas
                    width: 100%
                    
                
            
</style>