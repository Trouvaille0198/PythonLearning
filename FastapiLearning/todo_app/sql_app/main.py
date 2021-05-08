from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
import models
import schemas
import crud
from database import SessionLocal, engine

from fastapi import APIRouter
app = FastAPI()
router = APIRouter(
    prefix='/api',
    tags=['todo api']
)
origins = [
    "http://localhost:8080",
    'http//192.168.1.101'
    'http//192.168.1.107'

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/todos/', response_model=schemas.Todo)
def create_todo(todo: schemas.Todo, db: Session = Depends(get_db)):
    db_todo = crud.get_todo(db, id=todo.id)
    if db_todo:
        raise HTTPException(status_code=400, detail="Todo already exists")
    return crud.create_todo(db, todo=todo)


@app.get('/todos/', response_model=List[schemas.Todo])
def read_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    todos = crud.get_todos(db, skip, limit)
    return todos
