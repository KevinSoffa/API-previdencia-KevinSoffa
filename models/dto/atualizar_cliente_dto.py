from pydantic.dataclasses import dataclass
from uuid import UUID
from datetime import date, datetime
from pydantic import (Field, validator, EmailStr)


@dataclass
class AtualizarClienteDTO:
    nome: str = Field(None)
    email: EmailStr = Field(None)
    datadenascimento: date = Field(None)
    genero: str = Field(None)
    rendamensal: float = Field(None)

    @validator('nome', pre=True)
    def validar_nome(cls, v):
        if not isinstance(v, str) or len(v.strip()) == 0:
            raise ValueError('Nome Inválido!')
        return v
        
    @validator('datadenascimento', pre=True)
    def validar_data(cls, v):
        try:
            datetime.strptime(v, "%Y-%m-%d")  # Tenta converter a string para uma data válida
        except ValueError:
            raise ValueError('Data Inválida!')
        return v
        
    @validator('rendamensal', pre=True)
    def validar_rendamensal(cls, v):
        try:
            return float(v)  # Converte para float para garantir que seja um número válido
        except ValueError:
            raise ValueError("Valor inválido para renda mensal.")
