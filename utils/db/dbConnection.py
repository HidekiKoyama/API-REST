from . import DatabaseConection

class DataBase:
  """DataBase connect"""
  
  def __init__(self, connection : DatabaseConection):
    self.connection = connection
  
  async def sqlDQL(self, scripSQL:str, *args) -> dict:
    """Select in database
    
    Keyword arguments:
    scripSQL -- Pass the query as an argument
    *args -- Pass query filters as an argument, if necessary
    Return: Specified query
    """
    return await self.connection.sqlDQL(scripSQL, *args)
  
  async def sqlDML(self, scripSQL:str, *args) -> dict:
    """Insert, update or delete in database
    
    Keyword arguments:
    scripSQL -- Pass the query as an argument
    *args -- Pass query values as an argument, if necessary
    Return: Database status or response return
    """
    return await self.connection.sqlDML(scripSQL, *args)
