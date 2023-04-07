<template>
    <li class="list-group-item d-flex justify-content-between">
        <span>{{ tituloFilmeConcatenado }} - Ano: {{ ano }}</span>
        <button class="btn btn-success">Selecionar</button>
    </li>
</template>


<script>
export default {
    props: {
        titulo: {
            type: String,
            required: true,
            validator() {
                return true;
            }
        },
        ano: {
            type: Number,
            required: true
        }
    },
    created() {
        console.log("Título do filme: " + this.titulo);
    },
    computed: {
        tituloFilmeConcatenado() {
            return `Título: ${this.titulo}`
        }
    }
}
</script>