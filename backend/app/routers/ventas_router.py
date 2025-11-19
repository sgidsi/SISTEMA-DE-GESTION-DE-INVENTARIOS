from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.ventas import VentaCreate, VentaResponse
from app.services.ventas_service import create_venta, get_ventas, get_venta

router = APIRouter(prefix="/ventas", tags=["Ventas"])

@router.post("/", response_model=VentaResponse)
def crear_venta(data: VentaCreate, db: Session = Depends(get_db)):
    return create_venta(db, data)

@router.get("/", response_model=list[VentaResponse])
def listar_ventas(db: Session = Depends(get_db)):
    return get_ventas(db)

@router.get("/{venta_id}", response_model=VentaResponse)
def obtener_venta(venta_id: int, db: Session = Depends(get_db)):
    venta = get_venta(db, venta_id)
    if not venta:
        raise HTTPException(404, "Venta no encontrada")
    return venta
