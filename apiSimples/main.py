# API teste 01
#Frameworks: fastapi e uvecorn(servidor)
#Compilar a API: uvicorn main:app --reload

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="API de teste",
              version="1.0.0",
              description="API simples para ilustrar os conseitos basicos do Rest")


@app.get("/")
def boas_vindas():
    return {"mensagem: " "Bem-vindo(a) á aula de API 02"}

# ROTA 02: SAUDAÇÃO PERSONALIZADA
#-----------------------------------
# Aqui criamos uma rota que recebe um parâmetro chamado nome:

@app.get("/saudacao/{nome}")
def saudacao(nome: str):
    return {"Mensagem: " f"{nome}! é um prazer em te conhecer"}

#--------------Terceira execução

@app.get("/corridas", response_model=List[Corrida], summary = "Listar corridas" )
def listar_corridas():
    return corridas_db

@app.post(
    "/corridas",
    status_code=201,
    summary="Cria uma nova corrida"
)
def criar_corrida(dados: Corrida_Create):
    global proximo_id 

    # Requisição do que queremos que faça aqui dentro
    preco_final = dados.preco if dados.preco is not None else calcular_preco(dados.distancia_km)


nova_corrida = Corrida(
    id = proximo id,
    passageiro = dados.passageiro,
    motorista = dados.passageiro,
    origen = dados.origen,
    destino = dados.destino,
    distancia = dados.distancia_km,
    preco = preco_final,
    status = "solicitada",
    criado_em = datetime.utcnow()

)


    corridas_db.append(nova_corrida):
    proximo_id +=1
    return nova_corrida






