from datetime import datetime
from typing import List, Optional
from uuid import uuid4

from sqlalchemy import Column, String, DateTime, ForeignKey, Text
from sqlalchemy.sql import func

from app.models.base import Base

class Todo(Base):
    __tablename__ = "todos"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    title = Column(String, nullable=False)
    description = Column(String)
    status = Column(String, nullable=False, default="pending")
    due_date = Column(DateTime)
    category_id = Column(String, ForeignKey("categories.id"))
    # Store as comma-separated values instead of ARRAY for SQLite compatibility
    tag_ids = Column(Text)  # Will store comma-separated UUIDs
    memo_id = Column(String, ForeignKey("memos.id"))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    def __repr__(self):
        return f"<Todo(id={self.id}, title='{self.title}')>"