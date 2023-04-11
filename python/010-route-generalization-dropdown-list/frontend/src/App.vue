<template>
    <HeaderComponent />

    <div>
        <TableComponent />
    </div>
</template>

<script>
import HeaderComponent from "./components/HeaderComponent.vue";
import TableComponent from "./components/TableComponent.vue";

export default {
    name: 'App',
    components: {
        HeaderComponent,
        TableComponent
    }
}
</script>

<style>
:root {
    --gray-blue: #35495e;
    --green: #42b883;
    --white: #000;
}

* {
    padding: 0px;
    margin: 0px;
}

#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
}
</style>
