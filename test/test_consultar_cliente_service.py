import pytest
from unittest.mock import patch
from service.consultar_cliente_service import consultar_cliente_service

def test_consultar_cliente_service_id_vazio():
    """Deve lançar um ValueError quando o ID do cliente for vazio"""
    with pytest.raises(ValueError, match="O ID do cliente não pode ser vazio"):
        consultar_cliente_service("")

@patch("service.consultar_cliente_service.consultar_cliente_repository")
def test_consultar_cliente_service_cliente_nao_encontrado(mock_repository):
    """Deve lançar um ValueError quando o cliente não for encontrado"""
    mock_repository.return_value = None  # Mockando a resposta como None
    with pytest.raises(ValueError, match="Cliente não encontrado"):
        consultar_cliente_service("123")

@patch("service.consultar_cliente_service.consultar_cliente_repository")
def test_consultar_cliente_service_sucesso(mock_repository):
    """Deve retornar o cliente corretamente quando encontrado"""
    mock_repository.return_value = {"id": "123", "nome": "Cliente Teste"}  # Mockando um cliente válido
    resultado = consultar_cliente_service("123")
    assert resultado == {"id": "123", "nome": "Cliente Teste"}
