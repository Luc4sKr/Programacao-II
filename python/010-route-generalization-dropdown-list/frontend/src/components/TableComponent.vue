<template>
    <table>
        <tr>
            <th></th>
        </tr>

        <tr>
            <td></td>
            <td></td>
        </tr>
    </table>
</template>


<script>
const axios = require("axios").default;

const URL = "http://127.0.0.1:5000/listar/ExameRealizado";

export default {
    data() {
        return {
            
        }
    },
    created() {
        
    },
    methods: {
        getData() {
            axios.get(URL)
            .then(function (response) {
                return response;
            }).catch(function (error) {
                return error;
            }).finally(function () {
                return
            });
        }
    }
}
</script>


<style></style>