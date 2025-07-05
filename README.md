<body>
    <div class="container">
        <h1>FlaskAPI</h1>
<p>
    <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="Python 3.8+" class="badge">
    <img src="https://img.shields.io/badge/flask-2.0+-green.svg" alt="Flask 2.0+" class="badge">
    <img src="https://img.shields.io/badge/status-em%20desenvolvimento-orange" alt="Status: Em desenvolvimento" class="badge">
</p>
        <p>Uma API RESTful desenvolvida com Flask, SQLAlchemy e autenticação JWT, para gerenciamento de posts e usuários. Ideal para aprendizado e testes de desenvolvimento de APIs em Python.</p>

  <h2>📋 Índice</h2>
  <ul>
      <li><a href="#sobre">Sobre</a></li>
      <li><a href="#funcionalidades">Funcionalidades</a></li>
      <li><a href="#tecnologias">Tecnologias</a></li>
      <li><a href="#pré-requisitos">Pré-requisitos</a></li>
      <li><a href="#instalação">Instalação</a></li>
      <li><a href="#uso">Uso</a></li>
      <li><a href="#deploy-no-render">Deploy no Render</a></li>
      <li><a href="#estrutura-do-projeto">Estrutura do Projeto</a></li>
      <li><a href="#contribuição">Contribuição</a></li>
      <li><a href="#licença">Licença</a></li>
      <li><a href="#contato">Contato</a></li>
  </ul>

  <h2 id="sobre">ℹ️ Sobre</h2>
  <p>FlaskAPI é um projeto de backend que implementa uma API RESTful para criar, listar, atualizar e excluir posts, com autenticação de usuários via JWT. Utiliza Flask como framework web, SQLAlchemy para gerenciamento de banco de dados SQLite e Flask-JWT-Extended para segurança. O projeto é ideal para desenvolvedores que desejam aprender sobre APIs, autenticação e integração com bancos de dados.</p>

  <h2 id="funcionalidades">✨ Funcionalidades</h2>
  <ul>
      <li><strong>Autenticação de Usuários</strong>: Registro e login com geração de tokens JWT.</li>
      <li><strong>Gerenciamento de Posts</strong>: CRUD completo (Create, Read, Update, Delete) para posts, com validação de autor.</li>
      <li><strong>Banco de Dados</strong>: Persistência de dados em SQLite usando SQLAlchemy.</li>
      <li><strong>Testes</strong>: Suporte para testes unitários com pytest (em desenvolvimento).</li>
  </ul>

  <h2 id="tecnologias">🛠️ Tecnologias</h2>
  <ul>
      <li>Python 3.8+</li>
      <li>Flask 2.0+</li>
      <li>Flask-SQLAlchemy</li>
      <li>Flask-JWT-Extended</li>
      <li>pytest</li>
      <li>SQLite</li>
      <li>uv (gerenciador de ambiente e dependências)</li>
      <li>Insomnia/Postman (para testar endpoints)</li>
      <li>Render (sugestão para deploy)</li>
  </ul>

  <h2 id="pré-requisitos">📋 Pré-requisitos</h2>
  <ul>
      <li>Python 3.8 ou superior instalado.</li>
      <li><code>uv</code> instalado para gerenciar ambiente e dependências.</li>
      <li>Opcional: Insomnia ou Postman para testar os endpoints da API.</li>
      <li>Conta no Render (para deploy, se desejar).</li>
  </ul>

  <h2 id="instalação">🚀 Instalação</h2>
  <p>Siga os passos abaixo para configurar o projeto localmente usando <code>uv</code>:</p>
  <ol>
      <li><strong>Clone o repositório</strong>:
          <pre><code>git clone https://github.com/napolisiqueira/FlaskAPI.git
cd FlaskAPI</code></pre>
            </li>
            <li><strong>Instale o</strong> <code>uv</code> (se ainda não tiver):
                <pre><code>curl -LsSf https://astral.sh/uv/install.sh | sh</code></pre>
            </li>
            <li><strong>Crie e sincronize o ambiente virtual com</strong> <code>uv</code>:
                <pre><code>uv venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate  # Windows</code></pre>
            </li>
            <li><strong>Instale as dependências</strong>:
                <pre><code>uv pip install -r requirements.txt</code></pre>
            </li>
            <li><strong>Configure o banco de dados</strong>:
                <p>O projeto usa SQLite por padrão. Execute o script inicial para criar as tabelas:</p>
                <pre><code>uv run python app.py</code></pre>
                <p>Isso criará o arquivo <code>database.db</code> na raiz do projeto.</p>
            </li>
        </ol>

  <h2 id="uso">▶️ Uso</h2>
  <ol>
      <li><strong>Inicie a API</strong>:
          <pre><code>uv run python app.py</code></pre>
          <p>A API estará disponível em <code>http://localhost:5000</code>.</p>
      </li>
      <li><strong>Teste os endpoints</strong>: Use Insomnia ou Postman para interagir com a API. Exemplos de endpoints:</li>
      <ul>
          <li><strong>Registro de usuário</strong>:
              <pre><code>POST http://localhost:5000/register
Content-Type: application/json
{
  "username": "seu_usuario",
  "password": "sua_senha"
}</code></pre>
                </li>
                <li><strong>Login</strong>:
                    <pre><code>POST http://localhost:5000/login
