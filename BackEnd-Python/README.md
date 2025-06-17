# FlaskAPI

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)

![Flask](https://img.shields.io/badge/flask-2.0+-green.svg)

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-orange)Uma API RESTful desenvolvida com Flask, SQLAlchemy e autenticação JWT, para gerenciamento de posts e usuários. Ideal para aprendizado e testes de desenvolvimento de APIs em Python.

## 📋 Índice

- Sobre
- Funcionalidades
- Tecnologias
- Pré-requisitos
- Instalação
- Uso
- Deploy no Render
- Estrutura do Projeto
- Contribuição
- Licença
- Contato

## ℹ️ Sobre

FlaskAPI é um projeto de backend que implementa uma API RESTful para criar, listar, atualizar e excluir posts, com autenticação de usuários via JWT. Utiliza Flask como framework web, SQLAlchemy para gerenciamento de banco de dados SQLite e Flask-JWT-Extended para segurança. O projeto é ideal para desenvolvedores que desejam aprender sobre APIs, autenticação e integração com bancos de dados.

## ✨ Funcionalidades

- **Autenticação de Usuários**: Registro e login com geração de tokens JWT.
- **Gerenciamento de Posts**: CRUD completo (Create, Read, Update, Delete) para posts, com validação de autor.
- **Banco de Dados**: Persistência de dados em SQLite usando SQLAlchemy.
- **Testes**: Suporte para testes unitários com pytest (em desenvolvimento).

## 🛠️ Tecnologias

- Python 3.8+
- Flask 2.0+
- Flask-SQLAlchemy
- Flask-JWT-Extended
- pytest
- SQLite
- uv (gerenciador de ambiente e dependências)
- Insomnia/Postman (para testar endpoints)
- Render (sugestão para deploy)

## 📋 Pré-requisitos

- Python 3.8 ou superior instalado.
- `uv` instalado para gerenciar ambiente e dependências.
- Opcional: Insomnia ou Postman para testar os endpoints da API.
- Conta no Render (para deploy, se desejar).

## 🚀 Instalação

Siga os passos abaixo para configurar o projeto localmente usando `uv`:

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/napolisiqueira/FlaskAPI.git
   cd FlaskAPI
   ```

2. **Instale o** `uv` (se ainda não tiver):

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. **Crie e sincronize o ambiente virtual com** `uv`:

   ```bash
   uv venv
   source .venv/bin/activate  # Linux/Mac
   .venv\Scripts\activate  # Windows
   ```

4. **Instale as dependências**:

   ```bash
   uv pip install -r requirements.txt
   ```

5. **Configure o banco de dados**:

   - O projeto usa SQLite por padrão. Execute o script inicial para criar as tabelas:

     ```bash
     uv run python app.py
     ```
   - Isso criará o arquivo `database.db` na raiz do projeto.

## ▶️ Uso

1. **Inicie a API**:

   ```bash
   uv run python app.py
   ```

   A API estará disponível em `http://localhost:5000`.

2. **Teste os endpoints**: Use Insomnia ou Postman para interagir com a API. Exemplos de endpoints:

   - **Registro de usuário**:

     ```http
     POST http://localhost:5000/register
     Content-Type: application/json
     {
       "username": "seu_usuario",
       "password": "sua_senha"
     }
     ```
   - **Login**:

     ```http
     POST http://localhost:5000/login
     Content-Type: application/json
     {
       "username": "seu_usuario",
       "password": "sua_senha"
     }
     ```

     Retorna um token JWT para autenticação.
   - **Criar post** (requer token):

     ```http
     POST http://localhost:5000/posts
     Authorization: Bearer <seu_token>
     Content-Type: application/json
     {
       "title": "Meu Post",
       "body": "Conteúdo do post"
     }
     ```
   - **Listar posts**:

     ```http
     GET http://localhost:5000/posts
     ```

3. **Exemplo de resposta** (listagem de posts):

   ```json
   {
     "message": [
       {
         "post_id": 1,
         "title": "Meu Post",
         "body": "Conteúdo do post",
         "created": "2025-06-17T08:00:00",
         "author_id": 1
       }
     ]
   }
   ```

## 🌐 Deploy no Render

O Render é uma plataforma recomendada para hospedar esta API de forma simples e gratuita (com limitações no plano free). Siga os passos abaixo para fazer o deploy:

1. **Crie uma conta no Render**:

   - Acesse render.com e crie uma conta gratuita.

2. **Crie um novo serviço Web**:

   - No dashboard do Render, clique em "New" &gt; "Web Service".
   - Conecte seu repositório GitHub (`napolisiqueira/FlaskAPI`) diretamente ao Render.

3. **Configure o serviço**:

   - **Nome**: Escolha um nome para o serviço (ex.: `flask-api`).
   - **Runtime**: Selecione `Python`.
   - **Build Command**: Use o comando para instalar dependências com `uv`:

     ```bash
     uv pip install -r requirements.txt
     ```
   - **Start Command**: Defina o comando para iniciar a API:

     ```bash
     uv run python app.py
     ```
   - **Environment Variables**: Adicione variáveis, se necessário (ex.: `FLASK_ENV=production`).
   - **Instance Type**: Escolha "Free" para testes ou um plano pago para maior escalabilidade.

4. **Deploy**:

   - Clique em "Create Web Service" e aguarde o Render clonar o repositório, instalar dependências e iniciar a API.
   - Após o deploy, o Render fornecerá uma URL pública (ex.: `https://flask-api.onrender.com`) para acessar a API.

5. **Teste o deploy**:

   - Use Insomnia ou Postman para testar os endpoints na URL fornecida pelo Render, como `https://flask-api.onrender.com/register`.

**Notas sobre o Render**:

- No plano gratuito, o serviço pode "dormir" após inatividade, causando um pequeno atraso no primeiro acesso.
- Certifique-se de que o SQLite funciona no Render (o banco de dados é armazenado no disco efêmero). Para produção, considere migrar para um banco como PostgreSQL, que o Render suporta nativamente.

## 🗂️ Estrutura do Projeto

```plaintext
FlaskAPI/
├── app.py                # Arquivo principal da aplicação
├── models.py             # Modelos do banco de dados (Post, User)
├── routes.py             # Definição dos endpoints da API
├── database.db           # Banco de dados SQLite (gerado após execução)
├── pyproject.toml        # Dependências do projeto
├── uv.lock               # Para melhor gerenciamento de dependencias
├── tests/                # Pasta para testes unitários (em desenvolvimento)
└── README.md             # Documentação do projeto
```

## 🤝 Contribuição

Contribuições são bem-vindas! Siga os passos abaixo para contribuir:

1. Fork o repositório.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`).
3. Commit suas mudanças (`git commit -m "Adiciona nova funcionalidade"`).
4. Push para a branch (`git push origin feature/nova-funcionalidade`).
5. Abra um Pull Request.

Por favor, abra uma issue para discutir grandes mudanças antes de implementá-las.

## 📜 Licença

Este projeto está licenciado sob a MIT License.

## 📬 Contato

- GitHub: napolisiqueira
- Email: (adicione seu email se desejar)