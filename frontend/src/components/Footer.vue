<template>
    <footer>
        <div class="texto">
            <p class="copy">2026, todos los derechos reservados</p>
            <p>VORA MAR GLAMPING®</p> 
        </div>
        <div class="icons">
            <FontAwesomeIcon :icon="faInstagram" />
            <FontAwesomeIcon :icon="faTiktok" />
            <FontAwesomeIcon :icon="faYoutube" />
            <FontAwesomeIcon :icon="faFacebook" />
        </div>
    </footer>
    
</template>

<script setup>
    import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
    import {
        faInstagram,
        faTiktok,
        faYoutube,
        faFacebook
    } from '@fortawesome/free-brands-svg-icons'



</script>

<style scoped lang="sass">
    @use "../assets/sass/variables"
    @use "../assets/sass/mixins"
    footer
        box-shadow: 0 10px 30px rgba(0,0,0,0.08)
        padding: 2rem 3rem 
        @include mixins.flexbox($d: flex , $fd: row , $jc: space-around , $gap: 0 )
        align-items: center
        background: variables.$color_texto_principal
        color: variables.$color_background_secundario
        .texto
            @include mixins.flexbox($d: flex, $fd: row , $jc: start , $gap: 8px)
            text-align: start
            width: 50%
        .icons
            @include mixins.flexbox($d: flex, $fd: row , $jc: end , $gap: 1rem )
            width: 50%
    @media (max-width: 768px)  
        footer
            padding: 10px 15px 
            font-size: 12px 
            .texto
                padding: 10px 15px
                @include mixins.flexbox($d: flex, $fd: row , $jc: start, $gap: 2rem )
                .copy
                    font-size: 8px
            .icons
                @include mixins.flexbox($d: flex , $fd: row , $jc: end, $gap: 8px )
                      
            

        
</style>