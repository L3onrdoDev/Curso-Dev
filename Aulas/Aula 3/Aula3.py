# 1. Laço 'For' (Repetições Determinadas)
# Use o 'For' quando você sabe exatamente quantas vezes algo deve acontecer (Como ler 10 sensores ou precessar uma lista de peças.)
# Exemplo: Relatório de Produção Diária.
# Imagine que você tem uma meta de produzir 5 lotes e quer numerar cada um:

# Exemplo 1:

# for lote in range(1, 6):
#     print(f"Processando lote número {lote}...")
#     print("Qualidade verificada. [OK]")
#     print("Produção do dia finalizada!")

# # Exemplo 2:

# for b in range(10):
    # print(f"Quantidade total {b} foi...")

# Exemplo 3: 

# for vinil in range(1, 21):
#     print(f"Quantidade de discos produzidos: {vinil}")
#     print("Produção Finalizada.")

# Exemplo 4:

# prod = ["Engrenagem", "Eixo", "Rolamento", "Parafuso", "Martelo"]
# itemprod = ["Cilindricas", "Eixo Conico", "Radiais", "Madeira", "Bola", "Cabeça Chata", "Chave metalica verde"]

# for item in prod:
#     print(f"Item em estoque: {item}")
#     for item2 in itemprod:
#         print(f"Item de peças em esoque: {itemprod}")

# Exemplo 5:

# print("Loja Do Gordin")
# print("Opção 1: Peças")
# print("Opção 2: Item Peças")
# menu = int(input("Escolha uma opção: "))

# prod = "Engrenagem", "Eixo", "Rolamento", "Parafuso", "Martelo"
# itemprod = "Cilindricas", "Eixo Conico", "Radiais", "Madeira", "Bola", "Cabeça Chata", "Chave metalica verde"

# if menu == 1:
#     for item1 in prod:
#         print(f"Sua lista de peças {prod}")
# elif menu == 2:
#     print(f"Sua lista de peças {itemprod}")
# else:
#     print("Algum erro encontrado! Tente Novamente.")

# Exercicio 1: Contador de produção

# print("Recursos Humanos - Gordin Store")
# print("||-------------||-------------||")

# for b in range(1, 11):
#     print(f"Peça N° {b} processada com sucesso.")
# print("Ciclo de produção concluído.")

# Exercicio 2: 

# Produção de Frutas na Feira

# print("--- RELATÓRIO DE PRODUÇÃO---")
# for banana in range(1, 11):
#     print(f"Banana nº: {banana}")

# print("-----------------------------")

# for manga in range(1, 6):
#     print(f"Manga nº: {manga}")

# print("-----------------------------")

# for melancia in range(1, 11):
#     print(f"Melancia nº: {melancia}")

# print("-----------------------------")

# for abacaxi in range(1, 14):
#     print(f"Abacaxi nº: {abacaxi}")

# print("-----------------------------")

# total_banana = 10
# total_manga = 5
# total_melancia = 10
# total_abacaxi = 13

# total_geral = total_banana + total_manga + total_melancia + total_abacaxi

# print("A produção final foi: ", total_geral)

# Exercicio: 3

# numero = int(input("Quero a tabuada do: "))

# print(f"--- Tabuada do {numero} ---")

# for numero2 in range(1, 11):
#     resultado = numero * numero2
#     print(f"{numero} x {numero2} = {resultado}")

# print("------------------------")
