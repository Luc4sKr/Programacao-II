import { form_post } from "./form_post.js";
import { carregar_combo } from "./carregar_combo.js";
import { listagem_generica } from "./listagem_generica.js";


$(function() {

    $(document).on("click", "#btn-incluir", function() {
        form_post("ExameRealizado");
    });

    // carregar combo de pessoas e exames
    carregar_combo("pessoa_id", "Pessoa");
    carregar_combo("exame_id", "Exame");

    // listagem genérica
    listagem_generica("Pessoa", "pessoas", ['id', 'nome', 'email', 'telefone']);

});