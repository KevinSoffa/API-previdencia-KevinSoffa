from models.dao.utils.sql_select import executar_select
from models.dao.dao_cliente import TABELA as _tabela_cliente
from models.dao.database import CONEXAO as _c
import uuid

def consultar_cliente_repository(id_cliente: str):
    try:
        id_cliente = str(uuid.UUID(id_cliente))

        with _c.cursor() as cursor:
            where_clause = "id = %s"
            resultados = executar_select(cursor, _tabela_cliente, colunas=["*"], where=where_clause, params=(id_cliente,))

            if not resultados:
                return None  # Cliente não encontrado
            return resultados[0]

    except Exception as e:
        _c.rollback()  # **Importante: reseta a transação para evitar bloqueios**
        raise Exception(f"Erro ao consultar cliente: {e}")
