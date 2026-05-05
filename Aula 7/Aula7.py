# Projeto 1:
# Projeto: Precisamos de um algoritmo para gerenciamento de cancelas para um shopping.
# Toda entrada e saída irá ser sinalizada
# Valores para entrada e permanência do veículo deverá ser pergutado
# As entrada deverão ser registradas por placa.
#
# Passo 1:  
# Perguntar informações sobre o veiculo ou forma acesso (Placa, cor, modelo)
# Pressionar o botao para emitir ticket (Emitir a pergunta de qual sistema ele quer usar)
# Verificar se possui TAG para acesso liberado (Emitir a pergunta de qual sistema ele quer usar)
# Se possuir erros informar ao usuário

# Passo 2:
# Verificar tempo de permanência
# Valor a ser cobrado

# Passo 3:
# Saída como será?
# Calcular tempo de permanência
# Se for TAG gerar na fatura da TAG
# Pagar ticket
# Devolver ticket na saída

# Passo 4:
# Gerar relatório de entradas e saídas
# Tratamento de Erros
# # Revisão do código

print("----- Seja Bem-Vindo(a) Ao Shopping Center -----")
print("    ----- Digite as informações abaixo -----")

informacoes_princ = input("Digite a placa do veiculo:  ")
informacoes_princ2 = input("Digite o modelo do veiculo:  ")
informacoes_princ3 = input("Digite a cor do veiculo:  ")

print("Novo Veiculo Cadastrado: ")
print(f"Placa: {informacoes_princ} | Modelo: {informacoes_princ2} | Cor: {informacoes_princ3}")

print("------------------------------------------------")

print("Escolha o metodo de entrada.")
print("Nossos sistemas. Ticket / Tag / Interfone.")

metodo_entrada = input("Digite o sistema de entrada:  ")
print(f"O sistema de entrada escolhido foi '{metodo_entrada}'.")

if metodo_entrada == "Ticket":
    print("Sistema selecionado com sucesso, Pague antes de sair.")
    hora_entrada = float(input("Digite a hora de entrada:  "))
    valor_estacionamento = 15
    hora_saida = float(input("Digite a hora da saída:  "))
    total_permanencia = hora_saida - hora_entrada
    total_estacionamento = total_permanencia * valor_estacionamento
    print(f"Seu tempo de permanência: {total_permanencia} em horas.")
    print(f"O valor a ser cobrado foi de R$:  {total_estacionamento:.2f}")
    print("Devolver Ticket")

elif metodo_entrada == "Tag":
    print("Sua permanência no Shopping será cobrada na sua fatura.")

elif metodo_entrada == "Interfone":
    print("Liberando acesso pelo Interfone")
    print("Sua saída deverá ser feita também pelo Interfone.")

else: 
    print("Obrigado pela visita, Volte Novamente.")