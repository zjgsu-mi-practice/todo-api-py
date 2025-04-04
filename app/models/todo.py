from datetime import datetime
from typing import List, Optional
from uuid import UUID, uuid4

from sqlalchemy import Column, String, DateTime, ForeignKey, ARRAY
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.sql import func

from app.models.base import Base

class Todo(Base):
    __tablename__ = "todos"

    id = Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid4)
    title = Column(String, nullable=False)
    description = Column(String)
    status = Column(String, nullable=False, default="pending")
    due_date = Column(DateTime)
    category_id = Column(PG_UUID(as_uuid=True), ForeignKey("categories.id"))
    tag_ids = Column(ARRAY(PG_UUID(as_uuid=True)))
    memo_id = Column(PG_UUID(as_uuid=True), ForeignKey("memos.id"))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    def __repr__(self):
        return f"<Todo(id={self.id}, title='{self.title}')>"