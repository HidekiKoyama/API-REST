import psycopg

def connect_db():
  return psycopg.connect(
      dbname="apirest",
      user="postgres",       # Versao teste
      password="12345",      # Versao teste
      host="localhost",
      port="5432"
  )

async def read_users():
  conn = connect_db()
  cursor = conn.cursor()
  try:
    cursor.execute("SELECT * FROM tarefas;")
    users = cursor.fetchall()
    return users
  except Exception as e:
    print(f"Erro ao listar usuários: {e}")
  finally:
    cursor.close()
    conn.close()

async def insertData(id:str, categoria:str, descricao:str, tarefaok:bool):
  conn = connect_db()
  cursor = conn.cursor()
  try:
      cursor.execute(
          "INSERT INTO tarefas (id, categoria, descricao, tarefaok) VALUES (%s, %s, %s, %s) RETURNING id;",
          (id, categoria, descricao, tarefaok)
      )
      ins_id = cursor.fetchone()[0]
      conn.commit()
      return ins_id
  except Exception as e:
      return e
  finally:
      cursor.close()
      conn.close()

async def get_task_db(id:str):
  conn = connect_db()
  cursor = conn.cursor()
  
  try:
    # cursor.execute("SELECT * FROM tarefas;")
    cursor.execute("SELECT * FROM tarefas WHERE id = %s", (id,))
    users = cursor.fetchall()
    return users
  except Exception as e:
    print(f"Erro ao listar usuários: {e}")
  finally:
    cursor.close()
    conn.close()