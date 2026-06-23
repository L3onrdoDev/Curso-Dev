import tkinter as tk
from tkinter import messagebox, ttk

# ---------- // Codigo \\ ----------

def validar_emprestimo():

    nome = nome_usuario.get()
    tipo = tipo_usuario.get()
    categoria = categoria_livro.get()

    if nome == "" or tipo == "" or categoria == "":
        messagebox.showwarning("Aviso", "Preencha todos os campos!")
        return

    try:
        dias = int(dias_emprestimo.get())
    except ValueError:
        messagebox.showerror("Erro", "Digite apenas números para os dias.")
        return

    if categoria == "Raros" and tipo == "Comunidade":
        messagebox.showerror("Empréstimo Negado", "Livros raros só podem ser emprestados para alunos.")
        return

    if tipo == "Aluno":
        limite = 14

    elif tipo == "Comunidade":
        limite = 7

    else:
        messagebox.showerror("Erro","Digite Aluno ou Comunidade.")
        return

    if dias > limite:

        dias_extras = dias - limite
        taxa = dias_extras * 5

        messagebox.showinfo("Empréstimo Aprovado", f"Usuário: {nome} Tipo: {tipo} Categoria: {categoria} Dias solicitados: {dias} Taxa de renovação: R$ {taxa}")

    else:
        messagebox.showinfo("Empréstimo Aprovado", f"Usuário: {nome} Tipo: {tipo} Categoria: {categoria} Dias solicitados: {dias} Sem cobrança de taxa.")

# ---------- // Visual \\ ----------

janela = tk.Tk()
janela.title("Biblioteca Digital")
janela.geometry("450x300")

lbl_nome = tk.Label(janela, text="Nome")
lbl_nome.grid(row=0, column=0, padx=10, pady=10)

nome_usuario = tk.Entry(janela)
nome_usuario.grid(row=0, column=1)

lbl_tipo = tk.Label(janela, text="Tipo (Aluno/Comunidade)")
lbl_tipo.grid(row=1, column=0, padx=10, pady=10)

tipo_usuario = tk.ttk.Combobox(janela, values=["Aluno", "Comunidade"], width=16)
tipo_usuario.grid(row=1, column=1)

lbl_categoria = tk.Label(janela, text="Categoria (Comum/Raros)")
lbl_categoria.grid(row=2, column=0, padx=10, pady=10)

categoria_livro = tk.ttk.Combobox(janela, values=["Comum", "Raros"], width=16)
categoria_livro.grid(row=2, column=1)

lbl_dias = tk.Label(janela, text="Dias de empréstimo")
lbl_dias.grid(row=3, column=0, padx=10, pady=10)

dias_emprestimo = tk.Entry(janela)
dias_emprestimo.grid(row=3, column=1)

btn_validar = tk.Button(janela, text="Confirmar", command = validar_emprestimo)
btn_validar.grid(row=4, column=0, pady=20)

janela.mainloop()