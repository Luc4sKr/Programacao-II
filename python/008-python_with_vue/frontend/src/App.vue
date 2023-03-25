<template>
    <HeaderComponent />
    <FormPessoa />
</template>


<script>
import HeaderComponent from './components/HeaderComponent.vue';
import FormPessoa from './components/FormPessoa.vue';

export default {
    name: 'App',
    components: {
        HeaderComponent,
        FormPessoa
    }
}
</script>


<style>
:root {
    --green: #41B883;
    --bluish-gray: #34495E;
}

* {
    margin: 0px;
    padding: 0px;
}

#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    color: var(--bluish-gray);
}

.form-container {
    display: block;
    
}
</style>
