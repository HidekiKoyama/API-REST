  
def load_queries():
  """Load all queries into memory cache"""
  from pathlib import Path
  queries = {}
  for path in Path("./queries/QueriesTasks/").glob("*.sql"):
      queries[path.stem] = path.read_text()
  return queries
