<template>
    <header>
        <div class="title-container">
            <h1>CADASTRO</h1>
        </div>
        <div class="list-container">
            <ul>
                <li>PESSOA</li>
                <li>CELULAR</li>
            </ul>
        </div>
    </header>
</template>


<script>
export default {
    name: "HeaderComponent"
}
</script>


<style scoped>
header {
    height: 100px;
    background-color: var(--green);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.title-container {
    display: block;
}

.list-container {
    display: block;
}

.list-container > ul {
    list-style: none;
    display: flex;
}

.list-container > ul > li {
    margin-left: 10px;
    margin-right: 10px;
}
</style>