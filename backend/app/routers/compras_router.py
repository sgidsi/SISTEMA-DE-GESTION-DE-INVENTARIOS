from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.compras import CompraCreate, CompraResponse
from app.services.compras_service import create_compra, get_compras, get_compra

router = APIRouter(prefix="/compras", tags=["Compras"])

@router.post("/", response_model=CompraResponse)
def crear(data: CompraCreate, db: Session = Depends(get_db)):
    return create_compra(db, data)

@router.get("/", response_model=list[CompraResponse])
def listar(db: Session = Depends(get_db)):
    return get_compras(db)

@router.get("/{compra_id}", response_model=CompraResponse)
def obtener(compra_id: int, db: Session = Depends(get_db)):
    compra = get_compra(db, compra_id)
    if not compra:
        raise HTTPException(404, "Compra no encontrada")
    return compra
