from pydantic import Field, EmailStr, validator
from pydantic.dataclasses import dataclass
from datetime import date


@dataclass
class ClienteDTO:
    cpf: str = Field(..., min_length=11, max_length=11, pattern=r'^\d{11}$')
    nome: str = Field(..., max_length=100)
    email: EmailStr = Field(...)
    datadenascimento: date = Field(...)
    genero: str = Field(..., max_length=10)
    rendamensal: float = Field(..., gt=0)

##################################
### Validando inputs
##################################
    @validator('cpf')
    def validar_cpf(cls, v):
        if len(v) != 11 or not v.isdigit():
            raise ValueError("CPF deve ter 11 dígitos numéricos.")
        return v
