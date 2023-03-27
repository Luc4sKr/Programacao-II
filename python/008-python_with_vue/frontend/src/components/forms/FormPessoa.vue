<template>
    <div class="form-container">
        <form id="form-pessoa" class="form" action="post">
            <h2>PESSOA</h2>
            <div class="form-controller">
                <label for="nome">Nome</label>
                <input type="text" name="nome" id="nome" v-model="input_name">
            </div>
            <div class="form-controller">
                <label for="email">Email</label>
                <input type="email" name="email" id="email" v-model="input_email">
            </div>
            <div class="form-controller">
                <button type="submit" v-on:click="submitForm">Cadastrar</button>
            </div>
        </form>
    </div>
</template>


<script>
import axios from "axios";

const route = "http://localhost:5000/incluir_pessoa";

export default {
    name: "FormPessoa",

    data() {
        return {
            input_name: "",
            input_email: ""
        }

    },

    methods: {
        getFormData: function () {
            let nome = this.input_name;
            let email = this.input_email;

            return {
                nome,
                email
            }
        },

        submitForm: function (event) {
            event.preventDefault();

            axios.post(route, this.getFormData())
                .then(function (response) {
                    console.log(response)
                    if (response.data.resultado == "ok") {
                        alert("registro inserido");
                    } else {
                        alert("Algo de errado" + response.data.detalhes);
                    }
                })
                .catch(function(error) {
                    alert("Erro: " + error);
                });
        }
    }
}
</script>


<style scoped></style>