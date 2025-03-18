from models.dto.criar_produto_dto import ProdutoDTO
from repository import criar_produto_repository
from fastapi import HTTPException
from uuid import uuid4


def criar_produto_service(criar_produto_dto: ProdutoDTO):
    dados = criar_produto_dto.__dict__

    dados.update({
        'id': str(uuid4()) # gerando UUID 
    })

    try:
        response = criar_produto_repository(dados)

        if "id" in response:
            return {"id": response["id"]}
        
        raise HTTPException(status_code=500, detail="Falha ao criar o produto")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")
    