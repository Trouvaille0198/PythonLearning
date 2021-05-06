from typing import List, Optional
from pydantic import BaseModel


class Todo(BaseModel):
    id: int
    content: str
    created_time: int
    is_done: bool

    class config:
        orm_mode = True
