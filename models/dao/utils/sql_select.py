from typing import List, Optional


def executar_select(cursor, tabela: str, colunas: List[str] = ['*'], where: Optional[str] = None, params: Optional[tuple] = None):
    """
    Executa um SELECT na tabela fornecida, com colunas e filtros opcionais.
    
    :param cursor: O cursor do banco de dados.
    :param tabela: Nome da tabela de onde será feita a consulta.
    :param colunas: Lista de colunas a serem selecionadas (padrão é '*' para todas).
    :param where: Filtro opcional para a consulta.
    
    :return: Lista de dicionários com os resultados da consulta.
    """
    colunas_str = ', '.join(colunas)  # Gera a string das colunas selecionadas
    query = f"SELECT {colunas_str} FROM {tabela}"

    # Adiciona a cláusula WHERE se for preciso
    if where:
        query += f" WHERE {where}"

    cursor.execute(query, params)  # Executa a consulta SELECT

    # Obtém os resultados diretamente, que já devem ser mapeados corretamente
    resultados = cursor.fetchall()

    #print(f"Resultados brutos: {resultados}")

    # Retorna os resultados diretamente se forem do tipo RealDictRow
    return resultados if resultados else []  # Retorna uma lista vazia se não houver resultados

