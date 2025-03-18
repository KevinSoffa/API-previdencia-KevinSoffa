from models.dto.criar_cliente_dto import ClienteDTO
from repository import criar_cliente_repository
from datetime import datetime as dt
from fastapi import HTTPException
from uuid import uuid4


def criar_cliente_service(criar_cliente_dto: ClienteDTO):
    # Convertendo DTO em dict
    dados = criar_cliente_dto.__dict__

    now = str(dt.now())

    # Atualizando dados de datas
    dados.update({
        'id': str(uuid4()),
        'criado_em': now,
        'atualizado_em': now
    })

    try:
        # Chamando o repositório
        response = criar_cliente_repository(dados)

        if "id" in response:
            return {"id": response["id"]}
        
        # Se houver erro
        raise HTTPException(status_code=500, detail="Falha ao criar o cliente")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")
