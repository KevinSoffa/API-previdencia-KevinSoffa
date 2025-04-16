from service.consultar_plano_service import consultar_plano_service
import pytest
import uuid


def test_consultar_plano_service_retornar_dados(mocker):
    # Arrange
    id_plano = str(uuid.uuid4())
    id_cliente = str(uuid.uuid4())

    mock_plano = {
        "id": id_plano,
        "idcliente": id_cliente,
        "idproduto": str(uuid.uuid4()),
        "aporte": 5000,
        "datadacontratacao": "2024-11-11",
        "idadedeaposentadoria": 55
    }

    mock_cliente = {
        "id": id_cliente,
        "nome": "Fernanda Soffa Pontes"
    }

    # Mocks
    mocker.patch('service.consultar_plano_service.consultar_plano_repository', return_value=mock_plano.copy())
    mocker.patch('service.consultar_plano_service.consultar_cliente_service', return_value=mock_cliente)

    # Act
    result = consultar_plano_service(id_plano)

    # Assert
    assert result["id"] == id_plano
    assert result["idcliente"] == id_cliente
    assert result["aporte"] == 5000
    assert result["datadacontratacao"] == "2024-11-11"
    assert result["idadedeaposentadoria"] == 55
    assert result["nome_cliente"] == "Fernanda Soffa Pontes"


def test_consultar_plano_service_id_vazio():
    with pytest.raises(ValueError, match="O ID do plano não pode ser vazio"):
        consultar_plano_service("")
