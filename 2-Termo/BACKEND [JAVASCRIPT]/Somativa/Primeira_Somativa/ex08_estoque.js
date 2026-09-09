const Input = require('readline-sync');

const Banco_Dados = []

for (let i = 0; i < 3; i++) {
    console.log(`~~~ Estoque SuperMercado - ${i+1} ~~~`);
    let Nome = Input.question("Digite o nome: ");
    let Quantidade = Input.question("Digite a quantidade: ");
    let EstoqueMin = Input.question("Digite a quantidade do estoque: ");

    const novoAluno = {
        nome: Nome,
        quantidade: Quantidade,
        estoque: EstoqueMin
    };
    
    Banco_Dados.push(Nome);
    Banco_Dados.push(Quantidade);
    Banco_Dados.push(EstoqueMin);

    if (Quantidade < EstoqueMin) {
        console.log("REPOR ESTOQUE")
    } else {
        console.log("ESTOQUE OK")
    }
}