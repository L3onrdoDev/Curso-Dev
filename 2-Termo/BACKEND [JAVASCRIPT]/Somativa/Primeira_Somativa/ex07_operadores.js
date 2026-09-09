const Input = require('readline-sync');

const Banco_Dados = []

for (let i = 0; i < 5; i++) {
    console.log(`~~~ Cadastro De Nomes ${i+1} ~~~`);
    let NovoNome = Input.question("Digite Seu Nome: ");

    const novoAluno = {
        nome: NovoNome
    };
    
    Banco_Dados.push(novoAluno);
}

console.log("~~~~~~~~~~~~ // ~~~~~~~~~~~");
for (let i = 0; i < Banco_Dados.length; i++) {
    console.log(`${i + 1} - ${Banco_Dados[i].nome}`);
}