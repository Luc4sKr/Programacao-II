import { findError } from './utils.js';


$(document).ready(function () {
    var rota = 'http://localhost:5000/list_person';

    // chamada ajax
    var acao = $.ajax({
        url: rota,
        method: 'GET',
        dataType: 'json',
    });

    // se a chamada der certo
    acao.done(function (retorno) {
        // faz uma proteção contra erros
        try {
            if (retorno.resultado == "ok") {
                for (var p of retorno.detalhes) {
                    let tr = document.createElement("tr");

                    let name = document.createElement("th");
                    let email = document.createElement("th");
                    let phone = document.createElement("th")

                    $(name).text(p.name);
                    $(email).text(p.email);
                    $(phone).text(p.phone);

                    $(tr).append(name);
                    $(tr).append(email);
                    $(tr).append(phone);

                    $("#listagem").append(tr);
                }
            } else {
                alert("Erro informado pelo backend: " + retorno.detalhes);
            }
        } catch (error) { // se algo der errado...
            alert("Erro ao tentar fazer o ajax: " + error +
                "\nResposta da ação: " + retorno.detalhes);
        }
    });

    acao.fail(function (jqXHR, textStatus) {
        mensagem = findError(jqXHR, textStatus, rota);
        alert("Erro na chamada ajax: " + mensagem);
    });

});
