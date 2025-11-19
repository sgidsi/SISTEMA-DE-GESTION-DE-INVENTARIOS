from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.usuarios import UsuarioCreate, UsuarioUpdate, UsuarioResponse
from app.services.usuarios_service import (
    create_usuario, get_usuarios, get_usuario, update_usuario, delete_usuario
)

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.post("/", response_model=UsuarioResponse)
def crear_usuario(data: UsuarioCreate, db: Session = Depends(get_db)):
    return create_usuario(db, data)

@router.get("/", response_model=list[UsuarioResponse])
def listar_usuarios(db: Session = Depends(get_db)):
    return get_usuarios(db)

@router.get("/{usuario_id}", response_model=UsuarioResponse)
def obtener_usuario(usuario_id: int, db: Session = Depends(get_db)):
    user = get_usuario(db, usuario_id)
    if not user:
        raise HTTPException(404, "Usuario no encontrado")
    return user

@router.put("/{usuario_id}", response_model=UsuarioResponse)
def actualizar_usuario(usuario_id: int, data: UsuarioUpdate, db: Session = Depends(get_db)):
    user = update_usuario(db, usuario_id, data)
    if not user:
        raise HTTPException(404, "Usuario no encontrado")
    return user

@router.delete("/{usuario_id}")
def eliminar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    if not delete_usuario(db, usuario_id):
        raise HTTPException(404, "Usuario no encontrado")
    return {"message": "Usuario eliminado"}
