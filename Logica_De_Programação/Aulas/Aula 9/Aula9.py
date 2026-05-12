
# Meu Primeiro Robo


print("Seja Bem-Vindo Ao Trabalho")

metros = input("Digite a quantidade de metros:  ")
print(f"Você vai usar {metros} metros para andar.")

peca = input("Selecione a peça que deseja usar:  ")

# ----------------------------------------------------------------------------------

if peca == "defeito":
    print("Você chegou até a peça defeituosa você deve trazer para o programador.")

elif peca == "normal":
    print("Você chegou até a peça Normal você deve levar até o Bruno.")

else:
    print("Algo deu errado, Tente novamente.")