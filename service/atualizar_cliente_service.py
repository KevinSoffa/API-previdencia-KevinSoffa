from models.dto.atualizar_cliente_dto import AtualizarClienteDTO
from repository import atualizar_cliente_repository
from fastapi import HTTPException
from uuid import UUID


def atualizar_cliente_service(id:UUID, atualizar_dto: AtualizarClienteDTO):
    dados = atualizar_dto.__dict__

    response = atualizar_cliente_repository(
        str(id),
        dados
    )

    if response is None:
        return HTTPException(500)
    
    if response:
        return response
    
    raise HTTPException(404)