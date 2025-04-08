from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func
from sqlalchemy.orm import selectinload

from app.database import get_db
from app.models.todo import Todo
from app.schemas.todo import TodoCreate, TodoUpdate, TodoInDB, PaginatedResponse

router = APIRouter(prefix="/todos", tags=["todos"])

@router.get("/", response_model=PaginatedResponse)
async def list_todos(
    status: Optional[str] = Query(None, pattern="^(pending|in_progress|completed)$"),
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db)
):
    # Build query
    query = select(Todo)
    if status:
        query = query.where(Todo.status == status)
    
    # Get total count
    count_query = select(func.count()).select_from(Todo)
    if status:
        count_query = count_query.where(Todo.status == status)
    total = (await db.execute(count_query)).scalar_one()
    
    # Apply pagination
    offset = (page - 1) * limit
    query = query.offset(offset).limit(limit)
    
    # Execute query
    result = await db.execute(query)
    todos = result.scalars().all()
    
    # Convert SQLAlchemy models to Pydantic models
    todo_models = [TodoInDB.model_validate(todo) for todo in todos]
    
    return PaginatedResponse(
        data=todo_models,
        pagination={
            "total": total,
            "page": page,
            "limit": limit
        }
    )

@router.post("/", response_model=TodoInDB, status_code=201)
async def create_todo(todo: TodoCreate, db: AsyncSession = Depends(get_db)):
    print(todo.model_dump())
    db_todo = Todo(**todo.model_dump())
    db.add(db_todo)
    await db.commit()
    await db.refresh(db_todo)
    return TodoInDB.model_validate(db_todo)

@router.get("/{todo_id}", response_model=TodoInDB)
async def get_todo(todo_id: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Todo).where(Todo.id == todo_id))
    todo = result.scalar_one_or_none()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return TodoInDB.model_validate(todo)

@router.put("/{todo_id}", response_model=TodoInDB)
async def update_todo(todo_id: str, todo_update: TodoUpdate, db: AsyncSession = Depends(get_db)):
    # Check if todo exists
    result = await db.execute(select(Todo).where(Todo.id == todo_id))
    if not result.scalar_one_or_none():
        raise HTTPException(status_code=404, detail="Todo not found")
    
    # Update todo
    update_data = todo_update.model_dump(exclude_unset=True)
    await db.execute(
        update(Todo)
        .where(Todo.id == todo_id)
        .values(**update_data)
    )
    await db.commit()
    
    # Return updated todo
    result = await db.execute(select(Todo).where(Todo.id == todo_id))
    return TodoInDB.model_validate(result.scalar_one())

@router.delete("/{todo_id}", status_code=204)
async def delete_todo(todo_id: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Todo).where(Todo.id == todo_id))
    if not result.scalar_one_or_none():
        raise HTTPException(status_code=404, detail="Todo not found")
    
    await db.execute(delete(Todo).where(Todo.id == todo_id))
    await db.commit()
    return None
