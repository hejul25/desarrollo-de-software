from fastapi import FastAPI

app=FastAPI()

@app.get('/')
def mensaje():
    return "bienvenido a fastAPI ingenieros de sistemas y computacion"

@app.get('/{nombre}/{codigo}')
def mensaje2 (nombre:str,codigo:int):
    return f"Bienvenido {nombre} su codigo es {codigo}"

@app .get('/uno/')
def mesaje3 (edad:int,nombre:str):
    return f"{nombre} su edad es {edad}"

