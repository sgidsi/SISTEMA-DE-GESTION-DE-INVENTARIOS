from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.inventarios import InventarioCreate, InventarioUpdate, InventarioResponse
from app.services.inventarios_service import (
    get_inventarios, get_inventario, update_inventario
)

router = APIRouter(prefix="/inventarios", tags=["Inventarios"])

@router.get("/", response_model=list[InventarioResponse])
def listar(db: Session = Depends(get_db)):
    return get_inventarios(db)

@router.get("/{inventario_id}", response_model=InventarioResponse)
def obtener(inventario_id: int, db: Session = Depends(get_db)):
    inv = get_inventario(db, inventario_id)
    if not inv:
        raise HTTPException(404, "Inventario no encontrado")
    return inv

@router.put("/{inventario_id}", response_model=InventarioResponse)
def actualizar(inventario_id: int, data: InventarioUpdate, db: Session = Depends(get_db)):
    inv = update_inventario(db, inventario_id, data)
    if not inv:
        raise HTTPException(404, "Inventario no encontrado")
    return inv
