from fastapi import FastAPI

app = FastAPI(title='Prueba de aplicación de FastAPI',
              description='Prueba automatizada de actualización del app en google Run, utilizando DockerFile')

@app.get('/')
async def root():
    return {'mensaje':'Hola desde FastAPI Test02'}
