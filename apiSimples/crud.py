# crud.py
# Funções de acesso ao banco para o recurso Corrida


from sqlalchemy.orm import Session  
from models import Corrida, Participante
from schemas import CorridaCreate, CorridaUpdate, ParticipanteCreate, ParticipantesUpdate

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

#Participantes

def list_participantes(db: Session, skip: int = 0, limit: int = 50, nome: str | None = None):

    query = db.query(Participante)

    if nome:
        query = query.filter(Participante.nome.ilike(f"%{nome}%"))

    return query.offset(skip).limit(limit).all()

def get_participante(db: Session, id: int):

    query = db.query(Participante).filter(Participante.id == id).first()

    return query

def create_participante(db: Session, payload: ParticipanteCreate):

    participante = Participante(**payload.model_dump)

    db.add(participante)
    db.commit
    db.refresh

    return participante

def update_participante(db: Session, participante: Participante, payload: ParticipantesUpdate):

    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(participante, field, value)

        db.commit
        db.refresh
        return participante


def delete_participante(db: Session, participante: Participante):
    db.delete(participante)
    db.commit
    db.refresh





    
