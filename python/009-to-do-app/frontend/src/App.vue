<template>
    <HeaderComponent />
    <div class="wrapper">
        <div class="form-container">
            <FormComponent />
        </div>
    </div>
</template>

<script>
import HeaderComponent from './components/HeaderComponent.vue';
import FormComponent from './components/FormComponent.vue';

export default {
  name: 'App',
  components: {
    HeaderComponent,
    FormComponent
  }
}
</script>

<style>
:root {
    --header-bg: #343a40;
    --background-color: #e9ecef;
}

* {
    margin: 0px;
    padding: 0px;
    font-family: sans-serif;
}

body {
    background-color: var(--background-color);
}

.wrapper {
    width: 80%;
    margin: 0 auto;
}

.form-container {
    width: 100%;
    margin-top: 30px;
    display: flex;
    justify-content: center;
}
</style>
