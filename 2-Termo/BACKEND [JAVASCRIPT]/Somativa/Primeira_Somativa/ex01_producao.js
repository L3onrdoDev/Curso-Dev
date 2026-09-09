const Input = require('readline-sync');

const Pecas_Produzidas = Input.questionInt("Digite a quantidade de pecas produzidas por hora:  ");
const Turno = Input.questionFloat("Digite a quantidade de horas do turno:   ");

const Calculo = Pecas_Produzidas * Turno;

console.log(`Foram produzidas ${Pecas_Produzidas} Peças/H, e ${Turno} Horas. O total produzido foi ${Calculo} Pecas.`);
