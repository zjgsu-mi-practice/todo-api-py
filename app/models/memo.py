from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, String, DateTime, Text
from sqlalchemy.sql import func

from app.models.base import Base

class Memo(Base):
    __tablename__ = "memos"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    def __repr__(self):
        return f"<Memo(id={self.id})>" 