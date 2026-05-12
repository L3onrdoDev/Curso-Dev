# 2.0 O laço while (Repetições Indeterminadas)
# Use o while quando você não sabe quando vai parar. Ele depende de uma condição (Como um sensor de segungança ou um botão emergência.)
# Exemplo: Monitor de Temperatura (Loop infinito controlado)
# Repete enquanto a temperatura estiver seguna.


# import time
# temperatura = 30
# while temperatura < 80:
#     print(f"Temperatura Atual:  {temperatura}°C. Sistema operando.")
#     time.sleep(1)
#     temperatura +=3
# print("ALERTA! Temperatura atingiu o limite. Desligando o motor...")

# Exemplo 2: Monitoramento de Temperatura com Listas de leotiras.
# Listas de temperatura lidas pelos sensor por minuto

# leituras = [70, 75, 82, 98, 110, 85, 80]

# for temp in leituras:
#     if temp > 100:
#         print(f"CRÍTICO: {temp}°C detectado! Acionado parada de emergência.")
#         break
#     print(f"Temperatura está em {temp}°C. Operação normal.")

# print("Sistema Desligado. Aguardando manutenção.")

# Exemplo 3: 

# materias = ["Metal", "metal", "Plastico", "metal", "Vidro", "Metal"]
# for pecas in materias:
#     if pecas != "metal":
#         print(f"Aviso: Peças de {pecas} detectada. Desviando para o descarte..")
#         continue # Pula o restante do código abaixo e vai para a próxima peça
#     # Este código só roda se a peça for metal
#     print(f"Processando peça de {pecas}. Furando e polindo...")

# print("Fim do lote de produção")

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# Exercicio 1: 
# Tente criar um codigo que conte de 1 a 10, mas use o continue para não imprimir o número 5 (Simulando uma falha de sensor específica no item 5).

# for item in range(1, 11):
#     if item == 5:
#         print("O item 5 falhou! Pulando leitura...")
#         continue
#     print(f"Item {item} lido com sucesso.")

# Execicio 2: 
# Simule um semáforo com parada para cada cor. Determine um tempo que deseja para que quando mudar para tal cor ele
# represente uma pausa paa cada cor. Use o continue para pular a cor amarela (Simulando um semáforo com defeito que não acende a luz amarela)

# import time
# semaforo = ["Verde", "Amarelo", "Vermelho"]

# for cor in semaforo:
#     if cor == "Amarelo":
#         print("Luz amarela queimada.")
#         continue
#     time.sleep(1)

#     print(f"Sinal {cor} ligado")

# Exercicio 3:
# Uma fabrica tem 5 maquinas. Peça ao usuario (via input dentro do loop)
# O consumo em kWh em cada uma das 5 maquinas. Ao final do loop, o programa
# deve exibir o consumo total da fabrica.

# consumo_total = 0
# for i in range(1, 6):
#     consumo_maquina = float(input(f"Digite o consumo da maquina {i} em kWh: "))
#     consumo_total += consumo_maquina
# print(f"O consumo total da fábrica foi de: {consumo_total} kWh")

# Exercicio 4:
# Percorra uma lista de peças:
# medidas = [50.1, 49.8, 52.0, 50.0, 48.5]
# O padrão de qualidade aceita apenas peças com exatamente 50.0 ou mais.
# Use um for para ler a lista e, para cada peça, diga se ela está "Aprovada" ou "Rejeitada"

# medidas = [50.1, 49.8, 52.0, 50.0, 48.5]

# for peca in medidas:
#     if peca >= 50.0:
#         status = "Aprovada"
#     else:
#         status = "Rejeitada"
    
#     print(f"Medida: {peca} - Status: {status}")

# Exercicio 5:
# Uma balança industrial esta pesando lote de 6 sacos de insumos.
# O peso ideal de cada saco é 50kg, mas o sistemas aceita variações.
# Crie um programa que peça ao usuário o peso de cada saco (Via input dentro do loop)
# E, para cada um, informe se ele está "Dentro do limite" (Entre 48% e 52%) ou "Fora do limite".
# No final, exiba quantos sacos estão dentro do limite.

# sacos_limite = 0

# for i in range(1, 7):
#     peso = float(input(f"Digite o peso do saco {i} (em kg): "))

#     if peso <= 52:
#         print(f"Saco {i}: Dentro do limite. ")
#         sacos_limite += 1 
#     else:
#         print(f"Saco {i}: Fora do limite!")

# print(f"Resultado Final: {sacos_limite} sacos aprovados.")
# print(f"Sacos reprovados: {6 - sacos_limite}")

# Desafio 1:     

# ciclo = 0
# while ciclo < 5:
#         temperatura = float(input(f"Digite a temperatura da peça {ciclo + 1} em °C:  "))

#         if temperatura < 0:
#             print("Erro de leitura no sensor. Por favor, Digite uma temperatura válida")
#             continue
#         if temperatura > 150:
#             print("Alerta Crítico: RISCO DE EXPLOSÃO!")
#         break

# print(f"Peça {ciclo + 1} processada com temperatura {temperatura}°C.")
# ciclo += 1

# print(f"Peça {ciclo} processada com sucesso. Temperatura dentro do limite.")
# print("Fim do moitoramento de temperatura.")

# Desafio 2:
# Contador de peças com falha (while + if + continue)
# Uma linha de produção tem um sensor que detecta falhas em peças.
# O usuario deve digitar "sim" para indicar que uma peça tem falha e "não" para inidicar que está boa.
# O programa deve continuar pedindo a condição da peça até que o usuário digite "fim".
# No final, exiba o total de peças com falhas detectadas.