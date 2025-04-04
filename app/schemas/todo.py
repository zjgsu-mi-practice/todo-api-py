from datetime import datetime
from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel

class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: str = "pending"
    due_date: Optional[datetime] = None
    category_id: Optional[UUID] = None
    tag_ids: Optional[List[UUID]] = None
    memo_id: Optional[UUID] = None

class TodoCreate(TodoBase):
    pass

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    due_date: Optional[datetime] = None
    category_id: Optional[UUID] = None
    tag_ids: Optional[List[UUID]] = None
    memo_id: Optional[UUID] = None

class Todo(TodoBase):
    id: UUID
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True