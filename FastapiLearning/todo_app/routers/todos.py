from typing import List
from fastapi import APIRouter
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from schemas.todo import TodoBase
from models.todo import Todo
from core.db import SessionLocal, engine, get_db
from crud.todo import *


router = APIRouter()


@router.post('/add', response_model=TodoBase)
def add_todo(todo: TodoBase, db: Session = Depends(get_db)):
    db_todo = get_todo(db, id=todo.id)
    if db_todo:
        raise HTTPException(status_code=400, detail="Todo already exists")
    return create_todo(db, todo=todo)


@router.get('/read', response_model=List[TodoBase])
def read_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    todos = get_todos(db, skip, limit)
    return todos
