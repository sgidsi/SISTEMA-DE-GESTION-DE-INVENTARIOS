from pydantic import BaseModel

class ProductoBase(BaseModel):
    nombre: str
    descripcion: str | None = None
    precio: float
    stock: int

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(BaseModel):
    nombre: str | None = None
    descripcion: str | None = None
    precio: float | None = None
    stock: int | None = None

class ProductoResponse(ProductoBase):
    id: int

    class Config:
        from_attributes = True
