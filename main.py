from fastapi import FastAPI # Import la clase fastapi de la librería fastapi

app = FastAPI() # Crear una instancia de la clase fastapi

app.title = 'Mi Primera Aplicación de Películas y Análisis de Datos' # Asignar un valor a la variable title
app.version = '0.0.1' # Asignar un valor a la variable version

@app.get('/', tags=['Home']) # estamos definiendo una ruta

def message(): # definimos una función de la ruta
    return 'Hello World' # retornamos un diccionario


