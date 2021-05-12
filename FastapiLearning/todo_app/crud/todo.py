from sqlalchemy.orm import Session
from models.todo import Todo
from schemas.todo import TodoBase


# Create
def crud_create_todo(db: Session, todo: TodoBase):
    db_todo = Todo(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


# Read
def crud_get_todo(db: Session, id: int):
    return db.query(Todo).filter(Todo.id == id).first()


def crud_get_todos(db: Session, skip: int = 0, limit: int = 0):
    return db.query(Todo).offset(skip).limit(limit).all()


# update
def crud_update_todo(db: Session, todo: TodoBase):
    print(todo.dict())
    db_todo = db.query(Todo).filter(Todo.id == todo.id).first()
    for key, value in todo.dict().items():
        setattr(db_todo, key, value)
    db.add(db_todo)
    db.commit()
    # db.refresh(db_todo)
    return db_todo


# delete
def crud_delete_todo(db: Session, id: int):
    db_todo = db.query(Todo).filter(Todo.id == id).first()
    if db_todo:
        db.delete(db_todo)
        db.commit()
        # db.flush()
        return db_todo
