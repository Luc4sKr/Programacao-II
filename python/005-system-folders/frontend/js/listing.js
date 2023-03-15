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
                // percorrer a lista de pessoas retornadas; 
                for (var p of retorno.detalhes) { //p vai valer cada pessoa do vetor de pessoas
                    // criar um parágrafo
                    var paragrafo = $("<p>");
                    // informar o HTML deste parágrafo
                    // observe o apóstrofo inclinado, para interpretar as variáveis
                    paragrafo.html(`==> ${p.name}, ${p.email}`);
                    // adicionar o parágrafo criado na div
                    $('#listagem').append(paragrafo);
                }
            } else {
                alert("Erro informado pelo backend: " + retorno.detalhes);
            }
        } catch (error) { // se algo der errado...
            alert("Erro ao tentar fazer o ajax: " + error +
                "\nResposta da ação: " + retorno.detalhes);
        }
    });

    // se a chamada der erro
    acao.fail(function (jqXHR, textStatus) {
        mensagem = findError(jqXHR, textStatus, rota);
        alert("Erro na chamada ajax: " + mensagem);
    });

});
