# 1. Registro
modelo = input("Digite o modelo do veículo: ")
placa = input("Digite a placa do veículo: ")
print(f"Veículo {modelo} de placa {placa} registrado no sistema. Boa viagem!")
print("-----------------------------------------------------------------------")

# 2. Cálculo de Autonomia
capacidade = float(input("Capacidade do tanque (litros): "))
consumo = float(input("Consumo médio (km/l): "))
autonomia = capacidade * consumo

print(f"A distância total que o veículo pode percorrer é de {autonomia} km.")