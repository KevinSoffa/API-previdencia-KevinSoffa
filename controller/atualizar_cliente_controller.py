from service import atualizar_cliente_service
from models.dto import AtualizarClienteDTO
from .router import router
from fastapi import status
from uuid import UUID


@router.patch('/atualizar/cliente/{id_cliente}', status_code=status.HTTP_200_OK)
def atualizar_cliente_controller(id: UUID, atualizar_dto: AtualizarClienteDTO):
    return atualizar_cliente_service(id, atualizar_dto)