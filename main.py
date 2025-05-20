from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Tarea(BaseModel):
    id: int
    titulo: str
    completado: bool = False

tareas_db: List[Tarea] = []

@app.get("/")
def leer_root():
    return {"mensaje": "API de tareas operativa"}

@app.get("/tareas", response_model=List[Tarea])
def listar_tareas():
    return tareas_db

@app.post("/tareas", response_model=Tarea)
def crear_tarea(tarea: Tarea):
    tareas_db.append(tarea)
    return tarea
