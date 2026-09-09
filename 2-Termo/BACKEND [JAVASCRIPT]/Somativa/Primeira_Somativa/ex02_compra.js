const Input = require('readline-sync');

const Nome_Material = Input.question("Insira o nome do material:  ");
const Quantidade = Input.questionInt("Insira a quantidade:  ");
const Preco = Input.questionFloat("Insira o valor total da compra:  ");

const Calculo = Quantidade * Preco;

console.log(`${Quantidade} ${Nome_Material} a R$ ${Preco.toFixed(2)}. Eo valor total foi ${Calculo.toFixed(2)}`);
