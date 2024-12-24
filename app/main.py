from . import *
  
app = FastAPI()

app.include_router(ModelTask.router, prefix="/api/v1", tags=["task"])

@app.get("/api/v1/")
async def main():
  return {"message" : "Welcome the API!"}

# @app.post("/create_task/")
# async def insert_tarefa(tarefa: Task):
#     tarefa_id = str(uuid.uuid4())
#     return await insertData(tarefa_id, tarefa.categoria, tarefa.descricao, tarefa.tarefaok)

# @app.get("/get_task/")
# async def get_task(tarefa: Item):
#   return await get_task_db(tarefa.tarefa)
