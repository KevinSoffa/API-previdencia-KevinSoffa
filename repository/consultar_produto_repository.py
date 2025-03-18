from models.dao.utils.sql_select import executar_select
from models.dao.dao_produto import TABELA as _tabela_produto
from models.dao.database import CONEXAO as _c


def consultar_produto_repository(id_produto: str):
    try:
        with _c.cursor() as cursor:
            where_clause = "id = %s"
            resultados = executar_select(cursor, _tabela_produto, colunas=["*"], where=where_clause, params=(id_produto,))
            if not resultados:
                return None  # Produto não encontrado
            return resultados[0]

    except Exception as e:
        raise Exception(f"Erro ao consultar produto: {e}")
