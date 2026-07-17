from sqlalchemy.orm import Session

from app.models.product import Product
from app.models.history import History


def get_products(
    db: Session,
    search: str = "",
    skip: int = 0,
    limit: int = 10,
):
    query = db.query(Product)

    if search:
        query = query.filter(Product.name.ilike(f"%{search}%"))

    return query.offset(skip).limit(limit).all()


def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()


def create_product(db: Session, product):
    new_product = Product(**product.model_dump())

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    history = History(
        product_id=new_product.id,
        product_name=new_product.name,
        action="Producto creado",
    )

    db.add(history)
    db.commit()

    return new_product


def update_product(db: Session, product_id: int, data):
    product = get_product(db, product_id)

    if not product:
        return None

    values = data.model_dump()

    for key, value in values.items():
        setattr(product, key, value)

    db.commit()
    db.refresh(product)

    history = History(
        product_id=product.id,
        product_name=product.name,
        action="Producto actualizado",
    )

    db.add(history)
    db.commit()

    return product


def delete_product(db: Session, product_id: int):
    product = get_product(db, product_id)

    if not product:
        return False

    history = History(
        product_id=product.id,
        product_name=product.name,
        action="Producto eliminado",
    )

    db.add(history)

    db.flush()

    db.delete(product)

    db.commit()

    return True


def update_status(db: Session, product_id: int, status: bool):
    product = get_product(db, product_id)

    if not product:
        return None

    product.status = status

    db.commit()
    db.refresh(product)

    history = History(
        product_id=product.id,
        product_name=product.name,
        action="Estado actualizado",
    )

    db.add(history)
    db.commit()

    return product