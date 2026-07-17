from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.product import (
    ProductCreate,
    ProductUpdate,
    ProductResponse,
    ProductStatus,
)
from app.services.product_service import (
    get_products,
    get_product,
    create_product,
    update_product,
    delete_product,
    update_status,
)

router = APIRouter(
    prefix="/products",
    tags=["Products"],
)


@router.get("/", response_model=list[ProductResponse])
def list_products(
    search: str = "",
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
):
    return get_products(db, search, skip, limit)


@router.get("/{product_id}", response_model=ProductResponse)
def get_product_by_id(
    product_id: int,
    db: Session = Depends(get_db),
):
    product = get_product(db, product_id)

    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    return product


@router.post("/", response_model=ProductResponse, status_code=201)
def create_new_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
):
    return create_product(db, product)


@router.put("/{product_id}", response_model=ProductResponse)
def edit_product(
    product_id: int,
    product: ProductUpdate,
    db: Session = Depends(get_db),
):
    updated = update_product(db, product_id, product)

    if not updated:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    return updated


@router.patch("/{product_id}/status", response_model=ProductResponse)
def change_status(
    product_id: int,
    data: ProductStatus,
    db: Session = Depends(get_db),
):
    product = update_status(db, product_id, data.status)

    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    return product


@router.delete("/{product_id}")
def remove_product(
    product_id: int,
    db: Session = Depends(get_db),
):
    deleted = delete_product(db, product_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    return {
        "message": "Producto eliminado correctamente"
    }