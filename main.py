from fastapi import FastAPI
from pydantic import BaseModel

class Produto(BaseModel):
    nome: str
    preco: float

db = {
    1: {
        "nome": "Pizza de calabresa",
        "preco": 59.90,
    },
    2: {
        "nome": "Lasanha",
        "preco": 9.90
    }
}

app = FastAPI()

#rota principal de apresentação
@app.get('/')
def Apresentacao():
    return {
        "message": "Bem vindo",
        "statusCode": 200
    }

@app.get("/{user}")
def OlaUsuario(user):
    return {
        "message": f"olá {user}!",
        "statusCode": 200
    }

@app.get("/produtos/")
def MostrarTodosProdutos():
    return db

@app.get("/produtos/{id}")
def BuscarUmProduto(id):
    try:
        return db[id]
    except Exception as err:
        return {
            "message": "Not Found",
            "erro": f"{err}",
            "statusCode": 404
        }

@app.post("/produtos/cadastrar/")
def CadastrarProduto(item: Produto):
    id = len(db) + 1
    db[id] = item
    return {
        "message": "item criado com sucesso!",
        "Produto": item,
        "statusCode": 200
    }


