var acao = $.ajax({
    url: "http://127.0.0.1:5000/listar_pessoas",
    method: "get",
    dataType: "json"
});

acao.done(function(resultado) {
    for(var pessoa of resultado) {
        let tr = document.createElement("tr");
        
        let nome = document.createElement("th");
        let email = document.createElement("th");
        let telefone = document.createElement("th");
        let nascimento = document.createElement("th");

        $(nome).text(pessoa.nome)
        $(email).text(pessoa.email)
        $(telefone).text(pessoa.telefone)
        $(nascimento).text(pessoa.nascimento)


        $(tr).append(nome);
        $(tr).append(email);
        $(tr).append(telefone);
        $(tr).append(nascimento);

        $("#listagem").append(tr);
    }
});