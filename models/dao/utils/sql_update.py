from typing import Dict, Optional

def executar_update(cursor, tabela: str, valores: Dict[str, any], where: str, params: Optional[tuple] = None):
    if not valores:
        raise ValueError("Nenhum valor foi passado para atualização.")
    
    # Construção da cláusula SET
    set_clause = ', '.join(f"{coluna} = %s" for coluna in valores.keys())
    
    # Montagem da query SQL com o WHERE obrigatório
    query = f"UPDATE {tabela} SET {set_clause} WHERE {where}"
    
    # Parâmetros para a query (valores dos campos + parâmetros adicionais)
    valores_tuple = tuple(valores.values())
    parametros_finais = valores_tuple + (params if params else ())

    # Teste: Printando a query e os parâmetros antes de executar
    print("QUERY GERADA:", query)
    print("PARAMETROS:", parametros_finais)

    cursor.execute(query, parametros_finais)  # Executa a query
    return cursor.rowcount  # Retorna o número de registros atualizados