from models.dto.criar_produto_dto import ProdutoDTO
from service import criar_produto_service
from .router import router
from fastapi import status


@router.post('/criar/produto', status_code=status.HTTP_201_CREATED)
def criar_produto_controller(app_dto: ProdutoDTO):
    return criar_produto_service(app_dto)
