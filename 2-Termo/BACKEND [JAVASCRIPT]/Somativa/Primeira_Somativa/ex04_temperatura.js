const Input = require('readline-sync');

const Temperatura = Input.questionFloat("Digite a temperatura em C:  ");

if (Temperatura <= 60) {
    console.log(`${Temperatura}°C: NORMAL`)
} else if (Temperatura >= 61 && Temperatura <= 80) {
    console.log(`${Temperatura}°C: ATENCAO`)
} else {
    console.log(`${Temperatura}°C: CRITICA`)
}