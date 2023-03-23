$(function () {

    /*
    
    INCLUIR PESSOA 
    
    */

    // conecta o botão de enviar à ação javascript/jquery
    $(document).on("click", "#btIncluirPessoa", function () {

        // rota que vai ser chamada no backend
        var rota = 'http://localhost:5000/incluir_pessoa';

        var vetor_dados = $("#meuformularioquerido").serializeArray();

        // converter para {chave:valor, chave:valor, ...}
        var chave_valor = {};
        for (var i = 0; i < vetor_dados.length; i++) {
            chave_valor[vetor_dados[i]['name']] = vetor_dados[i]['value'];
        }

        // convertendo para JSON!!
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
                    //alert("registro inserido!");
                    $("#mensagem").text("Registro incluído");
                    $("#mensagem").fadeOut(3000, function () {
                        // atualiza a página
                        location.reload(true);
                    });
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
            mensagem = encontrarErro(jqXHR, textStatus, rota);
            alert("Erro na chamada ajax: " + mensagem);
        });

    }); // fim click btIncluir pessoa

    /*

    INCLUIR CELULAR

    */

    // conecta o botão de enviar à ação javascript/jquery
    $(document).on("click", "#btIncluirCelular", function () {

        // rota que vai ser chamada no backend
        var rota = 'http://localhost:5000/incluir_celular';

        var vetor_dados = $("#form_celular").serializeArray();

        // converter para {chave:valor, chave:valor, ...}
        var chave_valor = {};
        for (var i = 0; i < vetor_dados.length; i++) {
            chave_valor[vetor_dados[i]['name']] = vetor_dados[i]['value'];
        }

        // convertendo para JSON!!
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
                    //alert("registro inserido!");
                    $("#mensagem").text("Registro incluído");
                    $("#mensagem").fadeOut(3000, function () {
                        // atualiza a página
                        location.reload(true);
                    });
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
            mensagem = encontrarErro(jqXHR, textStatus, rota);
            alert("Erro na chamada ajax: " + mensagem);
        });

    }); // fim click btIncluirCelular


    /*

    LISTAR PESSOAS

    */

    // chamada ao backend
    var rota = 'http://localhost:5000/listar_pessoas';

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
                // percorrer a lista de pessoas retornadas; 
                for (var p of retorno.detalhes) { //p vai valer cada pessoa do vetor de pessoas
                    // https://stackoverflow.com/questions/8069663/avoiding-html-in-string-html-in-a-jquery-script
                    // criar um parágrafo
                    var paragrafo = $("<p>");
                    // informar o HTML deste parágrafo
                    // observe o apóstrofo inclinado, para interpretar as variáveis
                    paragrafo.html(`==> ${p.nome}, ${p.email}`);
                    // adicionar o parágrafo criado na div
                    $('#listagem_pessoas').append(paragrafo);
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
        mensagem = encontrarErro(jqXHR, textStatus, rota);
        alert("Erro na chamada ajax: " + mensagem);
    });

     /*

    LISTAR CELULARES

    */

    // chamada ao backend
    var rota = 'http://localhost:5000/listar_celulares';

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
                // percorrer a lista de pessoas retornadas; 
                for (var p of retorno.detalhes) { //p vai valer cada pessoa do vetor de pessoas
                    // https://stackoverflow.com/questions/8069663/avoiding-html-in-string-html-in-a-jquery-script
                    // criar um parágrafo
                    var paragrafo = $("<p>");
                    // informar o HTML deste parágrafo
                    // observe o apóstrofo inclinado, para interpretar as variáveis
                    paragrafo.html(`==> ${p.marca}, ${p.modelo}, celular de ${p.proprietario.nome}`);
                    // adicionar o parágrafo criado na div
                    $('#listagem_celulares').append(paragrafo);
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
        mensagem = encontrarErro(jqXHR, textStatus, rota);
        alert("Erro na chamada ajax: " + mensagem);
    });

    /*

    FUNÇÃO UTILITÁRIA

    */

    function encontrarErro(jqXHR, textStatus, rota) {
        var msg = '';
        if (jqXHR.status === 0) {
            msg = 'Não foi possível conectar, ' +
                'verifique se o endereço do backend está certo' +
                ' e se o backend está rodando.';
        } else if (jqXHR.status == 404) {
            msg = 'A URL informada não foi encontrada no ' +
                'servidor [erro 404]: ' + rota;
        } else if (jqXHR.status == 500) {
            msg = 'Erro interno do servidor [erro 500], ' +
                'verifique nos logs do servidor';
        } else if (textStatus === 'parsererror') {
            msg = 'Falha ao decodificar o resultado json';
        } else if (textStatus === 'timeout') {
            msg = 'Tempo excessivo de conexão, estourou o limite (timeout)';
        } else if (textStatus === 'abort') {
            msg = 'Requisição abortada (abort)';
        } else {
            msg = 'Erro desconhecido: ' + jqXHR.responseText;
        }
        return msg;
    }
});