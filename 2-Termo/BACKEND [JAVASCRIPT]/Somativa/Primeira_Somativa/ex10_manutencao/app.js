const Input = require('readline-sync');
const Oficina = require('./funcoesManutencao');

console.log("~~~ Sistema De Gestão - Oficina Barbosa ~~~");

const Peca = Input.questionFloat("Preco da peca:  R$");
const Horas = Input.questionInt("Horas de servico:  ");
const TempoUso = Input.questionInt("Meses desde o ultimo conserto:  ");

const Total = Oficina.CalcularOrcamento(Peca, Horas);

const Garantia = Oficina.VerificarGarantia(TempoUso);

console.log("\n~~~ Relatorio De Servico ~~~");
console.log(`Orcamento: R$ ${Total.toFixed(2)}`);
console.log(`Status Garantia: ${Garantia}`);
console.log("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")