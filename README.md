# 📌API PLANO DE PREVIDÊNCIA

<div align="center">
  <img height="90em" src="https://media.licdn.com/dms/image/v2/D4D16AQFdyUGy8Mtl1A/profile-displaybackgroundimage-shrink_350_1400/profile-displaybackgroundimage-shrink_350_1400/0/1703082248532?e=1747872000&v=beta&t=bD-iu-29yDw0L7P2FyZM7yHmYnCq6YEFG4uYmhvy7dk"/>
</div>


## Sumário 🔄

1. [Descrição](#descrição-)
2. [Desenvolvimento](#desenvolvimento-)
3. [Configuração do Ambiente](#configuração-do-ambiente-)

---
## Descrição 📝
Esta é uma API desenvolvida em Python utilizando FastAPI, seguindo a arquitetura MVC (Model-View-Controller). A API conta com testes automatizados para garantir qualidade e confiabilidade, além de utilizar PostgreSQL como banco de dados. Que simula o back-end de uma consultoria de vendas de planos de previdência

## Desenvolvimento 👨‍💻
`Controller` ✅
- Gerenciar as requisições HTTP
- - GET🟢
- - POST🔵
- - PATCH🟠
- - DELETE🔴

`Models` ✅
- Define as estruturas dos dados e suas interações com o banco de dados.
- - DTO - Camada de transferência de dados (Data Transfer Object), usada para transportar informações entre camadas.
- - DAO - Camada de acesso a dados (Data Access Object), responsável por interagir diretamente com o banco de dados.

`Repository` ✅
- Abstrai o acesso aos dados, fornecendo uma interface para interagir com o banco de dados sem expor sua implementação, facilitando o teste e a manutenção do código.

`Service` ✅
-  orquestrar as operações, utilizando os Repositories e outras dependências para realizar ações específicas, como validações e transformações de dados.

`Test` ✅ 
la contém testes automatizados para verificar o comportamento das camadas de Service, Repository, e outras partes do sistema, garantindo que as funcionalidades estejam corretas e que futuras mudanças não quebrem o sistema.


### Diretório 🗂️
```plaintext
📦 minha_api
 ┣ 📂 controller    # Controladores das rotas
 ┣ 📂 models        # Definições dos modelos e entidades
 ┣ 📂 repository    # Comunicação com o banco de dados
 ┣ 📂 service       # Lógica de negócios
 ┣ 📂 test          # Testes automatizados
 ┣ 📜 .env          # Configurações do ambiente
 ┣ 📜 .gitignore    # Arquivos ignorados pelo Git
 ┣ 📜 Dockerfile    # Configuração para container Docker
 ┣ 📜 main.py       # Ponto de entrada da aplicação
 ┣ 📜 pytest.ini    # Configurações do Pytest
 ┗ 📜 requirements.txt  # Dependências do projeto
```



### 🔧 Configuração do Ambiente 
#### Instalando bibliotecas necessárias
- 💻 Crie um ambiente virtual
```bash
python -m venv {nome-da-sua-venv}
```

- ▶️ Ative o ambiente virtual
```bash
python -m venv {nome-da-sua-venv}
```

- 🏗️ Instalar todas as bibliotecas nessárias
```bash
venv\Scripts\activate
```

Antes de executar o projeto, configure as seguintes variáveis de ambiente no seu arquivo `.env` ou diretamente no sistema (toda conexão de banco de dados é feita aqui):

| Variável              | Descrição                                           | tipo        |
|-----------------------|-----------------------------------------------------|-------------|
| HOST                  | Define o endereço do servidor do banco de dados     |  str        |
| DATABASE              | Nome do banco de dados que a aplicação irá utiliza  |  str        |
| USER                  | Nome de usuário para autenticação no banco de dados |  str        |
| PASSWORD              | Senha do usuário para acessar o banco de dados      |  str        |



### 📂 Exemplo de arquivo `.env`
```plaintext
##################################################
### CONEXÃO BANCO DE DADOS
##################################################
HOST=
DATABASE=
USER=
PASSWORD=
```

#### ⚡ Para iniciar o servidor local python via prompt de comando basta rodar o comando a baixo na pasta raiz
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

#### ⚡Para acessar o Swagger
```bash
localhost/docs
```