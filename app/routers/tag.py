from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from app.database import get_db
from app.models.tag import Tag
from app.schemas.tag import TagCreate, TagUpdate, TagInDB

router = APIRouter(prefix="/tags", tags=["tags"])

@router.get("/", response_model=List[TagInDB])
async def list_tags(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Tag))
    tags = result.scalars().all()
    return [TagInDB.model_validate(tag) for tag in tags]

@router.post("/", response_model=TagInDB, status_code=201)
async def create_tag(tag: TagCreate, db: AsyncSession = Depends(get_db)):
    db_tag = Tag(**tag.model_dump())
    db.add(db_tag)
    await db.commit()
    await db.refresh(db_tag)
    return TagInDB.model_validate(db_tag) 