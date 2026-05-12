# Clean Code - Aula 6
# Para que usar?
# Como usar?
# print("Clean Code - Aula 6")
# aula = 6
# print(f"Estamos na aula {aula} de Clean Code.")

# --------------------------------------------------------

# texto = "   Python é Muito Legal!   "
# print(texto.strip().upper())
# print(texto.strip().lower())
# print(texto.strip().capitalize())
# print(texto.strip().title())
# print(texto.strip().replace("", "_"))
# print(texto.strip().split())

# --------------------------------------------------------

# Escrita
# with open("notas.txt", "w") as arquivo:
#     arquivo.write("Estudar Python Hoje!\n")
#     arquivo.write("Ler sobre Clean Code.")

# # Leitura
# with open("notas.txt", "r") as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)

# --------------------------------------------------------

# Exercicio 1:

# Crie um programa que peça ao usuario para inserir uma frase e, em seguida, exiba a frase com as seguintes transformações:
# - Remova os espaços extras no inicio e no final da frase.

# frase = input("Digite a frase:  ")
# print(frase.strip().capitalize())

# --------------------------------------------------------

# Exercicio 2:

# Crie um programa que ele leia o conteudo de um arquivo de texto e conte quantas vezs a palavra 'Python' aparece no arquivo. Exiba o resultado para o usuario.

# print("Contagem de palavras em arquivo")
# with open("notas.txt", "r") as arquivos:
#     conteudo = arquivos.read()
#     contagem = conteudo.count("Python")
#     print(f"A contagem de palavras é de {contagem}...")

# --------------------------------------------------------

# Execução de comandos do sistema

# import os # Importa o módulo os para interagir com o sisema operacional

# Onde estou?

# print(os.getcwd())

# # Listar arquivos na pasta

# print(os.listdir(".."))
# print(os.listdir("..\\.."))
# print(os.listdir("C:\\"))
# print(os.listdir("C:\\Users"))
# print(os.listdir("C:\\Users\\Public"))

# --------------------------------------------------------

# Outros comandos úteis:

# Criar pastas

# os.mkdir("Nova_Pasta")

# # Renomear Pasta

# os.rename("Nova_Pasta", "pasta_renomeada")

# # Excluir Pasta


# os.rmdir("pasta_renomeada")

# --------------------------------------------------------

# Exercicio 2:

# Crie um script que mostre o caminho da pasta atual.

# import os
# os.getcwd()


# Exercicio 3: 

# Liste os arquivos da pasta atual.

# import os
# print(os.listdir())

# Exercicio 4: 

# Crie uma pasta chamada "projetos" e depois renomeie para "meus_projetos". Por Fim, Exclua a pasta.

# os.mkdir("projetos")
# os.rename("projeto", "meus_projetos")
# os.rmdir("meus_projetos")

# Exercicio 5:

# Crie um arquivo chamada "log.txt" e escreva a mensagem "log de atividades".
# Depois, leia o conteudo do arquivo e exiba na tela.

# with open("log.txt", "w") as arquivo:
#     arquivo.write("log de atividade")

# with open("log.txt", "r") as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)

# --------------------------------------------------------

# Exemplo de dicionario:
# Cria um dicionario com informações sobre uma pessoa e acessa um valor usado uma chave.

# pessoa = {
#     "nome": "Alice", 
#     "idade": "30",
#     "cidade": "São Paulo",
#     "profissao": "Engenheira",
# }

# pessoa2 = {
#     "nome": "Bruno", 
#     "idade": "25",
#     "cidade": "São Paulo",
#     "profissao": "Designer",
# }

# print(pessoa["cidade"])
# print(pessoa2["nome"], pessoa["idade"])

# --------------------------------------------------------

# Exemplo 2: Desligar o pc
# with open("deliga.bat", "w") as desligar:
# desligar.write("shutdow -s -t -c \ "Desligamento programa para daqui a 1 hora. Salve Seu Trabalho.")