from pydantic import Field, validator
from pydantic.dataclasses import dataclass
from datetime import date
from uuid import UUID


@dataclass
class ProdutoDTO:
    nome: str = Field(..., max_length=100)
    susep: str = Field(..., max_length=20)
    expiracaodevenda: date = Field(...)
    valorminimoaporteinicial: float = Field(...)
    valorminimoaporteextra: float = Field(...)
    idadedeentrada: int = Field(..., gt=0)
    idadedesaida: int = Field(..., gt=0)

##################################
### Validando inputs
##################################

    @validator('susep')
    def validar_susep(cls, v):
        """
        Valida o código SUSEP para garantir que tenha 20 dígitos numéricos.
        """
        if len(v) != 20 or not v.isdigit():
            raise ValueError("SUSEP deve ter exatamente 20 dígitos numéricos.")
        return v
    
    @validator('expiracaodevenda')
    def validar_expiracao(cls, v):
        """
        Valida a data de expiração da venda para garantir que não seja anterior à data atual.
        """
        if v < date.today():
            raise ValueError("A data de expiração da venda não pode ser anterior à data atual.")
        return v

    @validator('valorminimoaporteinicial')
    def validar_valores_inicial(cls, v):
        """
        Valida que os valores de aporte inicial sejam maiores que 1000.
        """
        if v <= 999:
            raise ValueError("Valor mínimo de aporte inicial deve ser maior que 1000.")
        return v
    
    @validator('valorminimoaporteextra')
    def validar_valores_extra(cls, v):
        """
        Valida que os valores de aporte extra sejam maiores que 100.
        """
        if v <= 99:
            raise ValueError("Valor mínimo de aporte extra deve ser maior que 100.")
        return v

    @validator('idadedeentrada')
    def validar_idade_entrada(cls, v):
        """
        Valida a idade mínima de entrada para garantir que seja maior que zero e sensata.
        """
        if v < 18:
            raise ValueError("A idade mínima para entrada deve ser 18 anos ou mais.")
        return v

    @validator('idadedesaida')
    def validar_idade_saida(cls, v, values):
        """
        Valida a idade máxima de saída, garantindo que seja no máximo 60 anos e maior que a idade mínima de entrada.
        """
        idade_entrada = values.get('idadedeentrada')
        if idade_entrada is not None:
            if v <= idade_entrada:
                raise ValueError("A idade máxima para saída deve ser maior que a idade mínima para entrada.")
        if v > 60:
            raise ValueError("A idade máxima para saída não pode ser superior a 60 anos.")
        return v
