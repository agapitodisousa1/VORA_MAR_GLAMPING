<template>
    <main>
        <Header></Header>
        <section class="main">
            <div class="spa">
                <div class="texto_spa">
                    <h1>SPA</h1>
                    <p>Disfruta de nuestro spa premium y de todas sus comodidades incluido en el precio total
                        
                    </p>
                </div>
                <div class="imagen_spa">
                    <img src="../../assets/images/spa.png" alt="">
                </div>
            </div>
            <div class="yoga">
                <div class="imagen_yoga">
                    <img src="../../assets/images/zona_yoga.png" alt="">
                </div>
                <div class="texto_yoga">
                    <h1>ZONA DE YOGA</h1>
                    <p>También disponemos de una zona para la práctica del yoga para una máxima relajación y aprovechamiento del tiempo</p>
                </div>
            </div>
            <div class="mar">
                <div class="texto_mar">
                    <h1>MAR</h1>
                    <p>Tenemos acceso directo al mar desde nuestras instalaciones. Podrás disfrutar de un cálido baño cada vez que lo necesites</p>
                </div>
                <div class="imagen_mar">
                    <img src="../../assets/images/5c74b65b-9555-4a56-85be-9420193b5a52 (1).png" alt="">
                </div>
            </div>
        </section>
        <Footer></Footer>

    </main>
    
</template>

<script setup>
    import Footer from '@/components/Footer.vue'; 
    import Header from '@/components/Header.vue';      

</script>

<style scoped lang="sass">
    @use "../../assets/sass/variables" 
    @use "../../assets/sass/mixins"
    main
        .main
            background: variables.$color_background_principal
            @include mixins.flexbox($d: flex, $fd: column, $jc: center, $gap: 1rem )
            .spa
                margin: 1rem
                border-radius: 20px
                background: variables.$color_background_secundario
                padding: 1rem
                @include mixins.flexbox($d: flex , $fd: row , $jc: center , $gap: 1rem )
                .texto_spa
                    h1
                        color: variables.$color_texto_principal
                        font-family: variables.$tipografia_titulo
                    p
                        font-family: variables.$tipografia_texto
                    @include mixins.flexbox($d: flex, $fd: column   , $jc: center, $gap: 1rem )
                    text-align: center
                .imagen_spa
                    padding: 2rem
                    img
                        border-radius: 20px
                        width: 500px  
                        &:hover
                            scale: 1.03
                            transition: ease-in-out 0.3s 
            .yoga
                margin: 1rem
                background: variables.$color_background_secundario
                padding: 1rem
                border-radius: 20px
                @include mixins.flexbox($d: flex, $fd: row , $jc: center, $gap: 1rem )
                .texto_yoga
                    h1 
                        font-family: variables.$tipografia_titulo
                        color: variables.$color_texto_principal
                    p
                        font-family: variables.$tipografia_texto
                    @include mixins.flexbox($d: flex, $fd: column , $jc: center, $gap: 1rem )
                    text-align: center
                .imagen_yoga
                    padding: 2rem
                    img
                        border-radius: 20px
                        width: 500px  
                        &:hover
                            scale: 1.03
                            transition: ease-in-out 0.3s 
            .mar
                margin: 1rem
                background: variables.$color_background_secundario
                padding: 1rem
                border-radius: 20px
                @include mixins.flexbox($d: flex, $fd: row , $jc: center, $gap: 1rem )
                .texto_mar
                    h1 
                        font-family: variables.$tipografia_titulo
                        color: variables.$color_texto_principal
                    p
                        font-family: variables.$tipografia_texto
                    @include mixins.flexbox($d: flex, $fd: column , $jc: center, $gap: 1rem )
                    text-align: center
                .imagen_mar
                    padding: 2rem
                    img
                        border-radius: 20px
                        width: 500px  
                        &:hover
                            scale: 1.03
                            transition: ease-in-out 0.3s 

    @media (max-width: 768px)
        main
            .main
                .spa
                    @include mixins.flexbox($d:flex, $fd: column , $jc: center , $gap: 1rem)
                    align-items: center
                    .imagen_spa
                        img
                            width: 250px
                .yoga
                    @include mixins.flexbox($d:flex, $fd: column , $jc: center , $gap: 1rem)
                    align-items: center
                    .imagen_yoga
                        img
                            width: 250px
                .mar
                    @include mixins.flexbox($d:flex, $fd: column , $jc: center , $gap: 1rem)
                    align-items: center
                    .imagen_mar
                        img 
                            width: 250px
            

</style>