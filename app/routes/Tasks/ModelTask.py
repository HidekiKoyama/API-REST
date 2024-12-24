from . import *

class Task(BaseModel):
  categoria: str
  descricao: str
  tarefaok: bool
  
router = APIRouter()

@router.get("/task/")
async def main():
  db = DataBase(PostgresSQL())
  dados = await db.sqlDQL("select * from tarefas")
  return dados
