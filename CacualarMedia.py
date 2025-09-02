from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
# Função para adicionar campos de nota
def add_capos():
    IndNota = len(campos) + 1

    # Frame para cada linha de nota
    frame_nota = ttk.Frame(frame_campos, style="light_steel_blue.TFrame")
    frame_nota.grid(row=IndNota, column=0, pady=5, sticky="ew")

    # Label
    label = ttk.Label(frame_nota, text=f"Nota {IndNota}:", background=light_steel_blue, foreground=dark_teal_blue, font=("Arial", 12, "bold"))
    label.pack(side="left")

    # Entrada
    entrada_nota = ttk.Entry(frame_nota, style="Custom.TEntry", font=("Arial", 12, "bold"))
    entrada_nota.pack(side="left", padx=12, fill="x")
    campos.append(entrada_nota)

# Função para calcular a média
def calcular_media():
    try:
        notas = [float(campo.get()) for campo in campos if campo.get() != ""]
        if notas:
            media = sum(notas) / len(notas)
            resultado.config(text=f"Média: {media:.2f}")
            messagebox.showinfo("Sua média é : ", f"Média: {media:.2f}")
        else:
            messagebox.showwarning("Atenção", "Digite pelo menos uma nota")

    except ValueError:
         messagebox.showwarning("Atenção", "Digite apenas números válidos")

# Cores
dark_teal_blue = "#0A2E3D"
light_steel_blue = "#B0C4DE"
color_green_leaf = "#4CAF50"
color_red = "#FF5722"
color_blue_sky = "#2196F3"
color_white = "white"

# Janela
janela = Tk()
janela.title('Calculadora de Média')
janela.geometry("500x500")
janela.config(bg=light_steel_blue)
janela.resizable(False, False)

# Configurar grid da janela para responsividade
janela.grid_columnconfigure(0, weight=3)  # coluna das notas
janela.grid_columnconfigure(1, weight=1)  # coluna lateral
janela.grid_rowconfigure(1, weight=1)     # área central cresce

# Tema ttk
style = ttk.Style()
style.theme_use('clam')

# Estilos
style.configure("light_steel_blue.TFrame", background=light_steel_blue)
style.configure("Green.TButton", background=color_green_leaf, foreground=color_white, borderwidth=0, relief="flat", font=("Arial", 10),)
style.map("Green.TButton", background=[('active', '#45A049')])

style.configure("blue_sky.TButton", background=color_blue_sky, foreground=color_white, borderwidth=0, relief="flat", font=("Arial", 10),)
style.map("blue_sky.TButton", background=[('active', '#1976D2')])
style.configure("Custom.TEntry", fieldbackground=color_white, foreground=dark_teal_blue, borderwidth=2, relief="flat", padding=5)

# Título
titulo = ttk.Label(janela, text="Insira as informações abaixo para Calcular a média:", padding=10,
                   background=dark_teal_blue, foreground=color_white, font=("Arial", 14))
titulo.grid(row=0, column=0, columnspan=2, pady=10, padx=10, sticky="ew")

# Frame para os campos (coluna 0)
frame_campos = ttk.Frame(janela, padding=10, style="light_steel_blue.TFrame")
frame_campos.grid(row=1, column=0, padx=10, sticky="nsew")

# Frame lateral (coluna 1) → botões e resultado
frame_lateral = ttk.Frame(janela, padding=10, style="light_steel_blue.TFrame")
frame_lateral.grid(row=1, column=1, padx=10, sticky="nsew")

# Configurar frame_campos para expandir
frame_campos.grid_columnconfigure(0, weight=1)

# Botão Adicionar
btn_adicionar = ttk.Button(frame_lateral, text="Adicionar Nota", style="blue_sky.TButton", command=add_capos)
btn_adicionar.pack(pady=15,)

# Botão Calcular
btn_calcular = ttk.Button(frame_lateral, text="Calcular Média", style="Green.TButton", command=calcular_media)
btn_calcular.pack(pady=15,)

# Label de resultado
resultado = ttk.Label(frame_lateral, text="", background=light_steel_blue, foreground=dark_teal_blue, font=("Arial", 12, "bold"))
resultado.pack(pady=20, )

# Lista de campos
campos = []

# Já começa com 3 notas
for _ in range(3):
    add_capos()

janela.mainloop()
