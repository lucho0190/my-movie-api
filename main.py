from fastapi import FastAPI # Import la clase fastapi de la librería fastapi
from fastapi.responses import HTMLResponse # Import la clase HTMLResponse de la librería fastapi.responses

from movies_list import movies_list # Importar la variable movies_list
app = FastAPI() # Crear una instancia de la clase fastapi

app.title = 'Mi Primera Aplicación de Películas y Análisis de Datos' # Asignar un valor a la variable title
app.version = '0.0.1' # Asignar un valor a la variable version

@app.get('/', tags=['Home']) # estamos definiendo una ruta

def message(): # definimos una función de la ruta
    return HTMLResponse('<h1>Hello, World!</h1>') # retorna un objeto de la clase HTMLResponse

@app.get('/movies', tags=['Movies']) # estamos definiendo una ruta de la clase fastapi
def movies(): # definimos una función de la ruta
    return movies_list
@app.get('/movies/{id}', tags=['Movies']) # estamos definiendo una ruta para consultar peliculas por id
def get_movie(id:int): # definimos una función de la rut
    for item in movies_list:
        if item['id'] == id:
            return item
    return []