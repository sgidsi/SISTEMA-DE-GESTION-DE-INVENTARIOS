from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.productos import ProductoCreate, ProductoUpdate, ProductoResponse
from app.services.productos_service import (
    create_producto, get_productos, get_producto,
    update_producto, delete_producto
)

router = APIRouter(prefix="/productos", tags=["Productos"])

@router.post("/", response_model=ProductoResponse)
def crear_producto(data: ProductoCreate, db: Session = Depends(get_db)):
    return create_producto(db, data)

@router.get("/", response_model=list[ProductoResponse])
def listar_productos(db: Session = Depends(get_db)):
    return get_productos(db)

@router.get("/{producto_id}", response_model=ProductoResponse)
def obtener_producto(producto_id: int, db: Session = Depends(get_db)):
    producto = get_producto(db, producto_id)
    if not producto:
        raise HTTPException(404, "Producto no encontrado")
    return producto

@router.put("/{producto_id}", response_model=ProductoResponse)
def actualizar_producto(producto_id: int, data: ProductoUpdate, db: Session = Depends(get_db)):
    producto = update_producto(db, producto_id, data)
    if not producto:
        raise HTTPException(404, "Producto no encontrado")
    return producto

@router.delete("/{producto_id}")
def eliminar_producto(producto_id: int, db: Session = Depends(get_db)):
    if not delete_producto(db, producto_id):
        raise HTTPException(404, "Producto no encontrado")
    return {"message": "Producto eliminado"}
