from . import *

class CreateTask(BaseModel):
  category: str
  description: str
  task_ok: bool

class FilterTask(BaseModel):
  id : Optional[str] = "%"  
  category: Optional[str] = "%"
  description: Optional[str] = "%"
  task_ok: Optional[bool] = False

class UniqueTask(BaseModel):
  id : str  
  
router = APIRouter()

@router.get("/task/")
async def alltasks():
  """List all tasks in the database."""
  db = DataBase(PostgresSQL())
  data = await db.sqlDQL(QUERIES_TASKS.get("allTasks"))
  return data

@router.post("/create_task/")
async def insert_task(task: CreateTask):
  """Create tasks into the database."""
  task_id = str(uuid.uuid4())
  db = DataBase(PostgresSQL())
  data = await db.sqlDML(QUERIES_TASKS.get("insertTask"), 
                         task_id, task.category, task.description, task.task_ok)
  return data

@router.get("/get_task/")
async def get_task(item : FilterTask):
  """Get tasks from the database with optional filter."""
  db =  DataBase(PostgresSQL())
  data = await db.sqlDQL(QUERIES_TASKS.get("filterTasks"), 
                         item.id, item.category, item.description, item.task_ok)
  return data

@router.delete("/delete_task/")
async def delete_task(id_task: UniqueTask):
  """Delete tasks from the database by id"""
  db = DataBase(PostgresSQL())
  data = await db.sqlDML(QUERIES_TASKS.get("deleteTasks"), id_task.id)
  return data

@router.put("/alter_task/")
async def alter_task(id_task : FilterTask):
  """Alter status task"""
  db = DataBase(PostgresSQL())
  data = await db.sqlDML(QUERIES_TASKS.get("AlterTasks"), 
                          id_task.category, id_task.description, id_task.task_ok, id_task.id)
  return data
