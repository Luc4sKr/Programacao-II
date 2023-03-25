<template>
    <div class="form-container">
        <form id="form-pessoa" action="post">
        <div class="form-controller">
            <label for="nome">Nome</label>
            <input type="text" name="nome" id="nome">
        </div>
        <div class="form-controller">
            <label for="email">Email</label>
            <input type="text" name="nome" id="nome">
        </div>
    </form>
    </div>
</template>


<script>
export default {
    name: "FormPessoa"
}
</script>


<style scoped>

</style>