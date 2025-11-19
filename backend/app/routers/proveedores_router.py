from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.proveedores import ProveedorCreate, ProveedorUpdate, ProveedorResponse
from app.services.proveedores_service import (
    create_proveedor, get_proveedores, get_proveedor,
    update_proveedor, delete_proveedor
)

router = APIRouter(prefix="/proveedores", tags=["Proveedores"])

@router.post("/", response_model=ProveedorResponse)
def crear(data: ProveedorCreate, db: Session = Depends(get_db)):
    return create_proveedor(db, data)

@router.get("/", response_model=list[ProveedorResponse])
def listar(db: Session = Depends(get_db)):
    return get_proveedores(db)

@router.get("/{proveedor_id}", response_model=ProveedorResponse)
def obtener(proveedor_id: int, db: Session = Depends(get_db)):
    prov = get_proveedor(db, proveedor_id)
    if not prov:
        raise HTTPException(404, "Proveedor no encontrado")
    return prov

@router.put("/{proveedor_id}", response_model=ProveedorResponse)
def actualizar(proveedor_id: int, data: ProveedorUpdate, db: Session = Depends(get_db)):
    prov = update_proveedor(db, proveedor_id, data)
    if not prov:
        raise HTTPException(404, "Proveedor no encontrado")
    return prov

@router.delete("/{proveedor_id}")
def eliminar(proveedor_id: int, db: Session = Depends(get_db)):
    if not delete_proveedor(db, proveedor_id):
        raise HTTPException(404, "Proveedor no encontrado")
    return {"message": "Proveedor eliminado"}
