# Documentacao lib psycopg
# https://www.psycopg.org/psycopg3/docs/basic/usage.html

from . import *

class PostgresSQL(DatabaseConection):
  """DataBase PosgresSQL"""
  
  def __init__(self):
    self.__dbname = config["POSTGRES_DBNAME"]
    self.__dbuser = config["POSTGRES_DBUSER"]
    self.__dbpassword = config["POSTGRES_DBPASSWORD"]
    self.__dbhost = config["POSTGRES_DBHOST"]
    self.__dbport = config["POSTGRES_DBPORT"]
    self.connect_db()
    
  def connect_db(self):
    return psycopg.connect(
        dbname=self.__dbname,
        user=self.__dbuser,
        password=self.__dbpassword,
        host=self.__dbhost,
        port=self.__dbport
    )

  async def sqlDQL(self, scripSQL:str, *args) -> dict:
    """Select in database
    
    Keyword arguments:
    scripSQL -- Pass the query as an argument
    *args -- Pass query filters as an argument, if necessary
    Return: Specified query
    """
    
    conn = self.connect_db()
    cursor = conn.cursor()
    try:
      cursor.execute(scripSQL, *args)
      result = cursor.fetchall()
      return result
    
    except Exception as e:
      return {"Error": e}
    
    finally:
      cursor.close()
      conn.close()

  async def sqlDML(self, scripSQL:str, *args) -> dict:
    """Insert, update or delete in database
    
    Keyword arguments:
    scripSQL -- Pass the query as an argument
    *args -- Pass query values as an argument, if necessary
    Return: Database status or response return
    """
    conn = self.connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute(scripSQL, *args)
        response = cursor.fetchone()[0]
        conn.commit()
        return {"res": response}
      
    except Exception as e:
        return {"Error": e}
      
    finally:
        cursor.close()
        conn.close()
