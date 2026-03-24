from fastapi import FastAPI,Body,HTTPException,Path

app=FastAPI()

productos = [
    
    {
        "codigo": 1,
        "nombre":"esfero",
        "valor":3500,
        "existencia":10
    }, 
    {
        "codigo": 2,
        "nombre":"cuaderno",
        "valor":5000,
        "existencia":15
    },
     {
        "codigo": 3,
        "nombre":"lapiz",
        "valor":200,
        "existencia":12
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
def findProductos(cod:int=Path(..., gt=0, descripcion="el codigo debe ser mayor a 0")):
    for prod in productos:
        if prod['codigo']==cod:
            return prod      
    raise HTTPException(status_code=404, detail=f"no se encontro el producto con el codigo {cod}")


@app .get('/productos/')
def findProductos2(nom:str):
    for prod in productos:
        if prod['nombre']==nom:
            return prod
    raise HTTPException(status_code =404,detail=f"no se encontro el producto con nombre {nom}")

@app.post('/productos')
def CreateProducto(
    nom:str=Body(...),
    val:float=Body(...,gt=0,description="el valor debe ser mayor a 0"),
    exi:int=Body(...,gt=0,descripcion="las existencias deben ser mayores a 0")):
    if productos:
        ultimo_codigo=max(prod['codigo']for prod in productos)
        nuevo_codigo=ultimo_codigo+1
    else:
        nuevo_codigo=1
    nuevo_pruducto={
        'codigo':nuevo_codigo,
        'nombre':nom,
        'valor':val,
        'existencia':exi,
    }
    productos.append({nuevo_pruducto})
    return {
        "mensaje":"producto creado exitosamente",
        "prosucto":nuevo_pruducto,
        "todos los productos":productos
    }

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
def updateproducto(
    cod:int=Path(...,gt=0,description="el codigo debe ser mayor a 0"),
    nom:str=Body(...),
    val:float=Body(...,gt=0,description="el vaor debe ser mayor a 0"),
    exi:int=Body(...,gt=0,description="las existencias deben ser mayores a 0")
):
    for prod in productos:
        if prod['codigo']==cod:
            prod['nombre']=nom
            prod['valor']=val
            prod['existencias']=exi
            return {
                "mensaje":"producto actualizado adecuadamente",
                "producto":prod,
                "todos los productos":productos
            }
    raise HTTPException(satus_code=404,detail=f"no se encontro el producto con el codigo {cod}")


@app.delete('/prductos/{cod}')
def deleteProductos(cod:int=Path(...,gt=0,description="el codigo debe ser mayor a 0")):
    for i,prod in enumerate(productos):
        if prod['codigo']==cod:
            producto_eliminado =productos.pop(i)
            return {
                "mensaje":"producto eliminado exitosamente",
                "producto_eliminado": producto_eliminado,
                "productos_restantes":productos              
            }
    raise HTTPException(status_code=404,detail=f"nose encontro el producto con el codigo {cod}")