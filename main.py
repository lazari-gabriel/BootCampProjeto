import customtkinter as ctk
from tkinter import messagebox
from PIL import Image


from datetime import datetime

FormatoData = "%d/%m/%Y"

Tipos_Avaliacao = ["Trabalho", "Prova", "Projeto", "Atividade"]
Status_Avaliacao = ["Pendente", "Concluído"]

class Janela_principal(ctk.CTk):
    def __init__(self):
        
        # Inicializa a classe pai / inicializar corretamente a janela.
        super().__init__()

        self.title("gerenciamento de Trabalhos, Provas, Projetos e Atividades")

        largura, altura = 1030, 600

        x = int((self.winfo_screenwidth() - largura) / 2)
        y = int((self.winfo_screenheight() - altura) / 2)
        self.geometry(f"{largura}x{altura}+{x}+{y}")

        self.resizable(False, False)


        # Tema
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        # Fonte global
        global fonte
        fonte = ctk.CTkFont(family="Comic Sans MS", size=15, weight="bold")

        # Dados
        self.lista_materias = []  
        self.lista_avaliacoes = []

        self.criar_interface()

    # Interface principal
    def criar_interface(self):

        # Frame no cabeçario da janela
        topo = ctk.CTkFrame(self)
        topo.pack(fill="x", pady=10)
                        

        self.botao_add_materia = ctk.CTkButton(topo, text="+ Matéria", font=fonte, height=30, command=self.Adicionar_Materia)
        self.botao_add_materia.pack(side="left", padx=10)

        self.botao_add_avaliacao = ctk.CTkButton(topo, text="+ Avaliação", font=fonte, height=30, command=self.Adicionar_Avaliacao)
        self.botao_add_avaliacao.pack(side="left", padx=10)

        self.botao_remover_avaliacao = ctk.CTkButton(topo, text="Remover Avaliação", font=fonte, height=30, command=self.Remover_Ultima_Avaliacao, fg_color="#E53935", hover_color="#FFAB91")
        self.botao_remover_avaliacao.pack(side="left", padx=10)

        self.botao_calculadora = ctk.CTkButton(topo, text="Calculadora de Média", font=fonte, height=30, command=self.Tela_Calculadora_Media)
        self.botao_calculadora.pack(side="right", padx=10)

        # Lista de avaliações
        self.janela_avaliacoes = ctk.CTkTextbox(self, width=900, height=400, font=fonte) # ja tem suporte a scroll
        self.janela_avaliacoes.configure(state="disabled") # para não poder editar
        self.janela_avaliacoes.pack(pady=10, padx=10, fill="both", expand=True)

        self.Atualizar_Lista()

    # Adicionar Matéria
    def Adicionar_Materia(self):
        janela = ctk.CTkToplevel(self)
        janela.title("Nova Matéria")
        janela.geometry("300x150")
        janela.resizable(False, False)

        materia_nome = ctk.CTkLabel(janela, text="Nome da matéria:", font=fonte )
        materia_nome.pack(pady=5)

        Entry_nome = ctk.CTkEntry(janela, width=200,placeholder_text="Ex: Matemática")
        Entry_nome.pack(pady=5)

        def salvar_materia():
            nome = Entry_nome.get().strip()
            if nome and nome not in self.lista_materias:
                self.lista_materias.append(nome)
                messagebox.showinfo("OK", f"Matéria '{nome}' adicionada.")
            janela.destroy()

        botao_salvar_materia = ctk.CTkButton(janela, text="Salvar", font=fonte, command=salvar_materia)
        botao_salvar_materia.pack(pady=10)

    # Adicionar Avaliação
    def Adicionar_Avaliacao(self):
        if not self.lista_materias:
            messagebox.showwarning("Atenção", "Cadastre uma matéria antes.")
            return

        janela = ctk.CTkToplevel(self)
        janela.title("Nova Avaliação")
        janela.geometry("400x550")
        janela.resizable(False, False)

        # Campos
        label_materia = ctk.CTkLabel(janela, text="Matéria:", font=fonte)
        label_materia.pack(pady=5)
        
        lista_materia = ctk.CTkComboBox(janela, values=self.lista_materias)
        lista_materia.set(self.lista_materias[0])
        lista_materia.pack(pady=5)

        label_tipo = ctk.CTkLabel(janela, text="Tipo:", font=fonte)
        label_tipo.pack(pady=5)

        lista_tipo_avaliacao = ctk.CTkComboBox(janela, values=Tipos_Avaliacao)
        lista_tipo_avaliacao.set(Tipos_Avaliacao[0])
        lista_tipo_avaliacao.pack(pady=5)

        label_titulo = ctk.CTkLabel(janela, text="Título:", font=fonte)
        label_titulo.pack(pady=5)
        Entry_titulo = ctk.CTkEntry(janela, width=250, placeholder_text="Ex: Prova Bimestral")
        Entry_titulo.pack(pady=5)

        label_data = ctk.CTkLabel(janela, text="Data (dd/mm/aaaa):", font=fonte)
        label_data.pack(pady=5)
        Entry_data = ctk.CTkEntry(janela, width=150, placeholder_text="Ex: 15/05/2023")
        Entry_data.pack(pady=5)

        label_status = ctk.CTkLabel(janela, text="Status:", font=fonte)
        label_status.pack(pady=5)
        lista_status_avaliacao = ctk.CTkComboBox(janela, values=Status_Avaliacao)
        lista_status_avaliacao.set(Status_Avaliacao[0])
        lista_status_avaliacao.pack(pady=5)

        label_nota = ctk.CTkLabel(janela, text="Nota: (campo opcional)" , font=fonte)
        label_nota.pack(pady=5)
        entrada_nota = ctk.CTkEntry(janela, width=100, placeholder_text="Ex: 8.5")
        entrada_nota.pack(pady=5)

        def salvar_avaliacao():
            materia = lista_materia.get()
            tipo = lista_tipo_avaliacao.get()
            titulo = Entry_titulo.get().strip()
            data = Entry_data.get().strip()
            status = lista_status_avaliacao.get()
            nota = entrada_nota.get().strip()

            if not titulo or not data:
                messagebox.showwarning("Erro", "Preencha todos os campos obrigatórios.")
                return

            try:
                datetime.strptime(data, FormatoData)
            except ValueError:
                messagebox.showerror("Erro", "Data inválida. Use dd/mm/aaaa.")
                return

            try:
                nota = float(nota) if nota else None
            except ValueError:
                messagebox.showerror("Erro", "Nota deve ser um número.")
                return

            avaliacao = {
                "materia": materia,
                "tipo": tipo,
                "titulo": titulo,
                "data": data,
                "status": status,
                "nota": nota
            }
            self.lista_avaliacoes.append(avaliacao)
            self.Atualizar_Lista()
            janela.destroy()

        botao_salvar_avaliacao = ctk.CTkButton(janela, text="Salvar", font=fonte, command=salvar_avaliacao)
        botao_salvar_avaliacao.pack(pady=15)

    def Remover_Ultima_Avaliacao(self):
        if not self.lista_avaliacoes:
            messagebox.showwarning("Erro", "Não há avaliações para remover.")
            return
        ultima = self.lista_avaliacoes.pop()
        messagebox.showinfo("Removido", f"Avaliação '{ultima['titulo']}' removida.")
        self.Atualizar_Lista()

    # Calculadora de média
    def Tela_Calculadora_Media(self):
        janela = ctk.CTkToplevel(self)
        janela.title('Calculadora de Média')
        janela.geometry("500x500")

        campos = []

        # Frame scrollável para notas
        frame_scroll = ctk.CTkScrollableFrame(janela)
        frame_scroll.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        # Frame lateral para botões
        frame_lateral = ctk.CTkFrame(janela, width=150)
        frame_lateral.pack(side="right", fill="y", padx=10, pady=10)

        # Adicionar campo
        def add_capos():
            IndNota = len(campos) + 1
            frame_nota = ctk.CTkFrame(frame_scroll)
            frame_nota.pack(fill="x", pady=5, padx=5)

            label = ctk.CTkLabel(frame_nota, text=f"Nota {IndNota}:", font=fonte, width=70)
            label.pack(side="left", padx=5)

            entrada_nota = ctk.CTkEntry(frame_nota , placeholder_text="Informe a nota", font=fonte)
            entrada_nota.pack(side="left", fill="x", expand=True, padx=5)

            campos.append((entrada_nota, frame_nota))

        # Remover último campo
        def remover_campo():
            if campos:
                entrada_nota, frame_nota = campos.pop()
                frame_nota.destroy()
            else:
                messagebox.showwarning("Atenção", "Não há mais campos para remover.")    

        # Calcular média
        def calcular_media():
            try:
                notas = [float(campo[0].get()) for campo in campos if campo[0].get() != ""]
                if notas:
                    media = sum(notas) / len(notas)
                    resultado.configure(text=f"Média: {media:.2f}")
                    messagebox.showinfo("Sua média é:", f"Média: {media:.2f}")
                else:
                    messagebox.showwarning("Atenção", "Digite pelo menos uma nota")
            except ValueError:
                messagebox.showwarning("Atenção", "Digite apenas números válidos")

        # Botões
        btn_adicionar = ctk.CTkButton(frame_lateral, text="Adicionar Nota", font=fonte, command=add_capos)
        btn_adicionar.pack(pady=5, fill="x")

        btn_remover = ctk.CTkButton(frame_lateral, text="Remover Nota", font=fonte, command=remover_campo, fg_color="#E53935", hover_color="#FF8A65")
        btn_remover.pack(pady=5, fill="x")

        btn_calcular = ctk.CTkButton(frame_lateral, text="Calcular Média", font=fonte, command=calcular_media)
        btn_calcular.pack(pady=5, fill="x")

        resultado = ctk.CTkLabel(frame_lateral, text="", font=fonte, width=120, fg_color="#4CAF50", corner_radius=8)
        resultado.pack(pady=20)

        # Começa com 3 campos
        for _ in range(3):
            add_capos()

    # Atualiza lista de avaliações
    def Atualizar_Lista(self):
        self.janela_avaliacoes.configure(state="normal")
        self.janela_avaliacoes.delete("0.0", "end")
        if not self.lista_avaliacoes:
            self.janela_avaliacoes.insert("end", "Nenhuma avaliação cadastrada.\n")
        else:
            for idx, avaliacao in enumerate(self.lista_avaliacoes, 1):
                linha = f"{idx}°  {avaliacao['titulo']} - {avaliacao['tipo']}  |  {avaliacao['materia']}  |  Data: {avaliacao['data']}  |  Status: {avaliacao['status']}  |  Nota: {avaliacao['nota']}\n"
                linha += "--------------------------------------------------------------------------------------------------------------\n"
                self.janela_avaliacoes.insert("end", linha)
        self.janela_avaliacoes.configure(state="disabled")

