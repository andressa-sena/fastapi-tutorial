from enum import StrEnum
from fastapi import FastAPI

class NomeCor(StrEnum):
    amarelo = "amarelo"
    azul = "azul"
    vermelho = "vermelho"

app = FastAPI()

fake_items_db = [{"item_name": "Goku"}, {"item_name": "Naruto"}, {"item_name": "Frieren"}]

# Um "path" também é comumente chamado de "endpoint" ou de "rota"
@app.get("/")
def root():
    return {"mensagem": "Olá Mundo"}

@app.get("/toca_raul")
def toca_raul():
    return {"música": "Quem não tem colírio usa óculos escuros..."}

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

# Parametros de Consulta
@app.get("/items/")
def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]

# Parametros opcionais
@app.get("/items/{item_id}")
def read_item2(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}