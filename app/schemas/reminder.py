from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional

class ReminderBase(BaseModel):
    todo_id: str
    time: datetime
    notify_method: str = Field(default="push", pattern="^(email|push|sms)$")

class ReminderCreate(ReminderBase):
    pass

class ReminderUpdate(ReminderBase):
    time: Optional[datetime] = None
    notify_method: Optional[str] = Field(None, pattern="^(email|push|sms)$")

class ReminderInDB(ReminderBase):
    id: str

    class Config:
        from_attributes = True 