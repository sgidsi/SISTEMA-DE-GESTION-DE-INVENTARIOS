from sqlalchemy.orm import Session
from app.models.productos import Producto
from app.schemas.productos import ProductoCreate, ProductoUpdate

def create_producto(db: Session, data: ProductoCreate):
    nuevo = Producto(**data.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def get_productos(db: Session):
    return db.query(Producto).all()

def get_producto(db: Session, producto_id: int):
    return db.query(Producto).filter(Producto.id == producto_id).first()

def update_producto(db: Session, producto_id: int, data: ProductoUpdate):
    producto = get_producto(db, producto_id)
    if not producto:
        return None

    for field, value in data.dict(exclude_unset=True).items():
        setattr(producto, field, value)

    db.commit()
    db.refresh(producto)
    return producto

def delete_producto(db: Session, producto_id: int):
    producto = get_producto(db, producto_id)
    if not producto:
        return None

    db.delete(producto)
    db.commit()
    return True
