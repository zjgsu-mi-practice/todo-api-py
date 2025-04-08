from pydantic import BaseModel
from typing import Optional

class TagBase(BaseModel):
    name: str

class TagCreate(TagBase):
    pass

class TagUpdate(TagBase):
    name: Optional[str] = None

class TagInDB(TagBase):
    id: str

    class Config:
        from_attributes = True 