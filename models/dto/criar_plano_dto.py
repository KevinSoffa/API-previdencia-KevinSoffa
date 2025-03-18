from pydantic import Field, EmailStr, validator, BaseModel
from pydantic.dataclasses import dataclass
from datetime import date
from uuid import UUID


class PlanoDTO(BaseModel):
    idcliente: str = Field(...)
    idproduto: str = Field(...)
    aporte: float = Field(...)
    datadacontratacao: date = Field(...)
    idadedeaposentadoria: int = Field(...)

