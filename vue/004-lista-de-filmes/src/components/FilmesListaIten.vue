<template>
    <li class="list-group-item d-flex justify-content-between">
        <span>{{ tituloFilmeConcatenado }}</span>
        <button class="btn btn-success">Selecionar</button>
    </li>
</template>


<script>
export default {
    props: {
        tituloFilme: {
            type: String,
            required: true,
            validator() {
                return true;
            }
        }
    },
    created() {
        console.log("Título do filme: " + this.tituloFilme);
    },
    computed: {
        tituloFilmeConcatenado() {
            return `Título: ${this.tituloFilme}`
        }
    }
}
</script>