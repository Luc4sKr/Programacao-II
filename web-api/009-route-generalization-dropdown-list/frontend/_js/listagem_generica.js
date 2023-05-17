export function listagem_generica(nome_classe, id_element, lista_campos) {

    // chamada ao backend
    var rota = `http://localhost:5000/listar/${nome_classe}`;

    // chamada ajax
    var acao = $.ajax({
        url: rota,
        dataType: 'json', // os dados são recebidos no formato json,
    });

    // se a chamada der certo
    acao.done(function (retorno) {
        // faz uma proteção contra erros
        try {
            if (retorno.resultado == "ok") {

                retorno.detalhes.forEach(pessoa => {
                    let tr = document.createElement("tr");

                    lista_campos.forEach(campo => {
                        let td = document.createElement("td");
                        td.innerText = `${pessoa[campo]}`;

                        tr.appendChild(td);
                    });
                    
                    document.querySelector(`#${id_element}`).appendChild(tr);
                });

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
        mensagem = encontrarErro(jqXHR, textStatus, rota);
        alert("Erro na chamada ajax: " + mensagem);
    });
}
