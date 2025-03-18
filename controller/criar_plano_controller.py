from models.dto.criar_plano_dto import PlanoDTO
from service import criar_plano_service
from .router import router
from fastapi import status


@router.post('/criar/plano', status_code=status.HTTP_201_CREATED)
def criar_plano_controller(app_dto: PlanoDTO):
    return criar_plano_service(app_dto)

