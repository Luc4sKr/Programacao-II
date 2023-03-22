new Vue({
    el: "#app",
    template: 
    `
    <div class="container">
        <h1>Comentários</h1>
        <hr />
        <div class="form-todo form-group">
            <p>
                <input placeholder="nome" type="text" name="author" class="form-control" v-model="name" />
            </p>
            <p>
                <textarea placeholder="Comentário" name="message"  class="form-control" v-model="message"></textarea>
            </p>
            <button v-on:click="addComment" type="submit" class="btn btn-primary">Comentar</button>
        </div>
        <div class="list-group">
            <div class="list-group-item" v-for="(comment, index) in comments">
                <span class="comment__author">Autor: <strong>{{ comment.name }}</strong></span>
                <p>{{ comment.message }}</p>
                <div>
                    <a href="#" title="Excluir" v-on:click.prevent="removeComment(index)">Excluir</a>
                </div>
            </div>
        </div>
        <hr />
    </div>
    `,
    data: function() {
        return {
            comments: [
                {
                    name: "Lucas",
                    message: "Lorem ipsum"
                }
            ]
        }
    }
});