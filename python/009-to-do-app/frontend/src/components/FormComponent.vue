<template>
    <form>
        <div class="form-control">
            <label for="task">Task</label>
            <input type="text" name="task" id="task">
        </div>
        <div class="btn-container">
            <button type="submit" id="btn-submit">Add</button>
        </div>
    </form>
</template>


<script>
import { axios } from "axios"

export default {
    data() {
        return {

        }
    },
    methods: {
        add_tast() {
            
        }
    }
}
</script>


<style>
form {
    border: 1px solid #000;
    padding: 10px 30px;
}

.form-control {
    display: flex;
    flex-direction: column;
}

label {
    font-size: 18px;
    margin-bottom: 10px;
}

input {
    width: 300px;
    margin-bottom: 10px;
}

.btn-cntainer {
    display: block;
}

#btn-submit {
    float: right;
    width: 80px;
    height: 25px;
}
</style>