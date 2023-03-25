<template>
    <div class="conversor">
        <h2>{{ coinA }} para {{ coinB }}</h2>
        <input type="text" v-moel="coinA_value" v-bind:placeholder="coinA">
		<input type="button" value="convert">
        <h3>{{ coinB_value }}</h3>
    </div>
</template>


<script>
export default {
    name: "ConversorComponent",
    props: ["coinA", "coinB"],

    data() {
        return {
            coinA_value: "",
            coinB_value: 0
        }
    },

    methods: {
        convert() {
            
        }
    }
}
</script>


<style scoped>

</style>
