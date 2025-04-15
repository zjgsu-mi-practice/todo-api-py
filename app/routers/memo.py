from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
import json

from app.database import get_db
from app.models.memo import Memo
from app.schemas.memo import MemoCreate, MemoUpdate, MemoInDB

router = APIRouter(prefix="/memos", tags=["memos"])

@router.post("/", response_model=MemoInDB, status_code=201)
async def create_memo(memo: MemoCreate, db: AsyncSession = Depends(get_db)):
    # Convert attachments list to JSON string
    memo_data = memo.model_dump()
    if memo_data.get("attachments"):
        memo_data["attachments"] = json.dumps(memo_data["attachments"])
    
    db_memo = Memo(**memo_data)
    db.add(db_memo)
    await db.commit()
    await db.refresh(db_memo)
    
    # Convert attachments from JSON string to list
    memo_dict = db_memo.__dict__
    if memo_dict.get("attachments"):
        memo_dict["attachments"] = json.loads(memo_dict["attachments"])
    return MemoInDB.model_validate(memo_dict)

@router.get("/{memo_id}", response_model=MemoInDB)
async def get_memo(memo_id: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Memo).where(Memo.id == memo_id))
    memo = result.scalar_one_or_none()
    if not memo:
        raise HTTPException(status_code=404, detail="Memo not found")
    
    # Convert attachments from JSON string to list
    memo_dict = memo.__dict__
    if memo_dict.get("attachments"):
        memo_dict["attachments"] = json.loads(memo_dict["attachments"])
    return MemoInDB.model_validate(memo_dict)

@router.put("/{memo_id}", response_model=MemoInDB)
async def update_memo(memo_id: str, memo_update: MemoUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Memo).where(Memo.id == memo_id))
    memo = result.scalar_one_or_none()
    if not memo:
        raise HTTPException(status_code=404, detail="Memo not found")
    
    update_data = memo_update.model_dump(exclude_unset=True)
    if "attachments" in update_data:
        update_data["attachments"] = json.dumps(update_data["attachments"])
    
    await db.execute(
        update(Memo)
        .where(Memo.id == memo_id)
        .values(**update_data)
    )
    await db.commit()
    
    # Refresh the memo
    result = await db.execute(select(Memo).where(Memo.id == memo_id))
    updated_memo = result.scalar_one()
    
    # Convert attachments from JSON string to list
    memo_dict = updated_memo.__dict__
    if memo_dict.get("attachments"):
        memo_dict["attachments"] = json.loads(memo_dict["attachments"])
    return MemoInDB.model_validate(memo_dict) 