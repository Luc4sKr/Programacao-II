<template>
    <h1>Hello World</h1>
    <p>{{ url }}</p>
</template>

<script>
export default {
    data: () => ({
        url: process.env.VUE_APP_URL
    })
}
</script>

<style lang="scss">

</style>