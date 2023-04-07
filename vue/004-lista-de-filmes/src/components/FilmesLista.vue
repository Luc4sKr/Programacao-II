<template>
    <div class="row">

        <!-- coluna 1 -->
        <div class="col-8">

            <h2>Filmes</h2>

            <div class="list-group list-group-flush">


                <FilmesListaIten
                    v-for="filme in filmes"
                    :key="filme.id" 
                    v-bind="filme" 
                />

            </div>
        </div>

        <!-- coluna 2 -->
        <div class="col-4">

            <FilmesListaItenInfo />

        </div>

    </div>
</template>

<script>

import FilmesListaIten from './FilmesListaIten.vue'
import FilmesListaItenInfo from './FilmesListaItenInfo.vue'

export default {
    components: {
        FilmesListaIten,
        FilmesListaItenInfo
    },
    data() {
        return {
            filmes: [
                { id: 1, titulo: "Vingadores: Guerra Infinita", ano: 2000 },
                { id: 2, titulo:"Nada de Novo no Front", ano: 2000 },
                { id: 3, titulo: "O Jogo da Imitação", ano: 2000 },
                { id: 4, titulo: "Deadpool 2", ano: 2000 }
            ]
        }

    }
}
</script>
