from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.categorias import CategoriaCreate, CategoriaUpdate, CategoriaResponse
from app.services.categorias_service import (
    create_categoria, get_categorias, get_categoria,
    update_categoria, delete_categoria
)

router = APIRouter(prefix="/categorias", tags=["Categorias"])

@router.post("/", response_model=CategoriaResponse)
def crear_categoria(data: CategoriaCreate, db: Session = Depends(get_db)):
    return create_categoria(db, data)

@router.get("/", response_model=list[CategoriaResponse])
def listar_categorias(db: Session = Depends(get_db)):
    return get_categorias(db)

@router.get("/{categoria_id}", response_model=CategoriaResponse)
def obtener_categoria(categoria_id: int, db: Session = Depends(get_db)):
    cat = get_categoria(db, categoria_id)
    if not cat:
        raise HTTPException(404, "Categoría no encontrada")
    return cat

@router.put("/{categoria_id}", response_model=CategoriaResponse)
def actualizar_categoria(categoria_id: int, data: CategoriaUpdate, db: Session = Depends(get_db)):
    cat = update_categoria(db, categoria_id, data)
    if not cat:
        raise HTTPException(404, "Categoría no encontrada")
    return cat

@router.delete("/{categoria_id}")
def eliminar_categoria(categoria_id: int, db: Session = Depends(get_db)):
    if not delete_categoria(db, categoria_id):
        raise HTTPException(404, "Categoría no encontrada")
    return {"message": "Categoría eliminada"}
