function CalcularOrcamento(PrecoPecas, HorasTrabalho) {
    const ValorHora = 80.00;
    const TotalMaoDeObra = HorasTrabalho * ValorHora;
    // const CalculoDesconto = TotalMaoDeObra * 0.2; | Outra forma de fazer.
    //const CalculoFinal = TotalMaoDeObra - CalculoDesconto; | Outra forma de fazer.
    return PrecoPecas + TotalMaoDeObra;
}

function VerificarGarantia(Meses) {
    if (Meses <= 6) {
        return "EM GARANTIA"
    } else {
        return "FORA DA GARANTIA"
    }
}

module.exports = {
    CalcularOrcamento,
    VerificarGarantia
} 