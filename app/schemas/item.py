from pydantic import BaseModel, Field
from typing import Optional, List

# 定义一个 Category Schema


class Category(BaseModel):
    name: str
    description: Optional[str] = None

# 定义用于创建商品的 Schema


class ItemCreate(BaseModel):
    name: str = Field(..., example="A great item")
    description: Optional[str] = Field(None, example="A long description")
    price: float = Field(..., ge=0, example=9.99)  # 价格必须大于等于0
    tax: Optional[float] = Field(None, ge=0, example=1.5)
    category: Optional[Category] = None  # 包含另一个Pydantic模型

# 定义用于响应的商品 Schema


class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    is_on_sale: bool = Field(False, example=False)

    # 嵌套的Pydantic模型
    category: Optional[Category] = None

    class Config:
        from_attributes = True

# 定义一个包含多个商品的 Schema


class Items(BaseModel):
    items: List[Item]
