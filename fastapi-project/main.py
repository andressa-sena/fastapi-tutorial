from enum import StrEnum
from fastapi import FastAPI

class NomeCor(StrEnum):
    amarelo = "amarelo"
    azul = "azul"
    vermelho = "vermelho"

app = FastAPI()

# Um "path" também é comumente chamado de "endpoint" ou de "rota"

@app.get("/")
def root():
    return {"mensagem": "Olá Mundo"}

# @app.get("/toca_raul")
# def toca_raul():
#     return {"música": "Quem não tem colírio usa óculos escuros..."}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/cores/{nome_cor}")
def get_cor(nome_cor: NomeCor):
    if nome_cor is NomeCor.amarelo:
        return {"nome_cor": nome_cor, "mensagem": "Amarelo"}
    
    if nome_cor.value == "azul":
        return {"nome_cor": nome_cor, "mensagem": "Azul"}
    
    return {"nome_cor": nome_cor, "mensagem": "Vermelho"}