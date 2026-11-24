from fastapi import FastAPI

app = FastAPI()

# Um "path" também é comumente chamado de "endpoint" ou de "rota"

@app.get("/")
def root():
    return {"mensagem": "Olá Mundo"}