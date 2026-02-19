from fastapi import FastAPI # 1. Importar FastAPI [cite: 53]

app = FastAPI(title="miniblog") # 2. Instancia con título [cite: 54]

@app.get("/") # 3. Decorador de ruta inicial [cite: 55]
async def home(): # 4. Función asíncrona 
    return {"message": "Hola Mon"} # Retorna un JSON/Diccionario