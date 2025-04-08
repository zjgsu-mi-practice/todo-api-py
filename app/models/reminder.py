from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.sql import func

from app.models.base import Base

class Reminder(Base):
    __tablename__ = "reminders"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    todo_id = Column(String, ForeignKey("todos.id"), nullable=False)
    time = Column(DateTime, nullable=False)
    notify_method = Column(String, nullable=False, default="push")
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    def __repr__(self):
        return f"<Reminder(id={self.id}, todo_id={self.todo_id}, time={self.time})>" 