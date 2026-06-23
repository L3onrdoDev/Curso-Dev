import tkinter as tk
from tkinter import messagebox

# .get() serve para buscar informação na caixa de texto
def janela_bemvindo():
    nome = nome_usuario.get()

    if nome == "":
        messagebox.showwarning("Aviso", "Digite seu nome :)")
    else:
        messagebox.showinfo("Bem-Vindo", f"Olá usuário, {nome} - Seja bem-vindo ao nosso sistema")

    idade = idade_usuario.get()

    if idade == "":
        messagebox.showwarning("Aviso", "Digite sua idade :)")
    else:
        messagebox.showinfo("Bem-Vindo", f"Olá usuário, Sua idade é {idade} Anos - Seja bem-vindo ao nosso sistema")
    
    
 
# Configurações da Janela
janela = tk.Tk()
janela.title("Exemplo 2")
janela.geometry("300x300")
janela.configure(bg="black")

# Componentes
lbl_mensagem = tk.Label(janela, text="Digite seu nome :)")
lbl_mensagem.grid(row=0, column=0, pady=10, padx=10)

nome_usuario = tk.Entry(janela, font=("Arial", 12))
nome_usuario.grid(row=0, column=1, pady=10, padx=10)

lbl_mensagem2 = tk.Label(janela, text="Digite sua idade :)")
lbl_mensagem2.grid(row=1, column=0, pady=10, padx=10)

idade_usuario = tk.Entry(janela, font=("Arial", 12))
idade_usuario.grid(row=1, column=1, pady=10, padx=10)

btn_mensagem = tk.Button(janela, text="Confirmar", command=janela_bemvindo)
btn_mensagem.grid(row=3, column=0, pady=10, padx=10)

btn_fechar_janela = tk.Button(janela, text="Fechar", font=("Arial", 14), bg="#e74c3c", fg="white", command=janela.destroy)
btn_fechar_janela.grid(row=3, column=1, pady=10, padx=10)

# Rodar interface
janela.mainloop()



