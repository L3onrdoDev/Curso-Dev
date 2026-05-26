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

# 1. Criar a janela principal
janela = tk.Tk()
janela.title("Minha Primeira Janela GUI")
janela.geometry("800x600") #Largura x Altura

# 2. Criar a função que o botão irá executar
def mostrar_mensagem():
    messagebox.showinfo("Sucesso!" "Você clicou no botão :)")

# 3. Criar os componentes
lbl_titulo_pagina = tk.Label(janela, text="Bem-Vindo a aula de Interface Gráfica!", font=("Arial", 14, "bold"))
lbl_subtitulo_pagina = tk.Label(janela, text="Aula 12 - Desenvolvimento de paginas GUI.", font=("Arial", 10, "bold"))
btn_clique_pagina = tk.Button(janela, text="Clique Aqui", font=("Arial", 14), bg="#4a53d1", fg="white", command=mostrar_mensagem)

# 4. Posicionar os componentes na janela
lbl_titulo_pagina.pack(pady=50) #pady adiciona um espaçamento verticial
lbl_subtitulo_pagina.pack(pady=40)
btn_clique_pagina.pack(pady=50)


# 5. Rodar o loop da interface
janela.mainloop()