Content-Type: application/json
{
  "username": "seu_usuario",
  "password": "sua_senha"
}</code></pre>
                    <p>Retorna um token JWT para autenticação.</p>
                </li>
                <li><strong>Criar post</strong> (requer token):
                    <pre><code>POST http://localhost:5000/posts
Authorization: Bearer &lt;seu_token&gt;
Content-Type: application/json
{
  "title": "Meu Post",
  "body": "Conteúdo do post"
}</code></pre>
                </li>
                <li><strong>Listar posts</strong>:
                    <pre><code>GET http://localhost:5000/posts</code></pre>
                </li>
            </ul>
            <li><strong>Exemplo de resposta</strong> (listagem de posts):
                <pre><code>{
  "message": [
    {
      "post_id": 1,
      "title": "Meu Post",
      "body": "Conteúdo do post",
      "created": "2025-06-17T08:00:00",
      "author_id": 1
    }
  ]
}</code></pre>
            </li>
        </ol>

  <h2 id="deploy-no-render">🌐 Deploy no Render</h2>
  <p>O Render é uma plataforma recomendada para hospedar esta API de forma simples e gratuita (com limitações no plano free). Siga os passos abaixo para fazer o deploy:</p>
  <ol>
      <li><strong>Crie uma conta no Render</strong>:
          <p>Acesse <a href="https://render.com">render.com</a> e crie uma conta gratuita.</p>
      </li>
      <li><strong>Crie um novo serviço Web</strong>:
          <p>No dashboard do Render, clique em "New" > "Web Service".</p>
          <p>Conecte seu repositório GitHub (<code>napolisiqueira/FlaskAPI</code>) diretamente ao Render.</p>
      </li>
      <li><strong>Configure o serviço</strong>:
          <ul>
              <li><strong>Nome</strong>: Escolha um nome para o serviço (ex.: <code>flask-api</code>).</li>
              <li><strong>Runtime</strong>: Selecione <code>Python</code>.</li>
              <li><strong>Build Command</strong>: Use o comando para instalar dependências com <code>uv</code>:
                  <pre><code>uv pip install -r requirements.txt</code></pre>
              </li>
              <li><strong>Start Command</strong>: Defina o comando para iniciar a API:
                  <pre><code>uv run python app.py</code></pre>
              </li>
              <li><strong>Environment Variables</strong>: Adicione variáveis, se necessário (ex.: <code>FLASK_ENV=production</code>).</li>
              <li><strong>Instance Type</strong>: Escolha "Free" para testes ou um plano pago para maior escalabilidade.</li>
          </ul>
      </li>
      <li><strong>Deploy</strong>:
          <p>Clique em "Create Web Service" e aguarde o Render clonar o repositório, instalar dependências e iniciar a API.</p>
          <p>Após o deploy, o Render fornecerá uma URL pública (ex.: <code>https://flask-api.onrender.com</code>) para acessar a API.</p>
      </li>
      <li><strong>Teste o deploy</strong>:
          <p>Use Insomnia ou Postman para testar os endpoints na URL fornecida pelo Render, como <code>https://flask-api.onrender.com/register</code>.</p>
      </li>
  </ol>
  <p><strong>Notas sobre o Render</strong>:</p>
  <ul>
      <li>No plano gratuito, o serviço pode "dormir" após inatividade, causando um pequeno atraso no primeiro acesso.</li>
      <li>Certifique-se de que o SQLite funciona no Render (o banco de dados é armazenado no disco efêmero). Para produção, considere migrar para um banco como PostgreSQL, que o Render suporta nativamente.</li>
  </ul>

  <h2 id="estrutura-do-projeto">🗂️ Estrutura do Projeto</h2>
  <pre><code>FlaskAPI/
├── app.py                # Arquivo principal da aplicação
├── models.py             # Modelos do banco de dados (Post, User)
├── routes.py             # Definição dos endpoints da API
├── database.db           # Banco de dados SQLite (gerado após execução)
├── pyproject.toml        # Dependências do projeto
├── uv.lock               # Para melhor gerenciamento de dependencias
├── tests/                # Pasta para testes unitários (em desenvolvimento)
└── README.md             # Documentação do projeto
</code></pre>

        <h2 id="contribuição">🤝 Contribuição</h2>
        <p>Contribuições são bem-vindas! Siga os passos abaixo para contribuir:</p>
        <ol>
            <li>Fork o repositório.</li>
            <li>Crie uma branch para sua feature (<code>git checkout -b feature/nova-funcionalidade</code>).</li>
            <li>Commit suas mudanças (<code>git commit -m "Adiciona nova funcionalidade"</code>).</li>
            <li>Push para a branch (<code>git push origin feature/nova-funcionalidade</code>).</li>
            <li>Abra um Pull Request.</li>
        </ol>
        <p>Por favor, abra uma issue para discutir grandes mudanças antes de implementá-las.</p>

        <h2 id="licença">📜 Licença</h2>
        <p>Este projeto está licenciado sob a MIT License.</p>

        <h2 id="contato">📬 Contato</h2>
        <ul>
            <li>GitHub: <a href="https://github.com/napolisiqueira">napolisiqueira</a></li>
            <li>Email: (adicione seu email se desejar)</li>
        </ul>
    </div>
</body>
</html>
