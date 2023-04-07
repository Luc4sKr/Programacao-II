<template>
    <li class="list-group-item d-flex justify-content-between">
        <span>{{ tituloFilme }}</span>
        <button class="btn btn-success">Selecionar</button>
    </li>
</template>


<script>
export default {
    props: ["tituloFilme"]
}
</script>