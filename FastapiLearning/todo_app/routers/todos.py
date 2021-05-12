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


@router.post('/create', response_model=TodoBase)
def create_todo(todo: TodoBase, db: Session = Depends(get_db)):
    db_todo = crud_get_todo(db, id=todo.id)
    if db_todo:
        raise HTTPException(status_code=400, detail="Todo already exists")
    return crud_create_todo(db, todo=todo)


@router.get('/get', response_model=List[TodoBase])
def get_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    todos = crud_get_todos(db, skip, limit)
    return todos


@router.post('/delete', response_model=TodoBase)
def delete_todos(todo: TodoBase, db: Session = Depends(get_db)):
    db_todo = crud_get_todo(db, id=todo.id)
    if not db_todo:
        raise HTTPException(status_code=400, detail="Todo doesn't exist")
    return crud_delete_todo(db, id=todo.id)


@router.put('/update', response_model=TodoBase)
def update_todos(todo: TodoBase, db: Session = Depends(get_db)):
    db_todo = crud_get_todo(db, id=todo.id)
    if not db_todo:
        raise HTTPException(status_code=400, detail="Todo doesn't exist")
    return crud_update_todo(db, todo=todo)
