# models.py
# Modelos de dados do domínio "corridas" usando SQLAlchemy ORM

from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy import func
from database import Base

class Corrida(Base):
    """
    Representa uma corrida:
    - nome: identificação da corrida (ex: Maratona de Curitiba)
    - cidade: localização
    - distancia_km: distância em quilômetros (ex: 42.195)
    - data_hora: data e hora previstas da largada
    - organizador: entidade ou pessoa responsável
    - created_at: timestamp de criação (preenchido pelo BD)
    """

    __tablename__ = "corridas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(150), nullable=False, index=True)
    cidade = Column(String(100), nullable=False, index=True)
    distancia_km = Column(Float, nullable=False)
    data_hora = Column(DateTime(timezone=True), nullable=False)
    organizador = Column(String(120), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())