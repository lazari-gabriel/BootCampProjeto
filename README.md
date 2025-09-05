# Gerenciador de Trabalhos, Provas, Projetos e Atividades

Aplicativo de desktop desenvolvido em **Python** com **CustomTkinter** para gerenciar matérias e avaliações, incluindo trabalhos, provas, projetos e atividades. Possui funcionalidades para adicionar, remover e visualizar avaliações, além de uma **calculadora de médias integrada** e **login/cadastro de usuários**.

O sistema oferece uma **interface moderna e intuitiva**, com tema escuro, tornando a organização acadêmica mais prática e visual.

---

## Funcionalidades

* **Login e Cadastro de Usuários:** Sistema seguro para múltiplos usuários, armazenando informações em arquivo local (`usuarios.txt`).
* Adicionar e remover **matérias**.
* Adicionar e remover **avaliações** (trabalhos, provas, projetos e atividades).
* Visualizar todas as avaliações cadastradas em uma lista organizada.
* **Calculadora de média** para suas notas, com suporte a múltiplos campos.
* Interface moderna com **tema escuro** utilizando CustomTkinter.

---

## Tecnologias Utilizadas

* Python 3.x
* [Tkinter](https://docs.python.org/3/library/tkinter.html) – biblioteca nativa para GUI do Python.
* [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) – versão estilizada e moderna do Tkinter.
* [Pillow (PIL)](https://pillow.readthedocs.io/) – para manipulação de imagens no login.

---

## Instalação

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

## Como Usar

### Tela de Login e Cadastro

* **Login:** Informe seu usuário e senha para acessar o sistema. É possível mostrar ou esconder a senha.
* **Cadastro:** Crie um novo usuário informando usuário, email, senha e confirmação da senha. Também é possível mostrar ou esconder as senhas.

### Gerenciamento de Matérias e Avaliações

1. **Adicionar Matéria:** Clique em **+ Matéria** e informe o nome da matéria.
2. **Adicionar Avaliação:** Clique em **+ Avaliação**, selecione a matéria, tipo de avaliação, status, título, data e nota (opcional).
3. **Visualizar Avaliações:** Todas as avaliações cadastradas aparecem na lista principal.
4. **Remover Avaliação:** Utilize o botão **Remover Avaliação** para deletar a última avaliação cadastrada.

### Calculadora de Média

* Abra a calculadora, insira suas notas e clique em **Calcular Média**.
* É possível adicionar ou remover campos conforme necessário.

---

## Estrutura do Projeto

```
gerenciador-avaliacoes/
│
├── main.py               # Código principal do aplicativo
├── usuarios.txt          # Armazena os usuários cadastrados (gerado automaticamente)
├── unimar.png            # Logo utilizada no login
├── README.md             # Documentação do projeto
└── LICENSE               # Licença MIT
```

---

## Licença

Este projeto está licenciado sob a **Licença MIT**. Consulte o arquivo `LICENSE` para mais informações.
