# main.py
# Ponto de entrada da API: rotas REST para o recurso "corridas"

from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List

from models import Participante
from database import ENGINE, get_db, Base, SessionLocal
from schemas import CorridaCreate, CorridaUpdate, CorridaOut, ParticipantesUpdate, ParticipanteCreate, ParticipantesOut
import crud

# Autenticação
"""from fastapi.security import OAuth2PasswordRequestForm
from auth import (
    authenticate_user,
    create_access_token,
    get_current_user,
    ACCESS_TOKEN_EXPIRE_MINUTE,
    TokenData
)"""

# Inicializar tabelas do banco (create_all só cria se não existir)
Base.metadata.create_all(bind=ENGINE)

app = FastAPI(
    title="API corrida",
    description="API REST para gerenciamento de corridas com FASTAPI E SQLAllchemy",
    version="1.0"
)

app.get("/health", summary="Verificar saúde da API")
def healthcheck():
    """HealthCheck simple para verifacar se a API está de pé"""

    return {"Status": "ok"}

@app.get(
    "/corridas",
    response_model=List[CorridaOut],
    summary="Lista de corridas",
    tags=["corridas"]
    )
def listar_corridas(
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0, description="Número de registros a pular"),
    limit: int = Query(50, ge=1, le=200, description="Máximo de registros a retornar"),
    cidade: str | None = Query(None, description="Filtro por cidade")
    ):
    """Retornar lista de corridas (filtro opcional para cidades)"""
    results = crud.list_corrida(db, skip=skip, limit=limit, cidade=cidade)
    return results


@app.get("/corridas/{corrida_id}",
         response_model=CorridaOut,
         summary="Obter corrida por id",
         tags=["corridas"]
         )
def obter_corrida(corrida_id: int, db: Session = Depends(get_db)):
   """Retornar uma corrida por id. se não existir erro 404"""
   corrida = crud.get_corrida(db, corrida_id)

   if not corrida:
       raise HTTPException(status_code=404, detail="Corrida não encontrada")
   return corrida

@app.post("/corridas",
          response_model=CorridaOut,
          status_code=201,
          summary="Criar corrida",
          tags=["corridas"]
          )
def criar_corrida(payload: CorridaCreate, db: Session = Depends(get_db)):
    """Criar uma nova corrida"""

    corrida = crud.create_corrida(db, payload )
    return corrida

@app.put("/corridas",
        response_model=CorridaOut,
        summary="Atualizar corrida",
        tags=["corridas"]
        )
def atualizar_corrida(corrida_id: int, payload: CorridaUpdate, db: Session = Depends(get_db)):
    "Atualizar corrida existente"

    corrida = crud.get_corrida(db, corrida_id)

    if not corrida:
        raise HTTPException(status_code=404, detail="Corrida não encontrada")

    corrida = crud.update_corrida(db, corrida, payload)
    return corrida

@app.delete("/corridas/{corrida_id}",
           response_model=CorridaOut,
           status_code=201,
           summary="Deletar corrida",
           tags=["corridas"]
           )
def deletar_corrida(corrida_id: int, db: Session = Depends(get_db)):

    corrida = crud.get_corrida(db, corrida_id)

    if not corrida:
        raise HTTPException(status_code=404, detail="Corrida não encontrada")
    
    corrida = crud.delete_corrida(db, corrida)
    return corrida  

@app.get(
        "/participantes",
         response_model=List[ParticipantesOut],
         summary="Listar Participantes",
         tags=["participantes"])
def list_participantes(
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0, description="Número de registroa a pular"),
    limit: int = Query(50, ge=1, le=200, description="Máximo de registro a retornar"),
    nome: str | None = Query(None)):

    result = crud.list_corrida(db,skip,limit,nome)
    return result

@app.get(
    "/participantes/{participante_id}",
    response_model=ParticipantesOut,
    summary="obter participante por id",
    tags=["participantes"])
def get_participante(id: int, db: Session = Depends(get_db)):

    result = crud.get_participante(db, id)
    return result

@app.put(
    "/participante/{paricipante_id}",
    response_model=ParticipantesOut,
    summary="Atualizar participante",
    tags=["participantes"])

def atualizar_participante(id: int, payload: ParticipantesUpdate, db: Session = Depends(get_db)):
    "Atualizar corrida existente"

    participante = crud.get_participante(db, id)

    if not participante:
        raise HTTPException(status_code=404, detail="Participante não encontrado")

    participante = crud.update_participante(db, participante, payload)
    return participante

@app.delete("/participante/{participante_id}",
           response_model=ParticipantesOut,
           status_code=201,
           summary="Deletar participante",
           tags=["participantes"]
           )
def deletar_participante(id: int, db: Session = Depends(get_db)):

    participante = crud.get_participante(db, id)

    if not participante:
        raise HTTPException(status_code=404, detail="Participante não encontrada")
    
    participante = crud.delete_participante(db, participante)
    return participante  
