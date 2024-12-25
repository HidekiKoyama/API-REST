from . import *
  
app = FastAPI()

app.include_router(ModelTask.router, prefix="/api/v1", tags=["task"])

@app.get("/api/v1/")
async def main():
  return {"message" : "Welcome the API!"}
