from fastapi import FastAPI,Body

app=FastAPI()

productos = [
    
    {
        "codigo": 1,
        "nombre":"esfero",
        "valor":3500,
        "existenia":10
    }, 
    {
        "codigo": 2,
        "nombre":"cuaderno",
        "valor":5000,
        "existenia":15
    },
     {
        "codigo": 3,
        "nombre":"lapiz",
        "valor":200,
        "existenia":12
    },
]

@app.get('/')
def mensaje():
    return "bienvenido a fastAPI ingenieros de sistemas y computacion"

#@app.get('/{nombre}/{codigo}')
#def mensaje2 (nombre:str,codigo:int):
 #   return f"Bienvenido {nombre} su codigo es {codigo}"

@app .get('/uno/')
def mesaje3 (edad:int,nombre:str):
    return f"{nombre} su edad es {edad}"

@app .get('/productoa')
def ListaProductos():
    return productos

@app .get('/productos/{cod}')
def findProductos(cod:int):
    for prod in productos:
        if prod['codigo']==cod:
            return prod
        
@app .get('/productos/')
def findProductos2(nom:str):
    for prod in productos:
        if prod['nombre']==nom:
            return prod

@app.post('/productos')
def CreateProducto(cod:int,nom:str,val:float,exi:int):
    productos.append({
        'codigo': cod,
        'nombre': nom,
        'valor' : val,
        'existencia': exi,
    })
    return productos

@app.post('/productos2')
def CreateProducto2(
    cod:int=Body(),
    nom:str=Body(),
    val:float=Body(),
    exi:int=Body()):
    productos.append({
        'codigo': cod,
        'nombre': nom,
        'valor' : val,
        'existencia': exi,
    })
    return productos

@app.put('/producto/{cod}')
def updateproducto(cod:int,
        nom:str=Body(),
        val:float=Body(),
        exi:int=Body()):
        for prod in productos:
            if prod['codigo']==cod:
                prod['nombre']=nom
                prod['valor']=val
                prod['existencias']=exi
        return productos

@app.delete('/prductos/{cod}')
def deleteProductos(cod:int):
    for prod in productos:
        if prod['codigo']==cod:
            productos.remove(prod)
    return productos
