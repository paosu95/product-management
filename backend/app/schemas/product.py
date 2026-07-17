from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class ProductBase(BaseModel):
    name: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Nombre del producto"
    )

    description: Optional[str] = Field(
        default=None,
        max_length=255
    )

    price: float = Field(
        ...,
        gt=0,
        description="Debe ser mayor que 0"
    )

    stock: int = Field(
        ...,
        ge=0,
        description="Debe ser mayor o igual a 0"
    )


class ProductCreate(ProductBase):
    status: bool


class ProductUpdate(ProductBase):
    status: bool


class ProductResponse(ProductBase):
    id: int
    status: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ProductStatus(BaseModel):
    status: bool