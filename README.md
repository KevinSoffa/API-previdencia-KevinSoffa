# 📌API PLANO DE PREVIDÊNCIA

<div align="center">
  <img height="180em" src="https://raw.githubusercontent.com/KevinSoffa/API-previdencia-KevinSoffa/refs/heads/develop/img/Kevin%20Soffa%20(2).png"/>
</div>


## Sumário 🔄

## Sumário 🔄

1. [Descrição](#descrição)
2. [Tecnologias](#tecnologias)
3. [Desenvolvimento](#desenvolvimento)
4. [Configuração do Ambiente](#configuração-do-ambiente)
5. [Modo de Uso](#modo-de-uso)
6. [Testes Automatizados](#testes-automatizados)

---
## Descrição 📝
Esta é uma API desenvolvida em Python utilizando FastAPI, seguindo a arquitetura MVC (Model-View-Controller). A API conta com testes automatizados para garantir qualidade e confiabilidade, além de utilizar PostgreSQL como banco de dados. Que simula o back-end de uma consultoria de vendas de planos de previdência

## Tecnologias
<div align="left">
    <img src="https://skillicons.dev/icons?i=py" height="40" alt="python logo"/>
    <img src="https://skillicons.dev/icons?i=fastapi" height="40" alt="fastapi logo"/>
    <img src="https://skillicons.dev/icons?i=postgres" height="40" alt="postgresql logo"/>
    <img src="https://raw.githubusercontent.com/KevinSoffa/API-previdencia-KevinSoffa/refs/heads/develop/img/pytestlogo.jpg" height="40" alt="postgresql logo"/>
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
 ┣ 📂 controller
 ┣ 📂 models
 ┣ 📂 k8s 
 ┣ 📂 repository
 ┣ 📂 service
 ┣ 📂 test 
 ┣ 📜 .env
 ┣ 📜 .gitignore
 ┣ 📜 Dockerfile
 ┣ 📜 main.py
 ┣ 📜 pytest.ini
 ┗ 📜 requirements.txt

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
### teste 1 [ Consultar Cliente - Service ] ⏩
 ```bash
pytest test/test_consultar_cliente_service.py -v
```
### teste 2 [ Consultar Plano - Service ] ⏩
 ```bash
pytest test/test_consultar_plano_service.py -v
```

## 🚢 Kubernetes [ Deploy ]
### 🚀 Deploy da aplicação FastAPI no Kubernetes
 Kubernetes para rodar e expor a API FastAPI.

### 📦 Deployment (`deployment.yaml`)

O `Deployment` define como a aplicação será executada no cluster:

- **Replicas**: 2 pods da aplicação serão criados.
- **Container**: Usa a imagem `meu-usuario/minha-api:latest`.
- **Porta interna**: A aplicação roda na porta `8000`.
- **Variáveis de ambiente**: Carregadas de um `ConfigMap` chamado `fastapi-config`.

### 🚀 Deploy do PostgreSQL no Kubernetes
Kubernetes para rodar o PostgreSQL como um contêiner no cluster.

### 📦 Deployment do PostgreSQL (`postgres-deployment.yaml`)

O `Deployment` do PostgreSQL cria um pod que executa o banco de dados, configurando as variáveis de ambiente necessárias para o banco.

- **Replicas**: 1 pod do PostgreSQL.
- **Imagem**: Usa a imagem oficial `postgres:14`.
- **Variáveis de ambiente**: Configurações do PostgreSQL (usuário, senha e nome do banco).
- **Porta interna**: O PostgreSQL expõe a porta `5432`.

## 🐳 Docker 
Este repositório contém uma aplicação FastAPI empacotada em um contêiner Docker. A aplicação foi criada utilizando o Python 3.11 e o servidor ASGI Uvicorn.

### Pré-requisitos
- Docker instalado na sua máquina.
- A aplicação foi construída com FastAPI, portanto, é necessário ter um arquivo `requirements.txt` contendo todas as dependências do Python.
