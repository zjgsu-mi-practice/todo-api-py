from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from app.database import get_db
from app.models.memo import Memo
from app.schemas.memo import MemoCreate, MemoUpdate, MemoInDB

router = APIRouter(prefix="/memos", tags=["memos"])

@router.get("/{memo_id}", response_model=MemoInDB)
async def get_memo(memo_id: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Memo).where(Memo.id == memo_id))
    memo = result.scalar_one_or_none()
    if not memo:
        raise HTTPException(status_code=404, detail="Memo not found")
    return MemoInDB.model_validate(memo)

@router.put("/{memo_id}", response_model=MemoInDB)
async def update_memo(memo_id: str, memo_update: MemoUpdate, db: AsyncSession = Depends(get_db)):
    # Check if memo exists
    result = await db.execute(select(Memo).where(Memo.id == memo_id))
    if not result.scalar_one_or_none():
        raise HTTPException(status_code=404, detail="Memo not found")
    
    # Update memo
    update_data = memo_update.model_dump(exclude_unset=True)
    await db.execute(
        update(Memo)
        .where(Memo.id == memo_id)
        .values(**update_data)
    )
    await db.commit()
    
    # Return updated memo
    result = await db.execute(select(Memo).where(Memo.id == memo_id))
    return MemoInDB.model_validate(result.scalar_one()) 