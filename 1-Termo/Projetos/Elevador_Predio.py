# Sistema de Elevador de Prédio
# O prédio possui 10 andares, sendo o térreo o andar 0. O elevador pode se mover para cima ou para baixo, e tem a capacidade de transportar até 5 pessoas.
# O elevador começa no andar 0 e pode ser chamado por qualquer pessoa em qualquer andar.
# O elevador deve se mover para o andar onde a pessoa chamou, e depois para o andar destino da pessoa.
# O elevador deve exibir mensagens indicando o andar atual, o número de pessoas no elevador, e as ações realizadas (subindo, descendo, parando). O programa deve continuar rodando até que o usuário decida encerrar.

andar_atual = 0

while True:

    print("-----------------------------------------------------------")
    print("--------------------- Quality Limeira ---------------------")
    print("-----------------------------------------------------------")

    print(f"Seu andar atual é: {andar_atual}")

    opcao = input("Deseja chamar o elevador? (Sim/Não): ")

    if opcao == "Não":
        print("Opção 'Não' Selecionada. Sistema Cancelado.")
        break

    try:
        andar_chamada = int(input("Digite o andar chamado: "))
        destino = int(input("Digite o andar de destino: "))
        pessoas = int(input("Quantas pessoas vai entrar? "))

        if pessoas > 5:
            print("Capacidade máxima: 5 pessoas.")
            continue

        if andar_chamada > andar_atual:
            print("Elevador subindo...")
        elif andar_chamada < andar_atual:
            print("Elevador descendo...")

        andar_atual = andar_chamada

        print(f"Parou no andar {andar_atual}")
        print(f"{pessoas} pessoas entraram.")

        if destino > andar_atual:
            print("Subindo...")
        elif destino < andar_atual:
            print("Descendo...")

        andar_atual = destino

        print(f"Parou no andar {andar_atual}")
        print("Viagem finalizada!")

    except ValueError:
        print("Digite apenas números.")
        continue