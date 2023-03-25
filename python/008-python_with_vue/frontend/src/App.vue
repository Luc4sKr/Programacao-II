<template>
    <HeaderComponent />
    <div class="wrapper">
        <div class="form-center">
            <FormsComponent />
        </div>
    </div>
</template>


<script>
import HeaderComponent from './components/HeaderComponent.vue';
import FormsComponent from './components/FormsComponent.vue';

export default {
    name: 'App',
    components: {
        HeaderComponent,
        FormsComponent
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

.form-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 500px;
    background-color: var(--dark-blue);
    margin-top: 50px;
    margin-bottom: 50px;
}

.form-center {
    color: var(--white);
    display: flex;
    justify-content: center;
}
</style>
