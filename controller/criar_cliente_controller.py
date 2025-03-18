from models.dto.criar_cliente_dto import ClienteDTO
from service import criar_cliente_service
from .router import router
from fastapi import status


@router.post('/criar/cliente', status_code=status.HTTP_201_CREATED)
def criar_cliente_controller(app_dto: ClienteDTO):
    return criar_cliente_service(app_dto)