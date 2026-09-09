const Input = require('readline-sync');

const Quantidade_Pecas = Input.questionInt("Digite a quantidade de pecas por ciclo: ");

for (let i = 0; i <= 10; i++) {
    let Calculo = Quantidade_Pecas + i; 
    
    console.log(`Ciclo: ${i + 1} = ${Calculo}`);
}
