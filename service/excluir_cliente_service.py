from repository.excluir_cliente_repository import excluir_cliente_repository, excluir_planos_repository
from models.dao.database import CONEXAO as _c
import uuid


def excluir_cliente_service(id_cliente: str) -> dict:
    """
        Exclui um cliente e seus planos associados.

        :param id_cliente: UUID do cliente a ser excluído.
        :return: Dicionário com status da exclusão.
    """
    try:
        id_cliente = str(uuid.UUID(id_cliente))

        with _c:
            planos_excluido = excluir_planos_repository(id_cliente)
            cliente_excluido = excluir_cliente_repository(id_cliente)

        if not cliente_excluido:
            return {
                    "success": False,
                    "message": "Cliente não encontrado!"
                    }
        
        return {
            "success": True,
            "message": "Cliente e planos excluídos com sucesso",
            "planos_excluidos": planos_excluido
        }
    
    except Exception as e:
        raise Exception(f"Erro ao excluir cliente e planos: {e}")
