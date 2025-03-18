from typing import Optional


def executar_delete(cursor, tabela: str, where: str, params: tuple) -> Optional[str]:
     """
        Executa um DELETE na tabela fornecida, baseado na condição WHERE.

        :param cursor: O cursor do banco de dados.
        :param tabela: Nome da tabela onde será feita a exclusão.
        :param where: Condição para deletar (ex: "id = %s").
        :param params: Parâmetros para a cláusula WHERE.
        
        :return: O ID do registro excluído ou None se não encontrado.
     """
     query = f"DELETE FROM {tabela} WHERE {where} RETURNING id;"
     cursor.execute(query, params)
     resultado = cursor.fetchone()
     return resultado[0] if resultado else None
