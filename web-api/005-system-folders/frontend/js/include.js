import { findError } from './utils.js';

// proteção para não executar o javascript antes do documento estar pronto
$(document).ready(function () {

    $(document).on("click", "#btn-enviar", function (e) {
        e.preventDefault();

        // rota que vai ser chamada no backend
        var rota = 'http://localhost:5000/include_person';

        const name = $("#name").val()
        const email = $("#email").val()
        const phone = $("#phone").val()

        var newData = {
            "name": name,
            "email": email,
            "phone": phone
        }

        // convertendo para JSON!!
        var dados_json = JSON.stringify(newData);

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
                    alert("tudo certo :-)");
                } else {
                    alert("Deu algum erro :-( " + retorno.detalhes);
                }
            } catch (error) { // se algo der errado...
                alert("Erro ao tentar fazer o ajax: " + error +
                    "\nResposta da ação: " + retorno);
            }
        });

        // se a chamada der erro
        acao.fail(function (jqXHR, textStatus) {
            mensagem = findError(jqXHR, textStatus, rota);
            alert("Erro na chamada ajax: " + mensagem);
        });

    });

});
