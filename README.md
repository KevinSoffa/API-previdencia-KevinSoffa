# 📌API PLANO DE PREVIDÊNCIA

<div align="center">
  <img height="180em" src="https://raw.githubusercontent.com/KevinSoffa/API-previdencia-KevinSoffa/refs/heads/develop/img/Kevin%20Soffa%20(2).png"/>
</div>


## Sumário 🔄

1. [Descrição](#descrição-)
2. [Tecnologias](#tecnologias)
3. [Desenvolvimento](#desenvolvimento-)
4. [Configuração do Ambiente](#configuração-do-ambiente)
5. [Modo de Uso](#modo-de-uso)
6. [Testes automatizados](#testes-automatizados)

---
## Descrição 📝
Esta é uma API desenvolvida em Python utilizando FastAPI, seguindo a arquitetura MVC (Model-View-Controller). A API conta com testes automatizados para garantir qualidade e confiabilidade, além de utilizar PostgreSQL como banco de dados. Que simula o back-end de uma consultoria de vendas de planos de previdência

## Tecnologias
<div align="left">
    <img src="https://skillicons.dev/icons?i=py" height="40" alt="python logo"/>
    <img src="https://skillicons.dev/icons?i=fastapi" height="40" alt="fastapi logo"/>
    <img src="https://skillicons.dev/icons?i=postgres" height="40" alt="postgresql logo"/>
    <img src="data:image/png;base64,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" height="40" alt="postgresql logo"/>
</div>

## Desenvolvimento 👨‍💻
`Controller` ✅
- Gerenciar as requisições `HTTP`
-  🟢**GET**
-  🔵**POST**
-  🟠**PATCH**
-  🔴**DELETE**

`Models` ✅
- Define as estruturas dos dados e suas interações com o banco de dados.
- - **DTO** - Camada de transferência de dados (Data Transfer Object), usada para transportar informações entre camadas.
- - **DAO** - Camada de acesso a dados (Data Access Object), responsável por interagir diretamente com o banco de dados.

`Repository` ✅
- Abstrai o acesso aos dados, fornecendo uma interface para interagir com o banco de dados sem expor sua implementação, facilitando o teste e a manutenção do código.

`Service` ✅
-  Orquestrar as operações, utilizando os Repositories e outras dependências para realizar ações específicas, como validações e transformações de dados.

`Test` ✅ 
Testes automatizados para verificar o comportamento das camadas de Service, Repository, e outras partes do sistema, garantindo que as funcionalidades estejam corretas e que futuras mudanças não quebrem o sistema.

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
{nome-da-sua-venv}\Scripts\activate
```

- 🏗️ Instalar todas as bibliotecas nessárias
```bash
pip install -r requirements
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

## Modo de Uso 🔄
### Criar Cliente
POST 🔵
 ```bash
/kevinsoffa/criar/cliente
```
JSON EXEMPLO ⬆️
 ```bash
{
  "cpf": "84292249629",
  "nome": "string",
  "email": "user@example.com",
  "datadenascimento": "2025-03-18",
  "genero": "string",
  "rendamensal": 1
}
```
RESPOSTA ⬇️
```bash
HTTP 201
{
 "id": "123e4567-e89b-12d3-a456-426614174000"
 }
```
***
### Criar Produto
POST 🔵
 ```bash
/kevinsoffa/criar/produto
```
JSON EXEMPLO ⬆️
 ```bash
{
  "cpf": "84292249629",
  "nome": "string",
  "email": "user@example.com",
  "datadenascimento": "2025-03-18",
  "genero": "string",
  "rendamensal": 1
}
```
RESPOSTA ⬇️
```bash
HTTP 201
{
 "id": "123e4567-e89b-12d3-a456-426614174000"
 }
```
***
### Criar Plano
POST 🔵
 ```bash
/kevinsoffa/criar/plano
```
JSON EXEMPLO ⬆️
 ```bash
{
  "idcliente": "string",
  "idproduto": "string",
  "aporte": 0,
  "datadacontratacao": "2025-03-18",
  "idadedeaposentadoria": 0
}
```
RESPOSTA ⬇️
```bash
HTTP 201
{
 "id": "123e4567-e89b-12d3-a456-426614174000"
 }
```
***
### Consultar Cliente
GET🟢
 ```bash
/kevinsoffa/consultar/cliente/{id_cliente}
```
UUID EXEMPLO ⬆️
 ```bash
{
    "id": "123e4567-e89b-12d3-a456-426614174000"
}
```
RESPOSTA ⬇️
```bash
HTTP 200
{
  "cliente": {
    "id": "c2320aa3-c5b3-4c06-9019-8b1f71105426",
    "cpf": "45645645600",
    "nome": "Kevin Soffa",
    "email": "kevin@cliente.com",
    "datadenascimento": "2010-08-24",
    "genero": "Masculino",
    "rendamensal": 2899.5,
    "criado_em": "2024-11-09T22:58:41.206614",
    "atualizado_em": "2024-11-09T22:58:41.206614"
  }
}
```
***
### Atualizar Cliente
PATCH🟠
 ```bash
/kevinsoffa/atualizar/cliente/{id_cliente}
```
UUID EXEMPLO ⬆️
 ```bash
{
    "id": "123e4567-e89b-12d3-a456-426614174000"
}
```
JSON
```bash
{
  "nome": "string",
  "email": "user@example.com",
  "datadenascimento": "2025-03-19",
  "genero": "string",
  "rendamensal": 0
}
```
RESPOSTA ⬇️
```bash
HTTP 200
{
  "cliente": {
    "id": "c2320aa3-c5b3-4c06-9019-8b1f71105426",
    "cpf": "45645645600",
    "nome": "Kevin Soffa",
    "email": "kevin@cliente.com",
    "datadenascimento": "2010-08-24",
    "genero": "Masculino",
    "rendamensal": 2899.5,
    "criado_em": "2024-11-09T22:58:41.206614",
    "atualizado_em": "2024-11-09T22:58:41.206614"
  }
}
```
### Apagar Cliente
DELETE🔴
 ```bash
/kevinsoffa/excluir/cliente/{id_cliente}
```
UUID EXEMPLO ⬆️
 ```bash
{
    "id": "123e4567-e89b-12d3-a456-426614174000"
}
```
RESPOSTA ⬇️
```bash
HTTP 200
{
  "message": "Cliente e planos excluídos com sucesso",
  "planos_excluidos": 0
}
```

## Testes Automatizados 🧪
### teste 1 ⏩
 ```bash
pytest test/test_consultar_cliente_service.py -v
```