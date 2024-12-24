from .db import *
import uuid
from typing import Union
from pydantic import BaseModel

from fastapi import FastAPI

class Task(BaseModel):
  categoria: str
  descricao: str
  tarefaok: bool

class Item(BaseModel):
  tarefa: str
  
app = FastAPI()

@app.get("/")
async def main():
  dados = await read_users()
  return dados

@app.post("/create_task/")
async def insert_tarefa(tarefa: Task):
    tarefa_id = str(uuid.uuid4())
    return await insertData(tarefa_id, tarefa.categoria, tarefa.descricao, tarefa.tarefaok)

@app.get("/get_task/")
async def get_task(tarefa: Item):
  return await get_task_db(tarefa.tarefa)