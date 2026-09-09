const Input = require('readline-sync');

const Peso_Peca = Input.questionFloat("Digite o peso da peca:  ");

if (Peso_Peca >= 95 && Peso_Peca < 105) {
    console.log("PEÇA APROVADA")
} else {
    console.log("PEÇA REPROVADA")
}

console.log(`O peso informado foi ${Peso_Peca}`);