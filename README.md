# 🎓 Gerenciador de Trabalhos, Provas, Projetos e Atividades  

Aplicativo de desktop desenvolvido em **Python** com **CustomTkinter** para gerenciar matérias e avaliações acadêmicas.  
Com ele, você pode organizar **trabalhos, provas, projetos e atividades**, além de calcular suas médias de forma prática.  

A interface moderna com **tema escuro** proporciona uma experiência intuitiva e agradável.  

---

## 🚀 Funcionalidades  

✅ **Login e Cadastro de Usuários**  
- Sistema de autenticação seguro para múltiplos usuários.  
- Armazenamento local em `usuarios.txt`.  
- Exibição/ocultação de senha.  

✅ **Gerenciamento de Matérias**  
- Adicionar e remover matérias.  
- Organização por listas.  

✅ **Gerenciamento de Avaliações**  
- Adicionar trabalhos, provas, projetos e atividades.  
- Informar título, tipo, status, data e nota (opcional).  
- Remover avaliações individualmente.  
- Listagem clara e organizada de todas as avaliações.  

✅ **Calculadora de Médias Integrada**  
- Inserção de múltiplas notas.  
- Adicionar/remover campos dinamicamente.  
- Cálculo automático da média.  

✅ **Interface Moderna**  
- Tema escuro com **CustomTkinter**.  
- Ícones e imagens personalizadas (via **Pillow**).  
- Layout intuitivo para facilitar a navegação.  

---

## 🛠 Tecnologias Utilizadas  

- **Python 3.x**  
- [Tkinter](https://docs.python.org/3/library/tkinter.html) – GUI nativa do Python  
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) – versão moderna e estilizada do Tkinter  
- [Pillow (PIL)](https://pillow.readthedocs.io/) – manipulação de imagens no login  

---

## 📥 Instalação  

1. Clone este repositório:  
```bash
git clone https://github.com/seu-usuario/gerenciador-avaliacoes.git
```  

2. Acesse a pasta do projeto:  
```bash
cd gerenciador-avaliacoes
```  

3. Instale as dependências:  
```bash
pip install customtkinter pillow
```  

4. Execute o aplicativo:  
```bash
python main.py
```  

---

## 📘 Como Usar  

### 🔑 Tela de Login e Cadastro  
- **Login:** Informe usuário e senha para entrar.  
- **Cadastro:** Informe usuário, e-mail, senha e confirmação da senha.  
- Opção de **mostrar/ocultar senha** disponível.  

### 📚 Gerenciamento de Matérias e Avaliações  
1. Clique em **+ Matéria** e adicione o nome da disciplina.  
2. Clique em **+ Avaliação** e preencha:  
   - Matéria  
   - Tipo (Trabalho, Prova, Projeto, Atividade)  
   - Status (pendente, concluído etc.)  
   - Título da avaliação  
   - Data da entrega  
   - Nota (opcional)  
3. Todas as avaliações aparecem na **lista principal**.  
4. Use **Remover Avaliação** para deletar a última avaliação cadastrada.  

### 🧮 Calculadora de Média  
- Adicione suas notas nos campos.  
- Clique em **Calcular Média** para obter o resultado.  
- É possível adicionar/remover quantos campos forem necessários.  

---

## 📂 Estrutura do Projeto  

```
gerenciador-avaliacoes/
│
├── main.py               # Código principal do aplicativo
├── usuarios.txt          # Armazena os usuários cadastrados (gerado automaticamente)
├── unimar.png            # Logo exibida na tela de login
├── README.md             # Documentação do projeto
└── LICENSE               # Licença MIT
```

---


## 📌 Possíveis Melhorias Futuras  

- [ ] Adicionar suporte a **banco de dados SQLite** (substituindo `usuarios.txt`).  
- [ ] Permitir **edição de avaliações já cadastradas**.  
- [ ] Notificações de **prazos próximos**.  
- [ ] Exportação das avaliações em **PDF/Excel**.  
- [ ] Sistema de **filtros e pesquisa** por matéria/tipo/status.  

---

## 📜 Licença  

Este projeto está licenciado sob a **Licença MIT**.  
Consulte o arquivo [`LICENSE`](LICENSE) para mais informações.  
