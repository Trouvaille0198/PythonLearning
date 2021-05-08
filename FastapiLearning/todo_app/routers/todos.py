from typing import List
from fastapi import APIRouter
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from schemas.todo import TodoBase
from models.todo import Todo
from core.db import SessionLocal, engine, get_db


router = APIRouter()


@router.post('/todos/', response_model=TodoBase)
def create_todo(todo: TodoBase, db: Session = Depends(get_db)):
    db_todo = crud.get_todo(db, id=todo.id)
    if db_todo:
        raise HTTPException(status_code=400, detail="Todo already exists")
    return crud.create_todo(db, todo=todo)


@router.get('/todos/', response_model=List[TodoBase])
def read_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    todos = crud.get_todos(db, skip, limit)
    return todos
