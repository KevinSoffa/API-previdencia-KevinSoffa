from models.dao.database import CONEXAO as _c
from models.dao.utils.sql_delete import executar_delete
from models.dao.dao_cliente import TABELA as _tabela_cliente
from models.dao.dao_plano import TABELA as _tabela_plano
import uuid


def excluir_planos_repository(id_cliente: str) -> int:
    """
        Exclui todos os planos associados a um cliente.

        :param id_cliente: ID do cliente cujos planos serão excluídos.
        :return: Número de planos excluídos.
    """
    try:
        with _c.cursor() as cursor:
            query = f"DELETE FROM {_tabela_plano} WHERE idcliente = %s RETURNING id;"
            cursor.execute(query, (id_cliente,))
            resultados = cursor.fetchall()
            return len(resultados)
        
    except Exception as e:
        raise Exception(f'Erro ao Excluir planos do cliente: {e}')



def excluir_cliente_repository(id_cliente: str) -> bool:
    """
    Exclui um cliente pelo ID.

    :param id_cliente: ID do cliente a ser excluído.
    :return: True se o cliente foi excluído, False se não encontrado.
    """
    try:
        with _c.cursor() as cursor:
            query = f"DELETE FROM {_tabela_cliente} WHERE id = %s RETURNING id;"
            cursor.execute(query, (id_cliente,))
            resultado = cursor.fetchone()
            return resultado is not None  # Retorna True se o cliente foi encontrado e excluído
    except Exception as e:
        raise Exception(f"Erro ao excluir cliente: {e}")