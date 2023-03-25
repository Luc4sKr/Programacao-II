<template>
	<h1>Conversor</h1>
	<div id="app">
		<ConversorComponent coinA="USD" coinB="BRL"/>
	</div>
</template>


<script>
import ConversorComponent from "./components/ConversorComponent.vue";

export default {
	name: 'App',
	components: {
		ConversorComponent
	}
}
</script>


<style>
#app {
	font-family: Avenir, Helvetica, Arial, sans-serif;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	text-align: center;
	color: #2c3e50;
	margin-top: 60px;
}
</style>
