from typing import Optional

from pydantic import BaseModel, Field


class ProductCreate(BaseModel):
    title: str = Field(max_length=150)
    price: int = Field(gt=0)

    category_id: int = Field(gt=0)


class ProductRead(BaseModel):
    id: int
    title: str
    price: int
    category_id: int

    class Config:
        from_attributes = True  # це дозволяє читати дані з SQLAlchemy моделей


class ProductUpdate(BaseModel):
    title: Optional[str] = Field(default=None, max_length=150)
    price: Optional[int] = Field(default=None, gt=0)
    category_id: Optional[int] = Field(default=None, gt=0)
