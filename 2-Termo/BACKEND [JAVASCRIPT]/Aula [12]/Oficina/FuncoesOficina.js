function CalcularOrcamento(PrecoPecas, HorasTrabalho) {
    const ValorHora = 85.00;
    const TotalMaoDeObra = HorasTrabalho * ValorHora;
    // const CalculoDesconto = TotalMaoDeObra * 0.2; | Outra forma de fazer.
    //const CalculoFinal = TotalMaoDeObra - CalculoDesconto; | Outra forma de fazer.
    return PrecoPecas + TotalMaoDeObra;
}

function VerificarGarantia(Meses) {
    if (Meses <= 3) {
        return "Dentro Da Garantia"
    } else {
        return "Garantia Expirada"
    }
}

function ValorComDesconto(ValorTotal) {
    return ValorTotal * 0.8;
}

module.exports = {
    CalcularOrcamento,
    VerificarGarantia,
    ValorComDesconto
} 