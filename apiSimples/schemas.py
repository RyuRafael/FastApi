# schemas.py
# Modelos Pydantic para entrada/saída da API (validação e serialização)


from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

class CorridaBase(BaseModel):
     """Base de dados para criar/atualizar corridas."""
     nome: str = Field(min_length=3, max_length=150)
     cidade: str = Field(min_length=2, max_length=100)
     distancia_km: float = Field(gt=0, description="Distância em km, deve ser > 0")
     data_hora: datetime
     organizador: str | None = Field(default=None, max_length=120)
    

class CorridaCreate(CorridaBase):
     """Payload pra criação de corridas"""
     pass

class CorridaUpdate(BaseModel):
     """Payload para atualização parcial/total de corrida.
    Todos os campos são opcionais para permitir atualizações parciais (PUT completo ou PATCH style)."""

     nome: str | None = Field(default=None, min_length=3, max_length=150)
     cidade: str | None = Field(default=None, min_length=2, max_length=100)
     distancia_km: float | None = Field(default=None, gt=0)
     data_hora: datetime | None = None
     organizador: str | None = Field(default=None, max_length=120)

class CorridaOut(BaseModel):
     """Resposta enviada ao cliente"""

     model_config = ConfigDict(from_attributes=True)

     id: int
     nome: str
     cidade: str
     distancia_km: float
     data_hora: datetime
     organizador: str | None
     created_at: datetime | None


#Participantes

class ParticipantesBase(BaseModel):
     nome: str = Field(min_length=3, max_length=150)
     idade: int = Field(min_length= 18, max_length=60)

class ParticipanteCreate(ParticipantesBase):
     pass

class ParticipantesUpdate(BaseModel):
     nome: str = Field(default=None, min_length=3, max_length=150)
     idade: int = Field(default=None, min_length=18, max_length=60)


class ParticipantesOut(BaseModel):
     id: int
     nome: str
     idade: int
