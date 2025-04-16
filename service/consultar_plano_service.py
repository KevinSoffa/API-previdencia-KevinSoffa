from .consultar_cliente_service import consultar_cliente_service
from repository import consultar_plano_repository


def consultar_plano_service(id_plano: str):

    if not id_plano:
        raise ValueError("O ID do plano não pode ser vazio")
    
    plano = consultar_plano_repository(id_plano)
    id_cliente = plano["idcliente"]
    cliente = consultar_cliente_service(id_cliente)
    
    nome_cliente = cliente.get('nome')

    plano["nome_cliente"] = nome_cliente


    if not plano:
        raise ValueError("Plano não encontrado")
    
    return plano