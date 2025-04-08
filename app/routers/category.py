from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from app.database import get_db
from app.models.category import Category
from app.schemas.category import CategoryCreate, CategoryUpdate, CategoryInDB

router = APIRouter(prefix="/categories", tags=["categories"])

@router.get("/", response_model=List[CategoryInDB])
async def list_categories(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Category))
    categories = result.scalars().all()
    return [CategoryInDB.model_validate(category) for category in categories]

@router.post("/", response_model=CategoryInDB, status_code=201)
async def create_category(category: CategoryCreate, db: AsyncSession = Depends(get_db)):
    db_category = Category(**category.model_dump())
    db.add(db_category)
    await db.commit()
    await db.refresh(db_category)
    return CategoryInDB.model_validate(db_category) 