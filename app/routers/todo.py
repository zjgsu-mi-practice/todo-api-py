from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List

from app.database import get_db
from app.models.todo import Todo as TodoModel
from app.schemas.todo import TodoCreate, TodoUpdate, Todo

router = APIRouter(prefix="/todos", tags=["todos"])

@router.get("/", response_model=List[Todo])
async def list_todos(
    skip: int = 0, 
    limit: int = 100,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(TodoModel).offset(skip).limit(limit))
    todos = result.scalars().all()
    return todos

@router.post("/", response_model=Todo)
async def create_todo(
    todo: TodoCreate, 
    db: AsyncSession = Depends(get_db)
):
    db_todo = TodoModel(**todo.dict())
    db.add(db_todo)
    await db.commit()
    await db.refresh(db_todo)
    return db_todo

@router.get("/{todo_id}", response_model=Todo)
async def get_todo(
    todo_id: str, 
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(TodoModel).filter(TodoModel.id == todo_id))
    todo = result.scalar_one_or_none()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.put("/{todo_id}", response_model=Todo)
async def update_todo(
    todo_id: str, 
    todo: TodoUpdate,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(TodoModel).filter(TodoModel.id == todo_id))
    db_todo = result.scalar_one_or_none()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    for field, value in todo.dict(exclude_unset=True).items():
        setattr(db_todo, field, value)
    
    await db.commit()
    await db.refresh(db_todo)
    return db_todo

@router.delete("/{todo_id}")
async def delete_todo(
    todo_id: str, 
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(TodoModel).filter(TodoModel.id == todo_id))
    todo = result.scalar_one_or_none()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    await db.delete(todo)
    await db.commit()
    return {"ok": True}