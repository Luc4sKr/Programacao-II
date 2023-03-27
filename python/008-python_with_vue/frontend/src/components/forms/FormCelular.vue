<template>
    <div class="form-container">
        <form class="form" id="form-celular" action="post">
            <h2>CELULAR</h2>
            <div class="form-controller">
                <label for="marca">Marca</label>
                <input type="text" name="marca" id="marca">
            </div>
            <div class="form-controller">
                <label for="modelo">Modelo</label>
                <input type="text" name="modelo" id="modelo">
            </div>
            <div class="form-controller">
                <label for="proprietario">Proprietario</label>
                <input type="text" name="proprietario" id="proprietario">
            </div>
            <div class="form-controller">
                <button type="submit">Cadastrar</button>
            </div>
        </form>
    </div>
</template>

<script>
export default {
    name: "FormCelular"
}
</script>

<style scoped>

</style>