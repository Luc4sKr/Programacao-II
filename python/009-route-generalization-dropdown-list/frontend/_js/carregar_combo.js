export function carregar_combo(combo_id, nome_classe) {
    var acao = $.ajax({
        url: 'http://localhost:5000/listar/' + nome_classe,
        dataType: 'json', // os dados são recebidos no formato json
    });

    // se a chamada der certo
    acao.done(function (retorno) {
        try {
            if (retorno.resultado == "ok") {
                montar_combo(combo_id, retorno.detalhes);
            } else {
                alert("Deu algum erro no backend: " + retorno.detalhes);
            }
        } catch (error) { // se algo der errado...
            alert("Erro ao tentar fazer o ajax: " + error +
                "\nResposta da ação: " + retorno.detalhes);
        }
    });

    // se a chamada der erro
    acao.fail(function (jqXHR, textStatus) {
        mensagem = encontrarErro(jqXHR, textStatus, rota);
        alert("Erro na chamada ajax: " + mensagem);
    });

    function montar_combo(combo_id, dados) {
        // esvaziar o combo
        $('#' + combo_id).empty();
        // percorrer a lista de dados
        for (var linha of dados) {
            $('#' + combo_id).append(
                $('<option></option>').attr("value",
                    linha.id).text(linha.nome));
        }
    }
}
