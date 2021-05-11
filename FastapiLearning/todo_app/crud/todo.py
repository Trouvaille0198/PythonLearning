from sqlalchemy.orm import Session
from models.todo import Todo
from schemas.todo import TodoBase


# Create
def create_todo(db: Session, todo: TodoBase):
    db_todo = Todo(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


# Read
def get_todo(db: Session, id: int):
    return db.query(Todo).filter(Todo.id == id).first()


def get_todos(db: Session, skip: int = 0, limit: int = 0):
    return db.query(Todo).offset(skip).limit(limit).all()


# update
def change_done(db: Session, id: int):
    db_todo = db.query(Todo).filter(Todo.id == id).first()
    db_todo.is_done = not db_todo.is_done
    db.commit()
    db.flush()
    db.refresh(db_todo)
    return db_todo


# delete
def delete_todo(db: Session, id: int):
    db_todo = db.query(Todo).filter(Todo.id == id).first()
    if db_todo:
        db.delete(db_todo)
        db.commit()
        db.flush()
        return db_todo()
