from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base


class Todo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    created_time = Column(String)
    is_done = Column(Boolean)
