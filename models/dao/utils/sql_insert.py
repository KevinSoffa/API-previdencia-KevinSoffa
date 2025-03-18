def executar_insert(cursor, tabela, dados):
    """
    Executa um insert
    """
    colunas = ', '.join(dados.keys())
    valores = ', '.join(['%s'] * len(dados))
    query = f"INSERT INTO {tabela} ({colunas}) VALUES ({valores})"

    # Executando a query
    cursor.execute(query, tuple(dados.values()))
