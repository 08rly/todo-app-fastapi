from fastapi import FastAPI

from backend.routers import todo
from backend.db.schemas import SuccessMsg

app = FastAPI()
app.include_router(todo.router)

@app.get("/", response_model=SuccessMsg)
def root():
    return {"message": "Welcome to Fast API"}
