from abc import ABC, abstractmethod

class DatabaseConection(ABC):
  """ Interface to database"""
  @abstractmethod
  def connect_db(self):
    pass

  @abstractmethod
  async def sqlDQL(self, scripSQL: str, *args) -> dict:
    pass

  @abstractmethod
  async def sqlDML(self, scripSQL: str, *args) -> dict:
    pass
