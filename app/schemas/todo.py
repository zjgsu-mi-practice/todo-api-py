from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, Field

class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: str = Field(default="pending", pattern="^(pending|in_progress|completed)$")
    due_date: Optional[datetime] = None
    category_id: Optional[str] = None
    tag_ids: Optional[List[str]] = None
    memo_id: Optional[str] = None

class TodoCreate(TodoBase):
    pass

class TodoUpdate(TodoBase):
    title: Optional[str] = None

class TodoInDB(TodoBase):
    id: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class PaginatedResponse(BaseModel):
    data: List[TodoInDB]
    pagination: dict = Field(
        default_factory=lambda: {
            "total": 0,
            "page": 1,
            "limit": 20
        }
    )