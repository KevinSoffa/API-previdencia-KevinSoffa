from repository import consultar_cliente_repository


def consultar_cliente_service(id_cliente: str):

    if not id_cliente:
        raise ValueError("O ID do cliente não pode ser vazio")
    
    cliente = consultar_cliente_repository(id_cliente)

    if not cliente:
        raise ValueError("Cliente não encontrado")
    
    return cliente