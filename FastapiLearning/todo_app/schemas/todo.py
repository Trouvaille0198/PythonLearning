from typing import List, Optional
from pydantic import BaseModel


class TodoBase(BaseModel):
    id: int
    content: str
    created_time: int
    is_done: bool = False

    class Config:
        orm_mode = True