class Janela_Login(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Login / Cadastro")

        largura, altura = 500, 550
        x = int((self.winfo_screenwidth() - largura) / 2)
        y = int((self.winfo_screenheight() - altura) / 2)
        self.geometry(f"{largura}x{altura}+{x}+{y}")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        global fonte
        fonte = ctk.CTkFont(family="Comic Sans MS", size=15, weight="bold")

        # imagem da unimar
        self.logo = ctk.CTkImage(Image.open("unimar.png"), size=(220, 70))
        label_logo = ctk.CTkLabel(self, image=self.logo, text="")
        label_logo.pack(pady=10)

        # botão que alterna entre login e cadastro
        frame_top = ctk.CTkFrame(self, corner_radius=0)
        frame_top.pack(pady=5)

        btn_login_frame = ctk.CTkButton(frame_top, text="Login", width=100, command=self.mostrar_login)
        btn_login_frame.pack(side="left", padx=5)

        btn_cadastro_frame = ctk.CTkButton(frame_top, text="Cadastro", width=100, command=self.mostrar_cadastro)
        btn_cadastro_frame.pack(side="left", padx=5)

        # frames de login e cadastro
        self.frame_login = ctk.CTkFrame(self, corner_radius=15)
        self.frame_cadastro = ctk.CTkFrame(self, corner_radius=15)

        self.frame_login.pack(pady=10, padx=20, fill="both", expand=True)
        self.frame_cadastro.pack_forget()  


        self.criar_frame_login()
        self.criar_frame_cadastro()

    # frame do login
    def criar_frame_login(self):
        label_usuario = ctk.CTkLabel(self.frame_login, text="Usuário:", font=fonte)
        label_usuario.pack(pady=5)
        self.entry_usuario_login = ctk.CTkEntry(self.frame_login, placeholder_text="Digite seu usuário")
        self.entry_usuario_login.pack(pady=5)

        label_senha = ctk.CTkLabel(self.frame_login, text="Senha:", font=fonte)
        label_senha.pack(pady=5)

        self.entry_senha_login = ctk.CTkEntry(self.frame_login, placeholder_text="Digite sua senha", show="*")
        self.entry_senha_login.pack(pady=5)

        # Checkbox mostrar senha
        self.mostrar_senha_var_login = ctk.BooleanVar()
        chk_mostrar = ctk.CTkCheckBox(self.frame_login, text="Mostrar senha", variable=self.mostrar_senha_var_login, command=self.mostrar_senha_login)
        chk_mostrar.pack(pady=5)

        btn_login = ctk.CTkButton(self.frame_login, text="Login", width=200, command=self.fazer_login)
        btn_login.pack(pady=10)

    # frame do cadastro
    def criar_frame_cadastro(self):
        label_usuario_cad = ctk.CTkLabel(self.frame_cadastro, text="Usuário:", font=fonte)
        label_usuario_cad.pack(pady=3)
        self.entry_usuario_cad = ctk.CTkEntry(self.frame_cadastro, placeholder_text="Digite seu usuário")
        self.entry_usuario_cad.pack(pady=3)

        label_email = ctk.CTkLabel(self.frame_cadastro, text="Email:", font=fonte)
        label_email.pack(pady=3)
        self.entry_email_cad = ctk.CTkEntry(self.frame_cadastro, placeholder_text="Digite seu email")
        self.entry_email_cad.pack(pady=3)

        label_senha_cad = ctk.CTkLabel(self.frame_cadastro, text="Senha:", font=fonte)
        label_senha_cad.pack(pady=3)
        self.entry_senha_cad = ctk.CTkEntry(self.frame_cadastro, placeholder_text="Digite sua senha", show="*") # show="*" para esconder a senha
        self.entry_senha_cad.pack(pady=3)

        label_confirmar = ctk.CTkLabel(self.frame_cadastro, text="Confirmar senha:", font=fonte)
        label_confirmar.pack(pady=3)
        self.entry_confirmar_cad = ctk.CTkEntry(self.frame_cadastro, placeholder_text="Confirme sua senha", show="*")
        self.entry_confirmar_cad.pack(pady=3)

        # Checkbox mostrar senha cadastro
        self.mostrar_senha_var_cad = ctk.BooleanVar()
        check_cadastro = ctk.CTkCheckBox(self.frame_cadastro, text="Mostrar senha", variable=self.mostrar_senha_var_cad, command=self.mostrar_senha_cadastro)
        check_cadastro.pack(pady=5)

        btn_cadastrar = ctk.CTkButton(self.frame_cadastro, text="Cadastrar", width=200, fg_color="#2196F3", hover_color="#1976D2", command=self.cadastrar_usuario)
        btn_cadastrar.pack(pady=10)

    # mostrar ou esconder senha
    def mostrar_senha_login(self):
        if self.mostrar_senha_var_login.get():
            self.entry_senha_login.configure(show="")
        else:
            self.entry_senha_login.configure(show="*")

    def mostrar_senha_cadastro(self):
        if self.mostrar_senha_var_cad.get():
            self.entry_senha_cad.configure(show="")
            self.entry_confirmar_cad.configure(show="")
        else:
            self.entry_senha_cad.configure(show="*")
            self.entry_confirmar_cad.configure(show="*")

    # mostrar frame correto
    def mostrar_login(self):
        self.frame_cadastro.pack_forget()
        self.frame_login.pack(pady=10, padx=20, fill="both", expand=True)

    def mostrar_cadastro(self):
        self.frame_login.pack_forget()
        self.frame_cadastro.pack(pady=10, padx=20, fill="both", expand=True)

    # logar
    def fazer_login(self):
        usuario = self.entry_usuario_login.get().strip()
        senha = self.entry_senha_login.get().strip()
        try:
            with open("usuarios.txt", "r") as f:
                for linha in f:
                    u, s, email = linha.strip().split(":")
                    if u == usuario and s == senha:
                        messagebox.showinfo("Login", f"Bem-vindo {usuario}!")
                        
                        # Esconde a janela de login
                        self.withdraw()
                        
                        # Abre a janela principal
                        app_principal = Janela_principal()
                        app_principal.mainloop()
                        
                        # Depois que a principal fechar, destrói a janela de login
                        self.destroy()
                        return
            messagebox.showerror("Erro", "Usuário ou senha incorretos!")
        except FileNotFoundError:
            messagebox.showerror("Erro", "Nenhum usuário cadastrado ainda.")

    # cadatrar
    def cadastrar_usuario(self):
        usuario = self.entry_usuario_cad.get().strip()
        email = self.entry_email_cad.get().strip()
        senha = self.entry_senha_cad.get().strip()
        confirmar = self.entry_confirmar_cad.get().strip()

        if not usuario or not email or not senha or not confirmar:
            messagebox.showwarning("Aviso", "Preencha todos os campos!")
            return

        if senha != confirmar:
            messagebox.showerror("Erro", "As senhas não coincidem!")
            return

        try:
            with open("usuarios.txt", "r") as f:
                for linha in f:
                    u, _, _ = linha.strip().split(":")
                    if u == usuario:
                        messagebox.showerror("Erro", "Usuário já existe!")
                        app = Janela_principal()
                        app.mainloop()
                        return
        except FileNotFoundError:
            pass

        with open("usuarios.txt", "a") as f:
            f.write(f"{usuario}:{senha}:{email}\n")

        messagebox.showinfo("Cadastro", "Usuário cadastrado com sucesso!")

# Roda a janela
if __name__ == "__main__":
    app = Janela_Login()
    app.mainloop()