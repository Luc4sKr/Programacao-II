import { encontrarErro } from "./error_function.js";

export function form_post(class_path) {
    // rota que vai ser chamada no backend
    // rota GENÉRICA :-)
    var rota = `http://localhost:5000/incluir/${class_path}`;

    // obter dados form
    var vetor_dados = $("#form_exam_reali").serializeArray();

    console.log(vetor_dados);

    // conversão para formato chave:valor
    var chave_valor = {};
    for (var i = 0; i < vetor_dados.length; i++) {
        chave_valor[vetor_dados[i]['name']] = vetor_dados[i]['value'];
    }

    // convertendo para JSON
    var dados_json = JSON.stringify(chave_valor);

    // chamada ajax
    var acao = $.ajax({
        url: rota,
        method: 'POST',
        dataType: 'json', // os dados são recebidos no formato json,
        contentType: 'application/json', // os dados serão enviados em json
        data: dados_json
    });

    // se a chamada der certo
    acao.done(function (retorno) {
        try {
            if (retorno.resultado == "ok") {
                alert("Exame realizado incluído");
            } else {
                alert("Deu algum erro no backend: " + retorno.detalhes);
            }
        } catch (error) { // se algo der errado...
            alert("Erro ao tentar fazer o ajax: " + error +
                "\nResposta da ação: " + retorno);
        }
    });

    // se a chamada der erro
    acao.fail(function (jqXHR, textStatus) {
        mensagem = encontrarErro(jqXHR, textStatus, rota);
        alert("Erro na chamada ajax: " + mensagem);
    });

}