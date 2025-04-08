from typing import List, Optional
from pydantic import BaseModel, Field, HttpUrl

class MemoBase(BaseModel):
    content: str
    attachments: Optional[List[HttpUrl]] = None

class MemoCreate(MemoBase):
    pass

class MemoUpdate(MemoBase):
    content: Optional[str] = None

class MemoInDB(MemoBase):
    id: str

    class Config:
        from_attributes = True 