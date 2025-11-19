from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.clientes import ClienteCreate, ClienteUpdate, ClienteResponse
from app.services.clientes_service import (
    create_cliente, get_clientes, get_cliente,
    update_cliente, delete_cliente
)

router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.post("/", response_model=ClienteResponse)
def crear(data: ClienteCreate, db: Session = Depends(get_db)):
    return create_cliente(db, data)

@router.get("/", response_model=list[ClienteResponse])
def listar(db: Session = Depends(get_db)):
    return get_clientes(db)

@router.get("/{cliente_id}", response_model=ClienteResponse)
def obtener(cliente_id: int, db: Session = Depends(get_db)):
    cli = get_cliente(db, cliente_id)
    if not cli:
        raise HTTPException(404, "Cliente no encontrado")
    return cli

@router.put("/{cliente_id}", response_model=ClienteResponse)
def actualizar(cliente_id: int, data: ClienteUpdate, db: Session = Depends(get_db)):
    cli = update_cliente(db, cliente_id, data)
    if not cli:
        raise HTTPException(404, "Cliente no encontrado")
    return cli

@router.delete("/{cliente_id}")
def eliminar(cliente_id: int, db: Session = Depends(get_db)):
    if not delete_cliente(db, cliente_id):
        raise HTTPException(404, "Cliente no encontrado")
    return {"message": "Cliente eliminado"}
