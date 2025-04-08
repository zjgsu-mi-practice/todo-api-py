from pydantic import BaseModel, Field
from typing import Optional

class CategoryBase(BaseModel):
    name: str
    color: Optional[str] = Field(None, pattern="^#[0-9A-Fa-f]{6}$")

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(CategoryBase):
    name: Optional[str] = None

class CategoryInDB(CategoryBase):
    id: str

    class Config:
        from_attributes = True 