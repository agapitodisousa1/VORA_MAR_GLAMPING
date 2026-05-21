<template>
    <main>
        <Header></Header>
        <section class="main">
            <h1>404 Página no encontrada</h1>
            <p>Lo sentimos, la página que buscas no existe</p>
            <img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExMXB2MXNhOHRxY3QzdTZkNWI5azNoamJscjRyajI3bThxdzJsZWgzbSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/9J7tdYltWyXIY/giphy.gif" alt="">
            <button @click="goHome">Volver a la página de inicio</button>
        </section>
        <Footer></Footer>
    </main>

  
</template>

<script setup>
    import Header from '@/components/Header.vue';
    import Footer from '@/components/Footer.vue';
    import { useRouter } from 'vue-router';

    const router = useRouter()
    const goHome = () => {
        router.push("/")
    }

</script>

<style scoped lang="sass">
    @use "../../assets/sass/variables" 
    @use "../../assets/sass/mixins"
    main
        .main
            background: variables.$color_background_secundario
            @include mixins.flexbox($d: flex, $fd: column , $jc: center , $gap: 1rem )
            text-align: center
            font-family: variables.$tipografia_texto
            padding: 1rem   
            width: 100%
            align-items: center
            h1
                color: variables.$color_texto_principal 
            img
                width: 20%
                border-radius: 20px 
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
    @media (max-width: 768px)
        main
            .main
                height: 79vh  
                img
                    width: 50%

                         
    
</style>