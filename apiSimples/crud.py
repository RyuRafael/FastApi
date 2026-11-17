# crud.py
# Funções de acesso ao banco para o recurso Corrida


from sqlalchemy.orm import Session  
from models import Corrida
from schemas import CorridaCreate, CorridaUpdate

def list_corrida(db: Session, skip: int = 0, limit: int = 50, cidade: str | None = None):
    """Lista de corridas simples e filtro de cidade opcional"""

    query = db.query(Corrida)

    if cidade:
        query = query.filter(Corrida.cidade.ilike(f"%{cidade}%"))

    return query.offset(skip).limit(limit).all()

def get_corrida(db: Session, corrida_id: int):
    """Buscar corrida por id"""

    query = db.query(Corrida).filter(Corrida.id == corrida_id).first()

    return query

def create_corrida(db: Session, payload: CorridaCreate):
    """Criar nova corrida apartir do payload"""

    corrida = Corrida(**payload.model_dump())

    db.add(corrida)
    db.commit()
    db.refresh(corrida)
    return corrida

def update_corrida(db: Session, corrida: Corrida, payload: CorridaUpdate):
    """Atualiza campos fornecidos no payload."""

    for field, value in payload.model_dump(exclude_unset=True).items:
        setattr(corrida, field, value)

    db.commit
    db.refresh(corrida)
    return corrida

def delete_corrida(db: Session, corrida: Corrida):
    db.delete(corrida)
    db.commit
    
