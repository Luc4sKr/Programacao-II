function form_post(e) {
    e.preventDefault;

    var rota = `http://localhost:5000/login`;

    var vetor_dados = $("#form_login").serializeArray();

    var chave_valor = {};
    for (var i = 0; i < vetor_dados.length; i++) {
        chave_valor[vetor_dados[i]['name']] = vetor_dados[i]['value'];
    }

    var dados_json = JSON.stringify(chave_valor);

    var acao = $.ajax({
        url: rota,
        method: 'POST',
        dataType: 'json',
        contentType: 'application/json',
        data: dados_json
    });

    acao.done(function (retorno) {
        try {
            if (retorno.resultado == "ok") {
                alert("tudo certo");
            } else {
                alert("Deu algum erro no backend: " + retorno.detalhes);
            }
        } catch (error) { // se algo der errado...
            alert("Erro ao tentar fazer o ajax: " + error +
                "\nResposta da ação: " + retorno);
        }
    });
}

$("#btn_form").on("click", function() {
    form_post();
});