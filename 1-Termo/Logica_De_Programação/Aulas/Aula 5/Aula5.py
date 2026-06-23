# # 1. Perfil de Gamer: Peça o nick (nome) do jogador e o nível atual. Exiba: "O
# # jogador [nick] está no nível [nível] e pronto para a partida!"

# print("Seja Bem-Vindo(a) A Revision Company.")
# print("Utilize nossa ferramenta abaixo.")

# nome = input("Digite seu nick:  ")
# nivel = int(input("Digite seu nível:  "))

# print(f"O jogador {nome} está no nível {nivel} e pronto para a partida!")

# # --------------------------------------------------------------------------------------

# # 2. Calculadora de Mesada: Peça o valor que o aluno ganha por semana e
# # multiplique por 4 para mostrar quanto ele terá no final do mês.

# print("Calculadora De Mesada")
# print("Utilize nosso sistema para gerenciar e calcular sua mesada.")

# valor_recebido = float(input("Digite o valor da mesada:  "))

# valor_final = valor_recebido * 4

# print(f"No final do mês você terá {valor_final} reais.")

# # --------------------------------------------------------------------------------------

# # 3. Conversor de Internet: Peça um valor em Gigabytes (GB) e converta para
# # Megabytes (MB) (multiplique por 1024).

# print("Conversor De Internet")
# print("Bem vindo(a) ao nosso sistema de conversor de GB para MB, Utilize nosso sistema abaixo.")

# GB = int(input("Digite a quantidade de GB:  "))

# valor_final = GB * 1024

# print("|| Conversor De Internet ||")
# print(f"O resultado da sua conversão foi {valor_final} MB")

# --------------------------------------------------------------------------------------

# 4. Média de Notas: Peça as notas de Matemática e Português. Calcule e mostre a
# média final.

nota_matematica = float(input("Digite sua nota de Matemática:  "))
nota_portugues = float(input("Digite sua nota de Português:  "))

calculo = nota_matematica + nota_portugues
calculo_final = calculo / 2

print(f"Sua média final é {calculo_final}")

# --------------------------------------------------------------------------------------

# 5. Seguidores: Peça a quantidade de seguidores atuais e quantos novos seguidores
# o aluno ganhou hoje. Exiba o total atualizado.

# seguidores_atual = int(input("Digite a quantidade de seguidores atual:  "))
# seguidores_novos = int(input("Digite a quantidade de seguidores novos:  "))

# calculo = seguidores_atual + seguidores_novos

# print(f"Você ganhou {seguidores_novos} seguidores novos hoje.")
# print(f"O total de seguidores agora é {calculo}")

# --------------------------------------------------------------------------------------

# 6. Idade em Dias: Peça a idade do aluno e calcule aproximadamente quantos dias
# ele já viveu (idade * 365).

# idade = int(input("Digite sua idade:  "))

# calculo = idade * 365

# print(f"Você já viveu {calculo} dias.")

# --------------------------------------------------------------------------------------

# 7. Consumo de Lanche: Peça o preço do salgado e o preço do suco. Exiba o valor
# total da conta.

# salgado = float(input("Digite o preço do salgado:  "))
# suco = float(input("Digite o preço do suco:  "))

# calculo = salgado + suco

# print(f"O valor total da sua conta foi de {calculo} reais.")

# --------------------------------------------------------------------------------------

# # 8. Ano de Nascimento: Peça o ano atual e a idade do aluno. Calcule e exiba o ano
# # em que ele nasceu.

# ano_atual = int(input("Digite o ano atual:  "))
# idade = int(input("Digite sua idade:  "))

# calculo = ano_atual - idade

# print(f"O ano que você nasceu é {calculo}")

# --------------------------------------------------------------------------------------

# 9. Filtro de Idade (TikTok): Peça a idade do usuário. Se for menor que 13, exiba
# "Acesso restrito". Se tiver entre 13 e 17, "Acesso moderado". Se for 18 ou
# mais, "Acesso liberado".

# idade = int(input("Digite sua idade: "))

# if idade < 13:
#     print("Acesso restrito")
# elif idade <= 17:
#     print("Acesso moderado")
# else:
#     print("Acesso liberado")

# # --------------------------------------------------------------------------------------

# # 10.Bateria do Celular: Crie um while que começa com a bateria em 100. A cada
# # repetição, subtraia 10 e mostre: "Bateria em [valor]%". O loop para quando
# # chegar em 10 e exibe: "Por favor, conecte o carregador!".

# bateria = 100

# while bateria > 10:
#     bateria -= 10

#     print(f"Bateria em {bateria}%")

# print("Por favor, conecte o carregador!")

# # --------------------------------------------------------------------------------------

# # 11. Contagem de Curtidas: Use um for para simular a contagem de curtidas em uma
# # foto. Peça ao usuário o limite de curtidas (ex: 5). O programa deve contar de 1 até
# # esse número, printando: "Curtida no [i] recebida!".

# limite = int(input("Digite o limite de curtidas: "))

# for i in range(1, limite + 1):

#     print(f"Curtida n° {i} recebida!")

# # --------------------------------------------------------------------------------------

# # 12.Carrinho de Compras Online: Use um while para pedir nomes de produtos que o
# # aluno quer comprar. O loop só para quando ele digitar "sair". No final, mostre
# # quantas vezes ele adiciona itens ao carrinho (use um contador).

# contador = 0

# while True:

#     produto = input("Digite o nome do produto (ou 'sair' para finalizar): ")

#     if produto.lower() == "sair":

#         break

#     if produto == "":

#         continue

#     contador += 1

#     print(f"'{produto}' adicionado ao carrinho!")

# print(f"Você adicionou {contador} item(ns) ao carrinho.")

# # --------------------------------------------------------------------------------------

# contador = 0
# produto = 0
# while produto != "sair":
#     contador =+ 1
#     produto = input("Digite o nome do produto (ou 'sair' para finalizar): ")
# print(f"Você adicionou {contador-1}")