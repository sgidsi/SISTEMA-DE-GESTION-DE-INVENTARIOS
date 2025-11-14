from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services import productos_service
from schemas.productos import ProductoCreate, ProductoUpdate, ProductoResponse
from core.config import get_db

router = APIRouter()

@router.get("/", response_model=list[ProductoResponse])
def listar_productos(db: Session = Depends(get_db)):
    productos = productos_service.get_productos(db)
    return {"status": "success", "data": productos, "message": ""}

@router.post("/", response_model=ProductoResponse)
def crear_producto(producto: ProductoCreate, db: Session = Depends(get_db)):
    nuevo_producto = productos_service.create_producto(db, producto)
    return {"status": "success", "data": nuevo_producto, "message": "Producto creado"}

@router.put("/{producto_id}", response_model=ProductoResponse)
def actualizar_producto(producto_id: int, producto: ProductoUpdate, db: Session = Depends(get_db)):
    actualizado = productos_service.update_producto(db, producto_id, producto)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"status": "success", "data": actualizado, "message": "Producto actualizado"}

@router.delete("/{producto_id}")
def eliminar_producto(producto_id: int, db: Session = Depends(get_db)):
    eliminado = productos_service.delete_producto(db, producto_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"status": "success", "data": eliminado, "message": "Producto eliminado"}
