<template>
    <main>
        <Header></Header>
        <section class="intro">
            <div class="texto">
                <h1>ALOJAMIENTOS</h1>
                <p>Tiendas Safari (mín. 19.6  m²) con aire acondicionado, baño privado completo y terraza chill-out con vistas.
                <br> <br>
                Colchones tamaño king, ropa de cama de algodón orgánico y amenidades cosméticas naturales y sostenibles de alta calidad y calidad hotelera. 
                <br> <br>
                Los interiores son minimalistas con toques naturales (madera, fibras) diseñados para reforzar un sentido de paz y armonía con el entorno costero.
                </p>
            </div>
            <div class="imagen">
                <img src="../../assets/images/alojamientos.png" alt="">
            </div>  
        </section>
        <div class="titulo">
            <h1>Elige una de entre nuestras 10 tiendas disponibles</h1>
        </div>
        <section class="cards" >
            <div class="card" v-for="alojamiento in alojamientos" :key="alojamiento.id">
                <h3>{{ alojamiento.nombre }}</h3>
                <p>{{ alojamiento.tipo }}</p>
                <p>Capacidad: {{ alojamiento.capacidad }} personas</p>
                <p><strong>{{ alojamiento.precio_base }}€</strong> / noche</p>
                <button @click="goReservas">RESERVAR</button>
            </div>
        </section>
        <Footer></Footer>
    </main>
  
</template>

<script setup>
    import Footer from '@/components/Footer.vue';
    import Header from '@/components/Header.vue';
    import { getAlojamientos } from "@/services/alojamientoService";
    import { ref, onMounted } from 'vue';
    import { useRouter } from 'vue-router';
    
    const alojamientos = ref([])
    const router = useRouter()
    const goReservas = () => {
        router.push("/reservas")
    }
    const fetchAlojamientos = async () => {

        try {
            const response = await getAlojamientos()
            alojamientos.value = response.data
        } catch (error) {
            console.log(error)
        }
    }
    onMounted(() => {
        fetchAlojamientos()
    })
</script>

<style scoped lang="sass">
    @use "../../assets/sass/variables" 
    @use "../../assets/sass/mixins"
    main
        .intro
            background: variables.$color_background_principal
            @include mixins.flexbox($d: flex , $fd: row , $jc: center, $gap: 1rem )
            .texto
                @include mixins.flexbox($d: flex, $fd: column , $jc: center , $gap: 3rem )                
                text-align: center
                padding: 2rem
                h1
                    font-family: variables.$tipografia_titulo
                    color: variables.$color_texto_principal
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
            background: variables.$color_background_secundario
            padding: 2rem
            font-family: variables.$tipografia_titulo    
            text-align: center
            width: 100%
            color: variables.$color_texto_principal
        .cards
            background: variables.$color_background_secundario
            display: flex
            flex-wrap: wrap
            gap: 1rem
            padding: 2rem
            justify-content: center
            .card
                background: white
                width: 17%
                @include mixins.flexbox($d: flex , $fd: column , $jc: center, $gap: 1rem )
                font-family: variables.$tipografia_texto
                box-shadow: 0 10px 30px rgba(0,0,0,0.08)
                padding: 2rem
                border-radius: 20px
                text-align: center
                &:hover
                    scale: 1.03
                    transition: ease-in-out 0.3s
                button
                    background: variables.$color_boton_principal
                    color: white
                    padding: 1rem
                    border-radius: 20px
                    border: none
                    cursor: pointer
                    &:hover
                        background: variables.$color_hover_principal
                        scale: 1.03
                        transition: ease-in-out 0.3s

</style>