from models.dao.utils.sql_insert import executar_insert
from models.dao.dao_produto import TABELA as _tabela
from models.dao.database import CONEXAO as _c
from json import dumps
from sys import stdout


def criar_produto_repository(dados: dict):
    try:
        with _c.cursor() as cursor:
            executar_insert(
                cursor,
                _tabela,
                dados
            )

            _c.commit()

            return {"id": dados.get("id")} # retornando ID
        
    except Exception as e:
        _c.rollback()

        stdout.write(
            'Erro ao criar: %s\nERRO: %s\n' % (
                dumps(
                    dados,
                    indent=2,
                    default=str,
                ),
                e,
            )
        )
        return {"message": "Erro ao criar o cliente", "error": str(e)}
