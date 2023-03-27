<template>
    <HeaderComponent />
    <div class="wrapper">
        <div class="forms-container">
            <FormPessoa />
            <FormCelular />
        </div>
    </div>
</template>


<script>
import HeaderComponent from './components/HeaderComponent.vue';

import FormPessoa from './components/forms/FormPessoa.vue';
import FormCelular from './components/forms/FormCelular.vue';

export default {
    name: 'App',
    components: {
        HeaderComponent,
        FormPessoa,
        FormCelular
    }
}
</script>


<style>
:root {
    --white: #ffffff;
    --green: #41B883;
    --gray-light: #a0b3b0;
    --bluish-gray: #34495E;
    --dark-blue: #13232f;
}

* {
    margin: 0px;
    padding: 0px;
}

#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    color: var(--dark-blue);
}

.wrapper {
    width: 80%;
    height: 100%;
    margin: 0 auto;;
}

.hide {
    display: none;
}

.forms-container {
    color: var(--white);
    display: flex;
    justify-content: space-evenly;
}

/* ESTILOS GLOBAIS DOS FORMULÁRIOS */
.form-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 380px;
    padding-top: 20px;
    padding-bottom: 20px;
    background-color: var(--dark-blue);
    margin-top: 50px;
    margin-bottom: 50px;
}

.form {
    height: 350px;
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    align-items: center;
}

.form-controller {
    display: flex;
    flex-direction: column;
}

.form label {
    font-size: 18px;
}

.form input {
    outline: 0;
    background-color: var(--white);
    width: 200px;
    border: 0;
    margin: 0 0 15px;
    padding: 10px;
    box-sizing: border-box;
    font-size: 14px;
}

.form button {
    width: 200px;
    height: 30px;
}
</style>
