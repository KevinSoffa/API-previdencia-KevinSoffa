from models.dao.utils.sql_update import executar_update
from models.dao.dao_cliente import TABELA as _tabela
from models.dao.database import CONEXAO as _c
from json import dumps
from sys import stdout
from uuid import UUID


def atualizar_cliente_repository(id: UUID, valores: dict):
    try:
        where_clause = "id = %s"
        params = (id,)  # Colocando o id em uma tupla para o parâmetro de WHERE
        
        with _c.cursor() as cursor:
            linhas_atualizadas = executar_update(
                cursor,
                _tabela,
                valores,
                where=where_clause, 
                params=params,
            )

            # Após o UPDATE, consulta o cliente para retornar os dados atualizados
            # Esse SELECT vai retornar os dados mais atualizados do cliente
            cursor.execute("SELECT * FROM cliente WHERE id = %s", (id,))
            consulta = cursor.fetchone()

            # Se não encontrar, retorna None
            if consulta is None:
                return None

            _c.commit()  # Comitando as alterações

            return consulta
        
    except Exception as e:
        _c.rollback()  # Desfazendo qualquer alteração em caso de erro

        stdout.write(
            'Erro ao atualizar o cliente ID: %s\nDados: %s\nERRO: %s\n' % (
                id,
                dumps(
                    valores,
                    indent=2,
                    default=str,
                ),
                e,
            )
        )
