from models.dao.utils.sql_select import executar_select
from models.dao.dao_plano import TABELA as _tabela_plano
from models.dao.database import CONEXAO as _c
import uuid


def consultar_plano_repository(id_plano: str):
    try:
        id_plano = str(uuid.UUID(id_plano))

        with _c.cursor() as cursor:
            where_clause = "id = %s"
            resultados = executar_select(
                cursor,
                _tabela_plano,
                colunas=["*"],
                where=where_clause,
                params=(id_plano,)
            )
            
            if not resultados:
                return None
            return resultados[0]
    
    except Exception as e:
        _c.rollback()
        raise Exception(f'Erro ao consultar plano: {e}')
