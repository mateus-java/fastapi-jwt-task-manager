# 🚀 FastAPI JWT Task Manager

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![SQLModel](https://img.shields.io/badge/SQLModel-ORM-red?style=for-the-badge&logo=sqlite&logoColor=white)](https://sqlmodel.tiangolo.com/)
[![JWT](https://img.shields.io/badge/JWT-Authentication-black?style=for-the-badge&logo=jsonwebtokens&logoColor=white)](https://jwt.io/)

</div>

---

## 📖 Sobre o Projeto / About the Project

### [PT-BR]
API RESTful moderna e segura desenvolvida em Python com **FastAPI**, projetada para o gerenciamento eficiente de tarefas de usuários com autenticação robusta baseada em **JSON Web Tokens (JWT)**. O projeto foca em boas práticas de engenharia de backend, criptografia de senhas com `Bcrypt`, modelagem de dados relacional com `SQLModel` e documentação automática interativa.

### [EN]
Modern and secure RESTful API built with Python and **FastAPI**, designed for user task management with robust **JSON Web Tokens (JWT)** authentication. This project focuses on backend engineering best practices, password hashing with `Bcrypt`, relational data modeling with `SQLModel`, and automatic interactive documentation.

---

## 🛠️ Tecnologias / Tech Stack

* **Python** — Linguagem principal de desenvolvimento.
* **FastAPI** — Framework web moderno, de altíssima performance e assíncrono.
* **SQLModel** — ORM moderno combinando SQLAlchemy e Pydantic.
* **SQLite** — Banco de dados relacional leve e embutido.
* **Passlib & Bcrypt** — Criptografia segura de credenciais.
* **Python-Jose** — Emissão e validação de tokens JWT.

---

## ⚙️ Funcionalidades / Features

* **Registro de Usuários (`/register`)**: Criação de contas com senhas protegidas por hash.
* **Autenticação JWT (`/login`)**: Login seguro gerando tokens de acesso com tempo de expiração.
* **Gerenciamento de Tarefas (`/tasks/`)**:
  * Criação, listagem e controle de tarefas exclusivas por usuário autenticado.
  * Proteção de rotas através de dependências (`OAuth2PasswordBearer`).
* **Documentação Interativa**: Swagger UI (`/docs`) e ReDoc (`/redoc`) gerados automaticamente.

---

## 🚀 Como Executar o Projeto / How to Run

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/fastapi-jwt-task-manager.git
   cd fastapi-jwt-task-manager
   ```

2. **Crie e ative o ambiente virtual:**
   ```bash
   python -m venv venv
   # No Windows:
   venv\Scripts\activate
   # No Linux/Mac:
   source venv/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute a aplicação:**
   ```bash
   uvicorn main:app --reload
   ```

5. **Acesse a documentação:**
   Abra o navegador em `http://127.0.0.1:8000/docs` para interagir com a API.

---

## 📌 Rotas da API / API Endpoints

| Método | Endpoint | Descrição / Description |
| :--- | :--- | :--- |
| `POST` | `/register` | Registo de um novo utilizador |
| `POST` | `/login` | Autenticação e obtenção do token JWT |
| `POST` | `/tasks/` | Criação de uma nova tarefa (Requer Token) |
| `GET` | `/tasks/` | Listagem das tarefas do utilizador logado (Requer Token) |

---

## 👤 Autor / Author

Desenvolvido com dedicação por Sindi. 💻✨