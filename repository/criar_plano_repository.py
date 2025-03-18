from models.dao.dao_plano import TABELA as _tabela_plano
from models.dao.utils.sql_insert import executar_insert
from models.dao.database import CONEXAO as _c


def criar_plano_repository(dados: dict):
    try:
        with _c.cursor() as cursor:
            executar_insert(cursor, _tabela_plano, dados)
            _c.commit()
            return {"id": dados.get("id")}  # Retorna o ID gerado na inserção
    except Exception as e:
        _c.rollback()
        raise Exception(f"Erro ao inserir contratação: {e}")
