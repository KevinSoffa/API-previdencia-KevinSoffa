# service/contratacao_service.py
from repository import consultar_produto_repository
from repository import consultar_cliente_repository
from models.dto.criar_plano_dto import PlanoDTO
from repository import criar_plano_repository
from datetime import datetime, date
from fastapi import HTTPException
from uuid import uuid4


def validar_idade(data_nascimento: date):
    # Data atual
    data_atual = date.today()

    # Calcula a idade com base na diferença de anos
    idade = data_atual.year - data_nascimento.year

    # Ajusta a idade com mes e dia
    if (data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day):
        idade -= 1

    # Verifica se a idade está entre 18 e 60 anos
    if idade >= 18 and idade < 60:
        return idade # Idade válida
    else:
        return idade  # Idade inválida


def criar_plano_service(contratacao_dto: PlanoDTO):
    # Convertendo DTO em dict
    dados = contratacao_dto.dict()

    try:
        # Consultar produto
        produto = consultar_produto_repository(dados["idproduto"])
        
        if not produto:
            raise HTTPException(status_code=404, detail="Produto não encontrado")

        # Consultar cliente
        cliente = consultar_cliente_repository(dados["idcliente"])
        if not cliente:
            raise HTTPException(status_code=404, detail="Cliente não encontrado")

        # Regras de validade
        # 1. Verificar se o produto está com o prazo de venda expirado
        data_expiracao = produto["expiracaodevenda"]
        

        # Converte para um objeto date caso data_expiracao seja uma string
        if isinstance(data_expiracao, str):
            data_expiracao = datetime.strptime(data_expiracao, "%Y-%m-%d").date()

        # Verifica se a data de expiração já passou
        if data_expiracao < date.today():
            raise HTTPException(status_code=400, detail="Produto com prazo de venda expirado.")

        # 2. Verificar se o aporte é maior que o valor mínimo
        valor_minimo_aporte = produto["valorminimoaporteinicial"]
        if dados["aporte"] < valor_minimo_aporte:
            raise HTTPException(status_code=400, detail=f"O aporte deve ser maior que {valor_minimo_aporte}.")

        # 3. Verificar se a idade de aposentadoria está dentro da faixa permitida
        idade_cliente = validar_idade(cliente["datadenascimento"])
        if idade_cliente <= 18 or idade_cliente > 60:
            raise HTTPException(status_code=400, detail=f"O cliente tem {idade_cliente} anos de idade. A idade deve ser de 18 a 60 anos.")


        # 4. Verifica se a data de contratação é igual a data atual
        if dados["datadacontratacao"] != date.today():
            raise HTTPException(status_code=400, detail="Data de contratação diferente da data atual.")

        # Gerar ID da contratação
        dados["id"] = str(uuid4()) # Gerando UUID


        # Caso todas as validações passem, criamos a contratação
        contratacao = criar_plano_repository(dados)
        
        return contratacao  # Retorna o ID da contratação inserida

    except HTTPException as e:
        raise e 
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")
