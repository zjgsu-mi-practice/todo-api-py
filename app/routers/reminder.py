from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from app.database import get_db
from app.models.reminder import Reminder
from app.schemas.reminder import ReminderCreate, ReminderUpdate, ReminderInDB

router = APIRouter(prefix="/todos/{todo_id}/reminders", tags=["reminders"])

@router.get("/", response_model=List[ReminderInDB])
async def list_reminders(todo_id: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Reminder).where(Reminder.todo_id == todo_id))
    reminders = result.scalars().all()
    return [ReminderInDB.model_validate(reminder) for reminder in reminders]

@router.post("/", response_model=ReminderInDB, status_code=201)
async def create_reminder(todo_id: str, reminder: ReminderCreate, db: AsyncSession = Depends(get_db)):
    db_reminder = Reminder(**reminder.model_dump(), todo_id=todo_id)
    db.add(db_reminder)
    await db.commit()
    await db.refresh(db_reminder)
    return ReminderInDB.model_validate(db_reminder) 