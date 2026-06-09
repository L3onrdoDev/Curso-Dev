import tkinter as tk
from tkinter import messagebox, ttk


# Foco: print, input, operações matemáticas e f-strings
# 1. Registro de Operador: Peça o nome do operador e o turno (A, B ou C). Exiba:
# "Operador [Nome] registrado no Turno [Turno]. Boa jornada!".

# def validar_login():

#     nome = nome_usuario.get()
#     turno = turno_usuario.get()

#     if nome == "" or turno == "":
#         messagebox.showwarning("Aviso", "Preencha todos os campos!")
#         return
#     else:
#         messagebox.showinfo("Sucesso", f"Operador {nome} registrado no Turno {turno}. Boa jornada!")

# janela = tk.Tk()
# janela.title("Painel Login - Operador")
# janela.geometry("800x600")
# janela.configure(bg="black")

# # Componentes
# lbl_mensagem = tk.Label(janela, text="Digite seu nome")
# lbl_mensagem.grid(row=0, column=0, pady=10, padx=10)

# nome_usuario = tk.Entry(janela, font=("Arial", 12))
# nome_usuario.grid(row=0, column=1, pady=10, padx=10)

# lbl_mensagem = tk.Label(janela, text="Selecione seu turno")
# lbl_mensagem.grid(row=1, column=0, pady=10, padx=10)

# turno_usuario = tk.ttk.Combobox(janela, values=["A", "B", "C"], width=16)
# turno_usuario.grid(row=1, column=1, pady=10, padx=10)

# btn_confirmar = tk.Button(janela, text="Confirmar", font=("Arial", 14), bg="#50e73c", fg="black", command=validar_login)
# btn_confirmar.grid(row=3, column=0, pady=10, padx=10)

# btn_fechar_janela = tk.Button(janela, text="Fechar", font=("Arial", 14), bg="#e74c3c", fg="white", command=janela.destroy)
# btn_fechar_janela.grid(row=3, column=1, pady=10, padx=10)

# # Rodar interface
# janela.mainloop()

# 2. Cálculo de Produção: Peça a quantidade de peças produzidas em 1 hora. Calcule e
# exiba quantas peças serão produzidas em um turno de 8 horas.
# def calcular_producao():
#     try:
#         pecas_hora = int(entrada_pecas.get())

#         producao_total = pecas_hora * 8

#         resultado(text=f"Produção em 8 horas: {producao_total} peças")

#     except ValueError:
#         messagebox.showerror("Erro","Digite um número válido!")

# janela = tk.Tk()
# janela.title("Cálculo de Produção")
# janela.geometry("800x600")

# titulo = tk.Label(janela,text="Produção por Turno",font=("Arial", 14, "bold"))
# sub_titulo = tk.Label(janela,text="Digite a quantidade de peças produzidas em 1h",font=("Arial", 10, "bold"))
# titulo.pack(pady=10)
# sub_titulo.pack(pady=10)

# tk.Label(janela,text="Peças produzidas por hora:")

# entrada_pecas = tk.Entry(janela)
# entrada_pecas.pack(pady=5)

# botao = tk.Button(janela,text="Calcular",command=calcular_producao)
# botao.pack(pady=10)

# resultado = tk.Label(janela,text="",font=("Arial", 12))
# resultado.pack(pady=10)

# btn_fechar_janela = tk.Button(janela, text="Fechar", font=("Arial", 14), bg="#e74c3c", fg="white", command=janela.destroy)
# btn_fechar_janela.pack(pady=15)

# janela.mainloop()

# 3. Conversor de Unidade: O sistema lê uma pressão em Bar. Converta para PSI (1 Bar
# ≈ 14.5 PSI) e exiba com duas casas decimais.
def calcular_pressao():
    try:
        bar = int(pressao.get())

        psi = bar * 14.5
        resultado(text=f"Produção em 8 horas: {producao_total} peças")

    except ValueError:
        messagebox.showerror("Erro","Digite um número válido!")

janela = tk.Tk()
janela.title("Conversor de Unidade")
janela.geometry("800x600")

titulo = tk.Label(janela,text="Produção por Turno",font=("Arial", 14, "bold"))
sub_titulo = tk.Label(janela,text="Digite a quantidade de peças produzidas em 1h",font=("Arial", 10, "bold"))
titulo.pack(pady=10)
sub_titulo.pack(pady=10)

tk.Label(janela,text="Peças produzidas por hora:")

entrada_pecas = tk.Entry(janela)
entrada_pecas.pack(pady=5)

botao = tk.Button(janela,text="Calcular",command=calcular_pressao)
botao.pack(pady=10)

resultado = tk.Label(janela,text="",font=("Arial", 12))
resultado.pack(pady=10)

btn_fechar_janela = tk.Button(janela, text="Fechar", font=("Arial", 14), bg="#e74c3c", fg="white", command=janela.destroy)
btn_fechar_janela.pack(pady=15)

pressao = tk.Entry(janela)
pressao.pack(pady=5)

janela.mainloop()

# 4. Média de Qualidade: Peça 3 notas de inspeção de uma peça (0 a 10). Exiba a média
# aritmética simples delas.



# Foco: if, elif, else e operadores lógicos
# 5. Termostato Inteligente: Peça a temperatura de um motor.
# ● Abaixo de 40°C: "Baixa carga".
# ● Entre 40°C e 70°C: "Normal".
# ● Acima de 70°C: "ALERTA: Resfriamento Ativado!".



# 6. Classificador de Lotes: O usuário insere o código do produto. Se começar com "A",
# exiba "Alimentos". Se "E", "Eletrônicos". Para qualquer outro, "Desconhecido".



# 7. Segurança de Operação: A máquina só liga se o sensor_porta == "fechada" E o
# botao_emergencia == "desligado". Peça esses dois inputs e diga se a máquina pode
# iniciar.



# 8. Cálculo de Descarte: Peça o total de peças produzidas e o total de defeituosas. Se
# o descarte for maior que 5% do total, exiba "Revisar Processo", caso contrário,
# "Processo Otimizado".



# 9. Validação de Medida: Uma peça deve ter entre 9.8mm e 10.2mm. Peça a medida e
# diga se está dentro da tolerância, acima ou abaixo.



# Foco: for e while
# 10.Contagem Regressiva de Setup: Use um for para fazer uma contagem regressiva
# de 10 até 1 para o início de uma prensa, e finalize com "Prensa Ativada!".



# 11.Soma de Produção (Acumulador): Use um while para pedir o peso de várias caixas.
# O loop para quando o usuário digitar 0. No fim, mostre o peso total acumulado.



# 12.Múltiplas Leituras: Use um for para pedir a temperatura de 5 sensores diferentes.
# Ao final, mostre qual foi a maior temperatura lida.



# 13.Painel de Login: Crie um while que peça a senha do supervisor ("admin123").
# Enquanto ele errar, o programa diz "Acesso Negado". Ele tem apenas 3 tentativas.
# Se esgotar, exiba "Painel Bloqueado".



# Misturando tudo: Inputs, Ifs e Loops.
# 14.Simulador de Estoque: Comece com estoque = 100. Crie um menu (while) onde o
# usuário pode: (1) Adicionar itens, (2) Remover itens ou (3) Sair. Se o estoque ficar
# abaixo de 10, avise: "Estoque Crítico!".



# 15.Relatório de Turno Completo: Use um for para processar 5 peças. Para cada peça,
# peça o diâmetro. Se a peça for aprovada (entre 19.9 e 20.1), conte-a. No final do
# loop, exiba o total de peças aprovadas e a porcentagem de eficiência do lote.