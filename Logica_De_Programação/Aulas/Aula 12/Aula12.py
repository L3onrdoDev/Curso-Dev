# Interface Gráfica com TKINTER
# Componentes Principais (Widgets)

# tk: Janela principal
# Label: Texto ou rotulo
# Button: Um botão clicável 
# Entry: Um campo de entrada de texto

# def: Definição de uma variavel
# bold: Negrito

import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Minha Primeira Janela GUI")
janela.geometry("800x600")

def mostrar_mensagem():
    messagebox.showinfo("Sucesso!", "Você clicou no botão :)")

lbl_titulo_pagina = tk.Label(janela, text="Bem-Vindo a aula de Interface Gráfica!", font=("Arial", 14, "bold"))
lbl_subtitulo_pagina = tk.Label(janela, text="Aula 12 - Desenvolvimento de paginas GUI.", font=("Arial", 10, "bold"))
btn_clique_pagina = tk.Button(janela, text="Clique Aqui", font=("Arial", 14), bg="#4a53d1", fg="white", command=mostrar_mensagem)
btn_fechar_janela = tk.Button(janela, text="Fechar", font=("Arial", 14), bg="#e74c3c", fg="white", command=janela.destroy)

lbl_titulo_pagina.pack(pady=50)
lbl_subtitulo_pagina.pack(pady=40)
btn_clique_pagina.pack(pady=50)
btn_fechar_janela.pack(pady=10)

janela.mainloop()
