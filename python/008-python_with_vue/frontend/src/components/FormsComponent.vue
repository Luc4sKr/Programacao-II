<template>
    <div class="form-container">
        <div class="hide">
            <form id="form-pessoa" action="post">
                <h2>PESSOA</h2>
                <div class="form-controller">
                    <label for="nome">Nome</label>
                    <input type="text" name="nome" id="nome">
                </div>
                <div class="form-controller">
                    <label for="email">Email</label>
                    <input type="email" name="email" id="email">
                </div>
            </form>
        </div>

        <div class="hide">
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
            </form>
        </div>
    </div>
</template>


<script>
const TABLE = Object.freeze({ Pessoa: 1, Celular: 2 });

export default {
    name: "FormsComponent",

    data() {
        return {
            
        }
    }
}
</script>


<style scoped>
.form {
    height: 280px;
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    align-items: center;
}

.form-controller {
    display: flex;
    flex-direction: column;
}

label {
    font-size: 18px;
}

input {
    outline: 0;
    background-color: var(--white);
    width: 100%;
    border: 0;
    margin: 0 0 15px;
    padding: 10px;
    box-sizing: border-box;
    font-size: 14px;
}
</style>