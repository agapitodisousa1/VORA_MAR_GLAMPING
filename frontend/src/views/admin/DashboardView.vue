<template>
    <main>
        <Header></Header>
        <section class="main">
            <div class="stats">
                <h1>ESTADÍSTICAS</h1>
                <p><strong>Total reservas: </strong>{{ totalReservas }}</p>
                <p><strong>Ingresos: </strong>{{ ingresos }}€</p>
                <p><strong>Usuarios totales: </strong>{{ totalUsuarios }}</p>
                <p><strong>Alojamientos totales: </strong>{{ totalAlojamientos }}</p>
                <p><strong>Reservas confirmadas: </strong>{{ confirmadas }}</p>
                <p><strong>Reservas pendientes: </strong>{{ pendientes }} </p>
                <p><strong>Reservas canceladas: </strong>{{ canceladas }}</p>
            </div>
            <div class="reservas">
                <div class="card_reservas" v-for="reserva in reservas" :key="reserva.id">
                    <h2>{{ reserva.nombre }}</h2>
                    <p><strong>Entrada:</strong> {{ reserva.fecha_inicio }}</p>
                    <p><strong>Salida:</strong> {{ reserva.fecha_fin }}</p>
                    <p><strong>Estado:</strong> {{ reserva.estado }}</p>
                    <p><strong>Alojamiento:</strong> {{ reserva.nombre }}</p>
                    <div class="botones">
                        <button class="btn_cancelar" v-if="reserva.estado != 'cancelada'" @click="cancelar(reserva.id)">Cancelar</button>
                        <button class="btn_confirmar" v-if="reserva.estado === 'pendiente'" @click="confirmar(reserva.id)">Confirmar</button>
                    </div>
            </div>

            </div>

        </section>
        
        <Footer></Footer>
    </main>

  
</template>

<script setup>
    import Header from '@/components/Header.vue';
    import Footer from '@/components/Footer.vue';
    import { getDashboard } from '@/services/dashboardService';
    import { ref, onMounted } from 'vue';
    import { confirmarReserva } from '@/services/dashboardService';
    import { cancelarReserva } from '@/services/reservaService';

    const stats = ref([])
    const reservas = ref([])
    const totalReservas = ref(0)
    const ingresos = ref(0)
    const totalUsuarios = ref(0)
    const totalAlojamientos = ref(0)
    const confirmadas = ref(0)
    const canceladas = ref(0)
    const pendientes = ref(0)
    const fetchDashboard = async () => {

        try {
            const response = await getDashboard()
            stats.value = response.data
            reservas.value = response.data.reservas
            totalReservas.value = response.data.total_reservas
            ingresos.value = response.data.ingresos
            totalUsuarios.value = response.data.total_usuarios
            totalAlojamientos.value = response.data.total_alojamientos
            pendientes.value = response.data.pendientes
            confirmadas.value = response.data.confirmadas
            canceladas.value = response.data.canceladas
        } catch (error) {
            console.log(error)
        }
    }
    const confirmar = async (id) => {
        try { 
            await confirmarReserva(id)
            await fetchDashboard()
        } catch (error) { 
            console.log(error)
        }

    }
    const cancelar = async (id) => {
        try { 
            await cancelarReserva(id)
            await fetchDashboard()
        } catch (error) { 
            console.log(error)
        }
    }
    onMounted(() => {
        fetchDashboard()
    })
</script>

<style scoped lang="sass">
    @use "../../assets/sass/variables" 
    @use "../../assets/sass/mixins"
    main
        .main
            @include mixins.flexbox($d: flex, $fd: column, $jc: center , $gap: 1rem)
            text-align: center
            background: variables.$color_background_principal
            .stats
                border-radius: 20px
                padding: 2rem
                margin: 1rem
                background: variables.$color_background_secundario
                @include mixins.flexbox($d: flex, $fd: column , $jc: center, $gap: 1rem)
                h1
                    font-family: variables.$tipografia_titulo
                p
                    font-family: variables.$tipografia_texto
            .reservas
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
                    .botones
                        @include mixins.flexbox($d: flex, $fd: row, $jc: center, $gap: 1rem )
                        align-items: center
                        .btn_cancelar   
                            padding: 1rem
                            background: variables.$color_boton_secundario
                            border-radius: 20px
                            border: none
                            color: white
                            cursor: pointer
                            &:hover
                                background: variables.$color_hover_secundario
                                scale: 1.03
                                transition: ease-in-out 0.3s
                        .btn_confirmar
                            padding: 1rem
                            background: variables.$color_alternativo
                            border-radius: 20px
                            border: none
                            color: white
                            cursor: pointer
                            &:hover
                                scale: 1.03
                                transition: ease-in-out 0.3s
    @media (max-width: 768px)
        main
            .main
                .reservas
                    .card_reservas
                        width: 100%

</style>